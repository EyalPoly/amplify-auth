# amplify-auth

Shared authentication providers for Amplify projects. Provides a reusable `CognitoAuthProvider` for authenticating against AWS Cognito User Pools with admin group verification.

## Installation

```bash
pip install amplify-auth
```

## Usage

### Standard Authentication

```python
from amplify_auth import CognitoAuthProvider

provider = CognitoAuthProvider(
    user_pool_id="us-east-1_xxxxx",
    client_id="your-client-id",
    region="us-east-1",
    admin_group_name="ADMINS",  # optional, defaults to "ADMINS"
)

if provider.authenticate("user@example.com", "password"):
    token = provider.get_id_token()
```

### Admin Authentication (AWS credentials required)

```python
if provider.authenticate_admin("user@example.com", "password", aws_profile="my-profile"):
    token = provider.get_id_token()
```

### Custom Provider

Extend `AuthenticationProvider` to create your own:

```python
from amplify_auth import AuthenticationProvider

class MyAuthProvider(AuthenticationProvider):
    def authenticate(self, username: str, password: str) -> bool:
        ...

    def get_id_token(self):
        ...

    def is_authenticated(self) -> bool:
        ...
```

## Features

- Standard Cognito USER_SRP_AUTH flow
- Admin ADMIN_USER_PASSWORD_AUTH flow
- MFA support (SMS and software token)
- Force password change handling
- Admin group membership verification
- JWT token management

## Development

```bash
# Clone and install
git clone https://github.com/EyalPoly/amplify-auth.git
cd amplify-auth
pip install -e ".[dev]"

# Run tests
pytest

# Type checking
mypy amplify_auth

# Formatting
black amplify_auth tests
```

## License

MIT