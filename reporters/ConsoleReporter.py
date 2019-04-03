import click

class ConsoleReporter:
  def report(self, metric, value, tags = {}):
    click.echo('Metric: %s, value: %s tags: %s' % (metric, value, tags))
