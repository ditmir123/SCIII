import Pyro4

@Pyro4.expose

class StringConcatenator:
    def concatenate(self, str1, str2):
        return str1 + str2

daemon = Pyro4.Daemon()
uri = daemon.register(StringConcatenator)

print('Server URI is:',uri)
daemon.requestLoop()

