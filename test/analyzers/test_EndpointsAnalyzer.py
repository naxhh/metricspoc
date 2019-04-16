import unittest

from analyzers import EndpointsAnalyzer


class TestEndpointsAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = EndpointsAnalyzer()

    def tearDown(self):
        self.analyzer = None

    def test_given_empty_projects_list_returns_empty(self):
        projects = []

        result = self.analyzer.analyze(projects)

        self.assertEqual(result, [])

    def test_given_not_supported_project_type_should_fail(self):
        projects = [{
            'type': 'not-supported'
        }]

        with self.assertRaises(Exception):
            self.analyzer.analyze(projects)
