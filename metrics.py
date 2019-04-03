import click

from configuration import configuration_for_vertical
from reporters import get_reporter
from analyzers import CommitAnalyzer

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
  click.echo('Retrieving sources for %s' % vertical)

@click.command()
@click.argument('vertical')
def delete(vertical):
  """Erase the source code"""
  click.echo('Erasing sources for %s' % vertical)

sources.add_command(get)
sources.add_command(delete)


@click.group()
def analyze():
  pass

@click.command()
@click.argument('vertical')
@click.option('--reporter', default='console', help='where to report the data')
def commits(vertical, reporter):
  """Analyzes changes in commits"""

  config = configuration_for_vertical(vertical)
  reporter = get_reporter(reporter)
  analyzer = CommitAnalyzer(reporter)

  analyzer.analyze(**config['analyzers']['commits'])

@click.command()
@click.argument('vertical')
@click.option('--reporter', default='console', help='where to report the data')
def endpoints(vertical, reporter):
  """Analyzes number of endpoints"""
  click.echo('Reporting endpoints of %s to %s' % vertical, reporter)

analyze.add_command(commits)
analyze.add_command(endpoints)

cli.add_command(sources)
cli.add_command(analyze)
