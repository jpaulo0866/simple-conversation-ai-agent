from pathlib import Path
from pydantic import BaseModel

class Config(BaseModel):
    session_id: str = ""
    history_file: str = "{}/.simple-conversation-agent/history.json".format(Path.home())
    model: str = "gpt-4o-mini"
    max_tokens: int = 1000
    temperature: int = 0
    system_role: str = "Você é uma assistente AI muito prestativa"

    @classmethod
    def get_default(cls):
        return cls(
            session_id="",
            history_file="{}/.simple-conversation-agent/history.json".format(Path.home()),
            model="gpt-4o-mini",
            max_tokens=1000, 
            temperature=0,
            system_role="Você é uma assistente AI muito prestativa"
        )

