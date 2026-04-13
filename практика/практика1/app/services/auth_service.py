from app.core.exceptions import PermissionDeniedError
from app.core.security import create_access_token, verify_password
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, users: UserRepository):
        self.users = users

    async def login(self, email: str, password: str) -> str:
        user = await self.users.get_by_email(email)
        if not user or not user.is_active:
            raise PermissionDeniedError("Invalid credentials")
        if not verify_password(password, user.password_hash):
            raise PermissionDeniedError("Invalid credentials")
        return create_access_token(str(user.id))
