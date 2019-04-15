import click

@click.group()
def sources():
  pass

@click.command()
@click.argument('vertical')
def get(vertical):
  """Retrieves the source code to be analyzed"""
  click.echo('Retrieving sources for %s' % vertical)

@click.command()
@click.argument('vertical')
def delete(vertical):
  """Erase the source code"""
  click.echo('Erasing sources for %s' % vertical)

sources.add_command(get)
sources.add_command(delete)
