import os
import re

from entities.EndpointProject import EndpointProject
from entities.EndpointMethod import EndpointMethod
from entities.EndpointParam import EndpointParam

class EndpointsAnalyzer:
  def analyze(self, projects):
    analyzed_projects = []

    for project in projects:
      if project['type'] != 'c#':
        raise Exception("Type '%s' for project is invalid " % project['type'])

      project = self._process_project(project['name'], project['folder'])

      analyzed_projects.append(project)

    return analyzed_projects
  def _process_project(self, project_name, controllers_folder):
    controller_files = os.listdir(controllers_folder)

    all_endpoints = []

    for controller in controller_files:
      methods = self._get_methods("%s/%s" % (controllers_folder, controller))
      endpoints = self._convert_to_endpoints(controller.strip('.cs'), methods)

      all_endpoints += endpoints

    return EndpointProject(project_name, all_endpoints)

  def _get_methods(self, file_path):
    with open(file_path) as file:
      file_content = [x.strip() for x in file.readlines()]

    public_accesors = [line for line in file_content if line.startswith('public ') and 'class' not in line]

    return public_accesors

  def _convert_to_endpoints(self, controller, accessors):
    # This regex retrieves 3 groups
    # group 1: Return object
    # group 2: method name
    # group 3: params (optional)
    method_regex = r'public ([^ ]+) ([^ ]+)\(([^\)]+)?\)'

    endpoints = []

    for line in accessors:
      match = re.search(method_regex, line)

      if match is None:
        continue

      response = match.group(1)
      method = match.group(2)
      raw_params = match.group(3)

      endpoints.append(
        EndpointMethod(response, controller, method, self._convert_params(raw_params))
      )

    return endpoints

  def _convert_params(self, raw_params):
    # This regex retrieves 2 groups but captures 3
    # group 1: Metadata like [FromBody]
    # group 2: param type
    # group 3: param name
    params_regex = r'(?:\[[^ ]+\])? ?([^ ]+) ([^ ]+)'

    params = []

    if raw_params is None:
      return params

    dirty_params = raw_params.split(',')

    for dirt_param in dirty_params:
      if dirt_param == '':
        continue

      match = re.search(params_regex, dirt_param.strip())

      param_type = match.group(1)
      param_name = match.group(2)

      params.append(EndpointParam(param_type, param_name))

    return params
