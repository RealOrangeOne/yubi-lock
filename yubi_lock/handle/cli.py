import click


@click.command('handle', short_help='Handler for inserting and removing drives')
@click.argument('type', type=click.Choice(["enable", "disable"]))
def cli(type):
    pass
