import pytest

from app.core.exceptions import PermissionDeniedError
from app.services.auth_service import AuthService


class DummyUser:
    def __init__(self, email: str, password_hash: str, is_active: bool = True):
        self.email = email
        self.password_hash = password_hash
        self.is_active = is_active


class DummyRepo:
    def __init__(self, user):
        self._user = user

    async def get_by_email(self, email: str):
        return self._user if self._user and self._user.email == email else None


@pytest.mark.asyncio
async def test_login_invalid_user() -> None:
    service = AuthService(DummyRepo(None))
    with pytest.raises(PermissionDeniedError):
        await service.login("nobody@example.com", "123")
