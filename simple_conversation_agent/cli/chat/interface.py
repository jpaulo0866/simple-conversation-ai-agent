from typing import Annotated
from rich import print
import typer

from simple_conversation_agent.agent.ai_agent import invoke, load_chain
from simple_conversation_agent.configuration.conf_service import ConfigTypes, set_config
from simple_conversation_agent.history.session_history import get_history

app = typer.Typer()

@app.command("new-chat", help="Starts a new chat")
def newChat(input: Annotated[str, typer.Option(prompt="Digite sua pergunta ou resposta: " )]):
    set_config(ConfigTypes.SESSION_ID, "")
    print(invoke(load_chain(), input))

@app.command("chat", help="Chat with AI assistant")
def chat(input: Annotated[str, typer.Option(prompt="Digite sua pergunta ou resposta: " )]):
    print(invoke(load_chain(), input))

@app.command("list-chats", help="Lists all chat channels")
def newChat():
    sessions = get_history("sessions")
    for session in sessions:
        print(f"chat_session_#{session}")

@app.command("use-chat", help="Use a chat ID")
def newChat(chat_id: Annotated[str, typer.Option(prompt="Qual o id de sessão?: " )]):
    sessions = get_history("sessions")

    for session in sessions:
        if str.lower(str.strip(chat_id)) == f"chat_session_#{session}":
            set_config(ConfigTypes.SESSION_ID, chat_id)
            print("OK!")
            return
        
    print("Chat ID não existe!")
    print("Confira os chats disponíveis em `list-chats`")