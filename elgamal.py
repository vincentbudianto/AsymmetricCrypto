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

    def encrypt(self, m, k):
        """ Parameter Input.

        Keyword Arguments:
        m -- Random Number (must be inputted and fulfills condition 0 <= m <= p - 1)
        k -- Random Number (must be inputted and fulfills condition 1 <= k <= p - 2)
        """
        if (m < 0):
            raise Exception('m must be >= 0')

        if (m > (self.p - 1)):
            raise Exception('m must be <= (p - 1)')

        if (k < 1):
            raise Exception('k must be >= 1')

        if (k > (self.p - 2)):
            raise Exception('k must be <= (p - 2)')

        a = (self.g ** k) % self.p
        b = ((self.y ** k) * m) % self.p

        return a, b

    def decrypt(self, a, b):
        temp = (a ** (self.p - 1 - self.x)) % self.p
        m = (b * temp) % self.p

        return m