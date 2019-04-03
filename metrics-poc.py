import click

@click.group()
def cli():
  pass

@click.group()
def sources():
  pass

@click.command()
@click.argument('vertical')
def get(vertical):
  """Retrieves the source code to be analyzed"""
  click.echo('Retrieving sources for %s' % name)

@click.command()
@click.argument('vertical')
def delete(vertical):
  """Erase the source code"""
  click.echo('Erasing sources for %s' % name)

sources.add_command(get)
sources.add_command(delete)


@click.group()
def analyze():
  pass

@click.command()
@click.argument('vertical')
@click.option('--reporter', default='console', help='where to report the data')
def commits(vertical, reporter):
  click.echo('Reporting commits of %s to %s' % vertical, reporter)

@click.command()
@click.argument('vertical')
@click.option('--reporter', default='console', help='where to report the data')
def endpoints(vertical, reporter):
  click.echo('Reporting endpoints of %s to %s' % vertical, reporter)

analyze.add_command(commits)
analyze.add_command(endpoints)

cli.add_command(sources)
cli.add_command(analyze)

if __name__ == '__main__':
  cli()
