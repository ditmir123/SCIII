import Pyro4

uri = input('Enter the URI of the Server:')
palindromer = Pyro4.Proxy(uri)

str1 = input('Enter the String to check Palindrome:')

result = palindromer.palindrome(str1)
print('The string ', str1, 'is',result)
