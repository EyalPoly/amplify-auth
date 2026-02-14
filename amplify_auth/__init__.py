"""Shared authentication providers for Amplify projects."""

from .provider import AuthenticationProvider
from .cognito_auth import CognitoAuthProvider

__all__ = ["AuthenticationProvider", "CognitoAuthProvider"]
