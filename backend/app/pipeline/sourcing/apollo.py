import httpx
from app.pipeline.base import SourcingProvider
from app.core.config import settings


class ApolloSourcingProvider(SourcingProvider):
    BASE_URL = "https://api.apollo.io/v1"

    async def fetch_contacts(self, criteria: dict, limit: int) -> list[dict]:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.BASE_URL}/mixed_people/search",
                headers={"X-Api-Key": settings.apollo_api_key},
                json={**criteria, "per_page": limit},
            )
            response.raise_for_status()
            people = response.json().get("people", [])
            return [
                {
                    "email": p.get("email"),
                    "first_name": p.get("first_name"),
                    "last_name": p.get("last_name"),
                    "title": p.get("title"),
                    "company": p.get("organization", {}).get("name"),
                    "linkedin_url": p.get("linkedin_url"),
                }
                for p in people
                if p.get("email")
            ]
