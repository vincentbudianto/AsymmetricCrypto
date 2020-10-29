import random
import json
import backend.util.num as num

class Elgamal:
    """
    Class for elgamal key exchange.
    """
    def __init__(self, p, g, x):
        """ Parameter Input.

        Keyword Arguments:
        p -- Prime Number (must be inputted and fulfills condition 256 <= p <= 65536)
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

    def encrypt(self, data):
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
            a1 = a % 256
            a2 = (a // 256) % 256
            b = ((self.y ** k) * m) % self.p
            b1 = b % 256
            b2 = (b // 256) % 256

            out.append(a1)
            out.append(a2)
            out.append(b1)
            out.append(b2)

        return out

    def decrypt(self, data):
        out = []

        newData = []
        for i in range(0, len(data), 2):
            newData.append(data[i] + (data[i + 1] * 256))
        data = newData

        for i in range(0, len(data), 2):
            temp = (data[i] ** (self.p - 1 - self.x)) % self.p
            m = (data[i+1] * temp) % self.p
            out.append(m)

        return out

    def encryptText(self, text):
        """ Parameter Input.

        Keyword Arguments:
        m -- Random Number (must be inputted and fulfills condition 0 <= m <= p - 1)
        k -- Random Number (must be inputted and fulfills condition 1 <= k <= p - 2)
        """
        text = str(text)
        data = bytearray(text.encode("ascii"))
        data = list(data)
        out = []

        for m in data:
            if (m < 0):
                raise Exception('m must be >= 0')

            if (m > (self.p - 1)):
                raise Exception('m must be <= (p - 1)')

            k = random.randint(1, (self.p - 2))

            a = (self.g ** k) % self.p
            b = ((self.y ** k) * m) % self.p

            out.append(a)
            out.append(b)

        #Out array post-processing
        outText = []
        for i in range(0, len(out)):
            outText.append((out[i] % 95) +  32)
            outText.append(((out[i] // 95) % 95) +  32)

        outText = bytearray(outText)
        outText = outText.decode("ascii")
        return outText

    def decryptText(self, text):
        text = str(text)
        data = bytearray(text.encode("ascii"))
        data = list(data)
        out = []

        # Data pre-processing
        newData = []
        for i in range(0, len(data), 2):
            newData.append(((data[i+1]-32) * 95) + (data[i]-32))
        data = newData

        for i in range(0, len(data), 2):
            temp = (data[i] ** (self.p - 1 - self.x)) % self.p
            m = (data[i+1] * temp) % self.p
            out.append(m)

        outText = bytearray(out)
        outText = outText.decode("ascii")
        return outText