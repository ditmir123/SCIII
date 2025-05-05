import xmlrpc.client

def main():
    server = xmlrpc.client.ServerProxy('http://localhost:8000')
    n = int(input('Enter the number to calculate the factorial:'))
    result = server.calculate_factorial(n)
    print('Factorial of',n,'is:',result)

if __name__ == '__main__':
    main()