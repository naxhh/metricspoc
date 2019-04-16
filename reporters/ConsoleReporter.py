import click
import json


class ConsoleReporter:
    printer = click

    def report(self, analyzer, data):
        self.printer.echo('{"analyzer": "%s", "payload": %s}' % (
            analyzer,
            json.dumps(data, default=lambda o: o.__dict__)
        ))

    def error(self, error_message):
        """This method allows us to report an error, other reporters may just raise the exception"""
        self.printer.echo(str(error_message))
