from entities.JsonSerializable import JsonSerializable


class EndpointMethod(JsonSerializable):

    def __init__(self, response, clazz, method, params):
        self.clazz = clazz
        self.method = method
        self.params = params
        self.response = response

    def __str__(self):
        return ('EndpointMethod(%s, %s, %s, %s)' % (
            self.response,
            self.clazz,
            self.method,
            [str(param) for param in self.params]
        ))
