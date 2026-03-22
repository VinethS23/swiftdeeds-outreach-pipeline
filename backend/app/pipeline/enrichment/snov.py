import httpx
from app.pipeline.base import EnrichmentProvider
from app.core.config import settings


class SnovEnrichmentProvider(EnrichmentProvider):
    AUTH_URL = "https://api.snov.io/v1/oauth/access_token"
    BASE_URL = "https://api.snov.io/v1"

    async def _get_token(self) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.post(self.AUTH_URL, data={
                "grant_type": "client_credentials",
                "client_id": settings.snov_client_id,
                "client_secret": settings.snov_client_secret,
            })
            response.raise_for_status()
            return response.json()["access_token"]

    async def enrich(self, contacts: list[dict]) -> list[dict]:
        token = await self._get_token()
        enriched = []
        async with httpx.AsyncClient() as client:
            for contact in contacts:
                email = contact.get("email")
                if not email:
                    continue
                response = await client.post(
                    f"{self.BASE_URL}/get-emails-verification-status",
                    headers={"Authorization": f"Bearer {token}"},
                    json={"emails": [email]},
                )
                if response.status_code != 200:
                    continue
                result = response.json().get("statuses", [{}])[0]
                if result.get("status") == "valid":
                    enriched.append({**contact, "verified": True})
        return enriched
