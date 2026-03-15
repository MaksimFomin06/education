from config.models import Config
from config.storage.json_storage import JSONStorage
from config.validators.url import URLValidator
from config.validators.selectors import SelectorsValidator
from config.validators.requirements import RequirementsValidator
 

class ConfigService:
    def __init__(self, storage: JSONStorage):
        self.storage = storage

    @staticmethod
    def create_config(url: str, selectors: dict, requirements: list) -> Config:
        validate_url = URLValidator.validate(url)
        validate_selectors = SelectorsValidator.validate(selectors)
        validate_requirements = RequirementsValidator.validate(requirements)

        return Config(
            url=validate_url,
            selectors=validate_selectors,
            requirements=validate_requirements
        )
    
    def save_config(self, config: Config, filepath: str) -> None:
        self.storage.save(config, filepath)
