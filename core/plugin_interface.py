from abc import ABC, abstractmethod
from fastapi import FastAPI

class MediaAddon(ABC):
    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def register_routes(self, app: FastAPI) -> None:
        """Register custom API endpoints for this addon."""
        pass
