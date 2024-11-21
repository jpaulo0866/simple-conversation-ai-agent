
import typer

from simple_conversation_agent.history.session_history import initialize_history_file

app = typer.Typer()

@app.command("init", help="Init History File")
def init():
   typer.echo(initialize_history_file())