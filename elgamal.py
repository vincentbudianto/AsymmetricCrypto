import random
import json
import util.num as num

class Elgamal:
    """
    Class for elgamal key exchange.
    """
    def __init__(self, p, g, x):
        """ Parameter Input.

        Keyword Arguments:
        p -- Prime Number (must be inputted)
        g -- Random Number (must be inputted and less than p)
        x -- Random Number (must be inputted and fulfills condition 1 <= x <= p - 2)
        """
        self.p = p

        if (p < 256):
            raise Exception("P must be >= 256")

        if (p > 65536):
            raise Exception("P must be <= 65536")

        if (not num.isPrime(p)):
            raise Exception('p must be prime number')

        self.g = g

        if (g >= p):
            raise Exception('g must be < x')

        self.x = x

        if (x < 1):
            raise Exception('x must be >= 1')

        if (x > (p - 2)):
            raise Exception('x must be <= (p - 2)')

        self.y = (self.g ** self.x) % p

    def getPrivateKey(self):
        return self.x, self.p

    def setPrivateKey(self, x, p):
        self.x = x
        self.p = p

    def getPublicKey(self):
        return self.y, self.g, self.p

    def setPublicKey(self, y, g, p):
        self.y = y
        self.g = g
        self.p = p

    def writeToFile(self, filename):
        # Creates the dictionary
        pubDict = {
            'y' : self.y,
            'g' : self.g,
            'p' : self.p
        }

        priDict = {
            'x' : self.x,
            'p' : self.p
        }

        # Serializing json
        pubJson = json.dumps(pubDict, indent = 4)
        priJson = json.dumps(priDict, indent = 4)

        # Write to file
        with open(str(filename) + ".pri", "w") as outfile:
            outfile.write(priJson)
        with open(str(filename) + ".pub", "w") as outfile:
            outfile.write(pubJson)

    def encrypt(self, data) -> []:
        """ Parameter Input.

        Keyword Arguments:
        m -- Random Number (must be inputted and fulfills condition 0 <= m <= p - 1)
        k -- Random Number (must be inputted and fulfills condition 1 <= k <= p - 2)
        """
        out = []

        for m in data:
            if (m < 0):
                raise Exception('m must be >= 0')

            if (m > (self.p - 1)):
                raise Exception('m must be <= (p - 1)')

            k = random.randint(1, (self.p - 2))

            a = (self.g ** k) % self.p
            b = ((self.y ** k) * m) % self.p

            out.append([a, b])

        return out

    def decrypt(self, data) -> []:
        out = []

        for a, b in data:
            temp = (a ** (self.p - 1 - self.x)) % self.p
            m = (b * temp) % self.p
            out.append(m)

        return out