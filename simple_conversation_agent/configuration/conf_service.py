from enum import Enum
import json
import os
from pathlib import Path

from simple_conversation_agent.configuration.models import Config

class ConfigTypes(Enum):
    SESSION_ID = "session_id"
    HISTORY_FILE = "history_file"

def get_all_config_as_dict() -> dict:
    config = None
    try:
        with open("{}/.simple-conversation-agent/config.json".format(Path.home()), "r") as file:
            file_read = file.read()
            config = json.loads(file_read)
            return config
    except Exception as e:
        return ("Config not found {}".format(e))

def get_all_config() -> Config:
    return Config(**get_all_config_as_dict())

def get_config(configType: ConfigTypes):
    config = None
    try:
        with open("{}/.simple-conversation-agent/config.json".format(Path.home()), "r") as file:
            file_read = file.read()
            config = json.loads(file_read)
            return config[configType.value]
    except Exception as e:
        return ("Config not found {}".format(e))


def set_config(configType: ConfigTypes, value: str):
    config_read = get_all_config_as_dict()
    config_read[configType.value] = value
    config = Config(**dict(config_read))
    with open("{}/.simple-conversation-agent/config.json".format(Path.home()), "w") as file:
        file.write(json.dumps(config.model_dump()))
    return config

def initialize_config_file():
    dir_path = Path.home() / ".simple-conversation-agent"
    file_path = dir_path / "config.json"

    if not dir_path.exists():
        print("Criando diretório {}".format(dir_path))
        os.makedirs(dir_path)

    if not file_path.exists():
        default_config = Config().get_default()
        with open(file_path, "w") as file:
            json.dump(default_config.model_dump(), file)
