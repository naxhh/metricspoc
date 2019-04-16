from reporters.ConsoleReporter import ConsoleReporter
from reporters.DatadogReporter import DatadogReporter


def get_reporter(reporter, vertical):
    if reporter == 'datadog':
        return DatadogReporter(vertical)
    else:
        return ConsoleReporter()
