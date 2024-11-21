import typer

from simple_conversation_agent.configuration.conf_service import ConfigTypes, get_all_config, get_config, initialize_config_file, set_config

app = typer.Typer()

@app.command("init", help="Init Config File")
def init():
   typer.echo(initialize_config_file())

@app.command("list", help="List all keys from config")
def list():
   typer.echo(get_all_config())

@app.command("get", help="Get keys from config")
def get(key: ConfigTypes):
    typer.echo(get_config(key))

@app.command("set", help="Set value to config key. Ex: panvel-cli conf set key value")
def set(key: ConfigTypes, value : str):
    typer.echo(set_config(key, value))