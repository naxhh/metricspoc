import click

from scripts.analyze import analyze
from scripts.sources import sources

@click.group()
def cli():
  pass

cli.add_command(sources)
cli.add_command(analyze)
