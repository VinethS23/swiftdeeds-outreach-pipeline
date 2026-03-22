"""
Abstract base classes for each pipeline stage.
Swap providers by implementing these interfaces.
"""
from abc import ABC, abstractmethod
from typing import Any


class SourcingProvider(ABC):
    """Acquire a list of contacts matching given criteria."""

    @abstractmethod
    async def fetch_contacts(self, criteria: dict[str, Any], limit: int) -> list[dict]:
        ...


class EnrichmentProvider(ABC):
    """Verify and enrich a list of contacts."""

    @abstractmethod
    async def enrich(self, contacts: list[dict]) -> list[dict]:
        ...


class CampaignProvider(ABC):
    """Push contacts into a sending campaign."""

    @abstractmethod
    async def create_campaign(self, name: str, contacts: list[dict]) -> str:
        ...

    @abstractmethod
    async def start_campaign(self, campaign_id: str) -> bool:
        ...
