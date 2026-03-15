from dataclasses import dataclass, field

@dataclass
class Config:
    url: str
    selectors: dict[str, str]
    requirements: list[dict] = field(default_factory=list)
