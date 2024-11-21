from dotenv import load_dotenv
import typer

from simple_conversation_agent.cli.config.interface import app as config_app
from simple_conversation_agent.cli.chat.interface import app as ai_app
from simple_conversation_agent.cli.history.interface import app as history_app

from simple_conversation_agent.configuration.conf_service import initialize_config_file
from simple_conversation_agent.history.session_history import initialize_history_file

app = typer.Typer()

app.add_typer(config_app, name="config")
app.add_typer(ai_app, name="ai")
app.add_typer(history_app, name="history")

if __name__ == "__main__":
    load_dotenv()
    initialize_config_file()
    initialize_history_file()
    app()

    