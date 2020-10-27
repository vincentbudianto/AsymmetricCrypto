import math
import random
import util.num as num
import json

class RSAKeygen(object):
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
        else:
            self.p = p
        if (not num.isPrime(q)):
            q = 0
        else:
            self.q = q

        # Find two random primes
        candidate = 0
        if (p == 0):
            while (not num.isPrime(candidate)):
                candidate = random.randint(10, 256)
            self.p = candidate
        candidate = 0
        if (q == 0):
            while ((not num.isPrime(candidate)) or candidate == self.p):
                candidate = random.randint(10, 256)
            self.q = candidate

        # Get n and totN
        self.n = self.p * self.q
        self.totN = ((self.p - 1) * (self.q - 1))

        # Finds e, a prime relative to totN
        if (e != 0 and math.gcd(e, self.totN) != 1):
            e = 0
        else:
            self.e = e

        if (e == 0):
            e = self.totN // 2
            while (math.gcd(e, self.totN) != 1 and e > 1):
                e = e - 1
            if (e > 1):
                self.e = e
            else:
                raise Exception('e')
        
        # Finds d, where d is a whole number and d = (1 + k * totN) / e and k is whole number
        print("finding d...")
        d = 0.9
        k = 1
        while (((1 + (k * self.totN)) % self.e) != 0):
            k += 1
            # print(k, (1 + (k * self.totN)), ((1 + (k * self.totN)) % self.e), self.e)
        d = (1.0 + (k * self.totN)) / float(self.e)
        if (d.is_integer()):
            d = int(d)
        else:
            raise Exception('d')
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

    def writeToFile(self, filename):
        # Creates the dictionary
        pubDict = {
            "e" : self.e,
            "n" : self.n
        }
        priDict = {
            "d" : self.d,
            "n" : self.n
        }

        # Serializing json  
        pubJson = json.dumps(pubDict, indent = 4) 
        priJson = json.dumps(priDict, indent = 4) 

        # Write to file
        with open(str(filename) + ".pri", "w") as outfile:
            outfile.write(priJson)
        with open(str(filename) + ".pub", "w") as outfile:
            outfile.write(pubJson) 
    
def encrypt(data, e, n) -> []:
    """ Encrypts data.
    Output size is doubled.
    Little Endian.

    Keyword Arguments:
    data -- an array of bytes ranging 0-255 (e.g. [0, 255, 64, 53, ...])
    """
    out = []
    for p in data:
        c = int(pow(p, e) % n)
        for i in range(0,2):
            cPart = c % 256
            out.append(cPart)
            c = c // 256
    return out

def decrypt(data, d, n) -> []:
    """ Decrypts data.
    Output size is halved.
    Little Endian.

    Keyword Arguments:
    data -- an array of bytes ranging 0-255 (e.g. [0, 255, 64, 53, ...])
    """
    out = []
    for i in range(0, len(data), 2):
        c = data[i] + (data[i+1] * 256)
        p = int(pow(c, d) % n)
        out.append(p)
    return out