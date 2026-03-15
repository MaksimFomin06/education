from dataclasses import asdict
import json
from models import Config


class JSONStorage:
    @staticmethod
    def save(config: Config, filepath: str) -> None:
        config_to_dct = asdict(config)

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(config_to_dct, file, indent=4, ensure_ascii=False)
