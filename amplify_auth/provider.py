"""Abstract authentication provider interface."""

from abc import ABC, abstractmethod
from typing import Optional


class AuthenticationProvider(ABC):
    """Abstract base class for authentication providers."""

    @abstractmethod
    def authenticate(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def get_id_token(self) -> Optional[str]:
        pass

    @abstractmethod
    def is_authenticated(self) -> bool:
        pass
