import xmlrpc.client

def main():
    server = xmlrpc.client.ServerProxy('http://localhost:8000')
    o = input('Enter the arithmetic operator from the following arithmetic operations:+, -, *, /, //, % to calculate:')
    a = int(input('Enter value for a:'))
    b = int(input('Enter value for b:'))
    result = server.calculate_arithmetic_calculation(a,b,o)
    print('The result after the arithmetic calculation using operator',o,'is:',result)
    
if __name__ == '__main__':
    main()