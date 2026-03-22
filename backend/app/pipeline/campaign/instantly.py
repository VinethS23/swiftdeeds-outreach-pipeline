import httpx
from app.pipeline.base import CampaignProvider
from app.core.config import settings


class InstantlyCampaignProvider(CampaignProvider):
    BASE_URL = "https://api.instantly.ai/api/v1"

    @property
    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {settings.instantly_api_key}"}

    async def create_campaign(self, name: str, contacts: list[dict]) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.BASE_URL}/campaign/create",
                headers=self._headers,
                json={"name": name},
            )
            response.raise_for_status()
            campaign_id = response.json()["id"]

            await client.post(
                f"{self.BASE_URL}/lead/add",
                headers=self._headers,
                json={
                    "campaign_id": campaign_id,
                    "leads": [
                        {
                            "email": c["email"],
                            "first_name": c.get("first_name", ""),
                            "last_name": c.get("last_name", ""),
                            "company_name": c.get("company", ""),
                        }
                        for c in contacts
                    ],
                },
            )
            return campaign_id

    async def start_campaign(self, campaign_id: str) -> bool:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.BASE_URL}/campaign/launch",
                headers=self._headers,
                json={"campaign_id": campaign_id},
            )
            return response.status_code == 200
