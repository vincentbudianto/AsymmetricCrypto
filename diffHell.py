

class DiffHell:
    """
    Class for Diffie-Hellman key exchange.
    """
    def __init__(self, x, n, g):
        """ Parameter Input.

        Keyword Arguments:
        x -- Special number chosen (must be inputted)
        n -- Agreed Prime (must be inputted)
        g -- Agreed Prime (must be less than n)
        """
        self.x = x
        if (g > x):
            raise Exception('g must be < n')
        self.g = g
        self.n = n
        self.X = (self.g ** self.x) % n
        self.Y = -1
        self.K = -1

    def __str__(self):
        x =   "x = " + str(self.x)
        g = "\ng = " + str(self.g)
        n = "\nn = " + str(self.n)
        X = "\nX = " + str(self.X)
        Y = "\nY = " + str(self.Y)
        K = "\nK = " + str(self.K)
        return x + g + n + X + Y + K

    def send(self):
        return self.X

    def agreedKey(self):
        return self.K

    def exchange(self, Y):
        self.Y = Y
        self.K = (self.Y ** self.x) % self.n