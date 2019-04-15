import click
import json

class ConsoleReporter:
  def report(self, analyzer, data):
    click.echo('{"analyzer": "%s", "payload": %s}' % (
      analyzer,
      json.dumps(data, default=lambda o: o.__dict__)
    ))

  def error(self, error_message):
    """This method allows us to report an error, other reporters may just raise the exception"""
    click.secho(str(error_message), err=True, bg='red')
