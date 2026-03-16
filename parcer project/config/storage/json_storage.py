from dataclasses import asdict
import json
from config.models import Config
import os


class JSONStorage:
    def __init__(self, base_dir: str = "config/configs"):
        self.base_dir = base_dir

        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def save(self, config: Config, filename: str) -> None:
        config_to_dct = asdict(config)

        filepath = os.path.join(self.base_dir, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(config_to_dct, file, indent=4, ensure_ascii=False)
