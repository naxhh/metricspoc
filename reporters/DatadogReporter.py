import click
from datadog import initialize, api

initialize()


class DatadogReporter:
    printer = click
    tracker = api

    def __init__(self, owner):
        self.owner = owner

    def report(self, analyzer, data):
        method = getattr(DatadogReporter, 'report_%s' % analyzer)

        method(self, data)

    def error(self, error_message):
        """This method allows us to report an error, other reporters may just raise the exception"""
        self.printer.echo(str(error_message))

    # Data is a List<EndpointProject>
    def report_endpoints(self, data):
        for project in data:
            metric = 'Elephant.endpoints.count'
            value = len(project.endpoints)
            tags = [
                'owner:%s' % self.owner,
                'project:%s' % project.project
            ]

            self.tracker.Metric.send(
                metric=metric,
                points=value,
                tags=tags,
                type='counter'
            )
