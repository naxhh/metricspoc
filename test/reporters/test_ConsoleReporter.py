import unittest
from unittest.mock import patch
import json

import reporters


class TestConsoleReporter(unittest.TestCase):

    def setUp(self):
        self.reporter = reporters.ConsoleReporter()

    def tearDown(self):
        self.reporter = None

    def test_report_otputs_a_json(self):
        with patch.object(self.reporter, 'printer') as mock:
            self.reporter.report('analyzer-name', {})

            mock.echo.assert_called_once()
            json_response = json.loads(mock.echo.call_args[0][0])

        self.assertEquals(json_response['analyzer'], 'analyzer-name')
        self.assertEquals(json_response['payload'], {})

    def test_error_returns_message(self):
        with patch.object(self.reporter, 'printer') as mock:
            self.reporter.error('some-error')

            response = mock.echo.call_args[0][0]

        self.assertEquals(response, 'some-error')


if __name__ == "__main__":
    unittest.main()
