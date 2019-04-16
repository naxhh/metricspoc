from reporters.ConsoleReporter import ConsoleReporter
from reporters.DatadogReporter import DatadogReporter


def get_reporter(reporter):
    if reporter == 'datadog':
        return DatadogReporter()
    else:
        return ConsoleReporter()
