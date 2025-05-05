import Pyro4

uri = input('Enter the URI of the server:')
concatenator = Pyro4.Proxy(uri)

str1 = input('Enter the 1st string:')
str2 = input('Enter the 2nd string:')

result = concatenator.concatenate(str1, str2)
print('The concatenated string is:', result)
