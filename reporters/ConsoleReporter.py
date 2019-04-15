import click

class ConsoleReporter:
  def report(self, metric, value, tags = {}):
    click.echo('Metric: %s, value: %s tags: %s' % (metric, value, tags))

  def error(self, error_message):
    """This method allows us to report an error, other reporters may do nothing"""
    click.echo(error_message, err=True)

  def debug(self, message):
    """This method allows us to debug, in other reporters it should do nothing"""
    click.secho("DEBUG: " + str(message), bg='red')
