from xmlrpc.server import SimpleXMLRPCServer

def arithmetic_calculation(a,b,o):
    if o == '+':
        return a+b
    elif o == '-':
        return a-b
    elif o == '*':
        return a*b
    elif o == '/':
        return a/b
    elif o == '//':
        return a//b
    elif o == '%':
        return a%b
    else:
        print('Please choose from the following arithmetic operations:+, -, *, /, //, %')
    
server = SimpleXMLRPCServer(('localhost',8000))
server.register_function(arithmetic_calculation,'calculate_arithmetic_calculation')
print('Server is ready to accept RPC calls')
server.serve_forever()
