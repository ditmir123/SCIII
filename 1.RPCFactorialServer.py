from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
server = SimpleXMLRPCServer(('localhost',8000))
server.register_function(factorial,'calculate_factorial')
print('Server is ready to accept RPC calls')
server.serve_forever()