from entities.JsonSerializable import JsonSerializable

class EndpointParam(JsonSerializable):
  def __init__(self, type, name):
    self.type = type
    self.name = name

  def __str__(self):
    return ('EndpointParam(%s, %s)' % (self.type, self.name))
