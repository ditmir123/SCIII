import Pyro4

@Pyro4.expose

class StringPalindrome:
    def palindrome(self, str1):
        if str1 == str1[::-1]:
            return 'a Palindrome'
        else:
            return 'not a Palindrome'

daemon = Pyro4.Daemon()
uri = daemon.register(StringPalindrome)

print('Server URI is:', uri)

daemon.requestLoop()
