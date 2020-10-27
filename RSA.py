import math
import random
import util.num as num

class RSA(object):
    """
    The RSA encryption/decryption algorithm
    """
    def __init__(self, seed=0, p=0, q=0, e=0):
        """ Key Creation.

        Keyword Arguments:
        seed -- random function seed (default 0)
        p -- a prime number (default 0)
        q -- a prime number not p (default 0)
        e -- a prime relative to totN (default 0)
        """
        self.name = "RSA algorithm."

        self.seed = seed
        random.seed(self.seed)

        # Check if p and q is prime
        if (not num.isPrime(p)):
            p = 0
        if (not num.isPrime(q)):
            q = 0

        # Find two random primes
        if (p == 0):
            candidate = random.randint(1000000000, 100000000000)
            if num.isPrime(candidate):
                self.p = candidate
        if (q == 0):
            candidate = random.randint(1000000000, 100000000000)
            if num.isPrime(candidate):
                self.q = candidate

        # Get n and totN
        self.n = p * q
        self.totN = (p - 1) * (q - 1)

        # Finds e, a prime relative to totN
        if (e != 0 and math.gcd(e, self.totN) != 1):
            e = 0

        if (e == 0):
            e = self.totN // 2
            while (math.gcd(e, self.totN) != 1 and e > 1):
                e = e - 1
            if (e > 1):
                self.e = e
            else:
                raise Exception('e')
        
        # Finds d, where d is a whole number and d = (1 + k * totN) / e and k is whole number
        d = 0.9
        k = 1
        while (not d.is_integer()):
            d = (1.0 + (k * totN)) / float(e)
            k = k + 1
        self.d = d

    def __str__(self):
        p = "p = " + str(self.p)
        q = "q = " + str(self.q)
        n = "n = " + str(self.n)
        totN = "totN = " + str(self.totN)
        e = "e = " + str(self.e)
        d = "d = " + str(self.d)
        return self.name + "\n" + p + "\n" + q + "\n" + n + "\n"+ totN + "\n" + e + "\n" + d + "\n"
