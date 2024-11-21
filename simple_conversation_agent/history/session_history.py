import json
import os
from pathlib import Path
from simple_conversation_agent.configuration.conf_service import ConfigTypes, get_config
    
def get_all_history():
    history_file = get_config(ConfigTypes.HISTORY_FILE)
    with open(history_file, "r") as file:
        file_read = file.read()
        history = json.loads(file_read)
        return history
    
def get_history(session_id: str):
   return get_all_history()[session_id]

def get_history_file(session_id: str):
    dir_path = Path.home() / ".simple-conversation-agent"
    return dir_path / f"{session_id}.json"
    
def set_history(session_id: str, conversations):
    history_file = get_config(ConfigTypes.HISTORY_FILE)
    actual_history = get_all_history()

    for conversation in conversations:
        actual_history[session_id].append(conversation)
    
    with open(history_file, "w") as file:
        json.dump(actual_history, file)

def rewrite_history(session_id: str, conversations):
    history_file = get_config(ConfigTypes.HISTORY_FILE)
    actual_history = get_all_history()

    actual_history[session_id] = conversations
    
    with open(history_file, "w") as file:
        json.dump(actual_history, file)

def generate_session_id():
    sessions = get_history("sessions")

    if sessions is None or len(sessions) == 0:
        last = 0
    else:
        last = sessions[len(sessions)-1]

    if last is None:
        last = 0

    last = last + 1
    set_history("sessions", [last])
    return f"chat_session_#{last}"

def initialize_history_file():
    dir_path = Path.home() / ".simple-conversation-agent"
    file_path = dir_path / "history.json"

    if not dir_path.exists():
        print("Criando diretório {}".format(dir_path))
        os.makedirs(dir_path)

    if not file_path.exists():
        with open(file_path, "w") as file:
            json.dump({
                "sessions": []
            }, file)

