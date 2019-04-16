import unittest
from pyfakefs.fake_filesystem_unittest import TestCase

from analyzers import EndpointsAnalyzer


class TestEndpointsAnalyzer(TestCase):
    repos_path = 'repos/test'
    projects = [{
        'type': 'c#',
        'name': 'test-name',
        'folder': repos_path
    }]

    def setUp(self):
        self.setUpPyfakefs()
        self.fs.create_dir('repos/test')

        self.analyzer = EndpointsAnalyzer()

    def tearDown(self):
        self.analyzer = None

    def test_empty_projects_list_returns_empty(self):
        projects = []

        result = self.analyzer.analyze(projects)

        self.assertEqual(result, [])

    def test_not_supported_project_type_should_fail(self):
        projects = [{
            'type': 'not-supported'
        }]

        with self.assertRaises(Exception):
            self.analyzer.analyze(projects)

    def test_csharp_empty_path_should_return_zero_endpoints(self):
        projects = [{
            'type': 'c#',
            'name': 'test-name',
            'folder': 'empty-path'
        }]

        self.fs.create_dir('empty-path')

        result = self.analyzer.analyze(projects)

        self.assertEqual(len(result), 1)

        analyzed_project = result.pop()

        self.assertEqual(analyzed_project.project, 'test-name')
        self.assertEqual(len(analyzed_project.endpoints), 0)

    def test_csharp_empty_file_should_return_zero_endpoints(self):
        self.fs.create_file(self.repos_path + '/EmptyController.cs', contents="""
using Stuff;

namespace Controllers
{
    public class EmptyController : ApiController
    {
    }
}
            """)

        result = self.analyzer.analyze(self.projects).pop()

        self.assertEqual(len(result.endpoints), 0)

    def test_csharp_public_method_should_count_as_endpoint(self):
        self.fs.create_file(self.repos_path + '/SimpleEndpoint.cs', contents="""
using Stuff;

namespace Controllers
{
    public class SimpleEndpoint : ApiController
    {
        public HttpResponseMessage Get()
        {
            actual code
        }
    }
}
""")

        result = self.analyzer.analyze(self.projects).pop()

        self.assertEqual(len(result.endpoints), 1)

        endpoint = result.endpoints.pop()

        self.assertEqual(endpoint.clazz, 'SimpleEndpoint')
        self.assertEqual(endpoint.method, 'Get')
        self.assertEqual(len(endpoint.params), 0)

    def test_csharp_public_setter_should_not_count_as_endpoints(self):
        self.fs.create_file(self.repos_path + '/PublicSettersController.cs', contents="""
using Stuff;

namespace Controllers
{
    public class PublicSettersController : ApiController
    {
    }

    public Domain.BusinessRules.User.IUserService UserService
    {
        get
        {
            if (this._userService == null)
                this._userService = IoCFactory.Resolve<Domain.BusinessRules.User.IUserService>();

            return this._userService;
        }
        set
        {
            this._userService = value;
        }
    }
}
        """)

        result = self.analyzer.analyze(self.projects).pop()

        self.assertEqual(len(result.endpoints), 0)

    def test_csharp_params_should_be_parsed(self):
        self.fs.create_file(self.repos_path + '/EndpointWithParams.cs', contents="""
using Stuff;

namespace Controllers
{
    public class EndpointWithParams : ApiController
    {
        public HttpResponseMessage Get(int resourceId)
        {
            actual code
        }
    }
}
        """)

        result = self.analyzer.analyze(self.projects).pop()
        params = result.endpoints.pop().params

        self.assertEqual(len(params), 1)

        param = params.pop()
        self.assertEqual(param.type, 'int')
        self.assertEqual(param.name, 'resourceId')

    def test_csharp_params_should_remove_annotations(self):
        self.fs.create_file(self.repos_path + '/EndpointWithParams.cs', contents="""
using Stuff;

namespace Controllers
{
    public class EndpointWithParams : ApiController
    {
        public HttpResponseMessage Get([FromUri] int resourceId)
        {
            actual code
        }
    }
}
        """)

        result = self.analyzer.analyze(self.projects).pop()
        params = result.endpoints.pop().params

        self.assertEqual(len(params), 1)

        param = params.pop()
        self.assertEqual(param.type, 'int')
        self.assertEqual(param.name, 'resourceId')


if __name__ == "__main__":
    unittest.main()
