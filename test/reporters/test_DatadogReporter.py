import unittest
from unittest.mock import patch, call, ANY
import json

import reporters

from entities.EndpointProject import EndpointProject
from entities.EndpointMethod import EndpointMethod
from entities.EndpointParam import EndpointParam


class TestDatadogReporter(unittest.TestCase):

    def setUp(self):
        self.reporter = reporters.DatadogReporter('test-owner')

    def tearDown(self):
        self.reporter = None

    def test_report_fails_for_no_existing_reporter(self):
        with self.assertRaises(AttributeError):
            self.reporter.report('not-existing-analyzer', {})

    def test_reports_endpoints_count(self):
        data = [
            self.__generate_endpoints_data('test-project'),
            self.__generate_endpoints_data('test-second-project')
        ]

        with patch.object(self.reporter, 'tracker') as mock:
            self.reporter.report('endpoints', data)

            print(mock.Metric.send.mock_calls)
            mock.Metric.send.assert_has_calls([
                call(metric='Elephant.endpoints.count', points=2, tags=[
                     'owner:test-owner', 'project:test-project'], type=ANY),
                call(metric='Elephant.endpoints.count', points=2, tags=[
                     'owner:test-owner', 'project:test-second-project'], type=ANY)
            ], any_order=True)

    def test_error_returns_message(self):
        with patch.object(self.reporter, 'printer') as mock:
            self.reporter.error('some-error')

            response = mock.echo.call_args[0][0]

        self.assertEquals(response, 'some-error')

    def __generate_endpoints_data(self, project_name):
        endpoints = [
            EndpointMethod('HttpResponse', 'TestController', 'Get', EndpointParam('int', 'id')),
            EndpointMethod('HttpResponse', 'TestController', 'Post', EndpointParam('int', 'id'))
        ]

        return EndpointProject(project_name, endpoints)

if __name__ == "__main__":
    unittest.main()
