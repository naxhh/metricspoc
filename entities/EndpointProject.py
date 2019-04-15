from entities.JsonSerializable import JsonSerializable

class EndpointProject(JsonSerializable):
  def __init__(self, project, endpoints):
    self.project = project
    self.endpoints = endpoints

  def __str__(self):
    return ('EndpointProject(%s, %s)' % (
      self.project,
      [str(endpoint) for endpoint in self.endpoints]
    ))
