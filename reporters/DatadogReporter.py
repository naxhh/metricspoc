import click

# Just for PoC sake...
class DatadogReporter:
  def report(self, metric, value, tags = {}):
    click.echo('[DD] Metric: %s, value: %s tags: %s' % (metric, value, tags))
