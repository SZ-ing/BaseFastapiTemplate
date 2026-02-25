import yaml
from pathlib import Path
from .config_schemas import AppConfig


def loadConfig(config_path:str = "configs/configs.yaml"):
    with open(config_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    settings = AppConfig(**data)
    return settings