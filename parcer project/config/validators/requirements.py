class RequirementsValidator:
    NECESSARY_KEYS = {"field", "operator", "value"}
    FORBIDDEN_VALUES = {"", " ", None}
    @staticmethod
    def validate(requirements: list[dict]) -> list[dict]:
        for requirement in requirements:
            keys = requirement.keys()
            values = requirement.values()

            if set(keys) != RequirementsValidator.NECESSARY_KEYS:
                raise KeyError(f"В требовании '{requirement}' отсутствует нужный ключ")
            elif RequirementsValidator.FORBIDDEN_VALUES & set(values):
                raise ValueError(f"В требовании '{requirement}' пустое или запрещенное значение")

        return requirements