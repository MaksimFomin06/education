class SelectorsValidator:
    @staticmethod
    def validate(selectors: dict) -> dict:
        for key, value in selectors.items():
            if (not key) or (not value):
                raise ValueError("Ключи и значения не могут быть пустыми")

        return selectors