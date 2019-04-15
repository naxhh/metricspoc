import click

class DatadogReporter:
  def report(self, analyzer, data):
    method = getattr(DatadogReporter, 'report_%s' % analyzer)

    method(self, data)

  def error(self, error_message):
    """This method allows us to report an error, other reporters may just raise the exception"""
    click.secho(str(error_message), err=True, bg='red')

  # Data is a List<EndpointProject>
  def report_endpoints(self, data):
    for project in data:
      metric = 'Elephant.endpoints.count'
      value = len(project.endpoints)
      tags = [
        'project:%s' % project.project
      ]

      #datadog.metric(metric, value)
      click.echo("Metric: %s Value: %s Tags: %s" % (metric, value, tags))
