import click

from configuration import configuration_for_vertical
from reporters import get_reporter
from analyzers import EndpointsAnalyzer, CommitAnalyzer


@click.group()
def analyze():
    pass


@click.command()
@click.argument('vertical')
@click.option('--reporter', default='console', help='where to report the data')
def endpoints(vertical, reporter):
    """Analyzes the number of endpoints"""

    config = configuration_for_vertical(vertical)
    reporter = get_reporter(reporter, vertical)
    analyzer = EndpointsAnalyzer()

    try:
        result = analyzer.analyze(**config['analyzers']['endpoints'])
        reporter.report('endpoints', result)
    except Exception as err:
        reporter.error(err)


analyze.add_command(endpoints)
