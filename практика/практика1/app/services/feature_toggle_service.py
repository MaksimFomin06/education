from app.repositories.feature_toggle_repository import FeatureToggleRepository


class FeatureToggleService:
    def __init__(self, repo: FeatureToggleRepository):
        self.repo = repo

    async def is_enabled(self, name: str, *, default: bool = False) -> bool:
        try:
            return await self.repo.is_enabled(name)
        except Exception:
            # Temporary compromise: avoid killing request path if toggles DB has issues.
            return default
