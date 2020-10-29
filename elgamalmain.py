import elgamal

alice = elgamal.Elgamal(p = 2357, g = 2, x = 1751)
y1, g1, p1 = alice.getPublicKey()

bob = elgamal.Elgamal(p = 3337, g = 2, x = 1751)
y2, g2, p2 = bob.getPublicKey()
print('Before :')
print('y :', y2)
print('g :', g2)
print('p :', p2)
bob.setPublicKey(y = y1, g = g1, p = p1)
y3, g3, p3 = bob.getPublicKey()
print('After :')
print('y :', y3)
print('g :', g3)
print('p :', p3)

a, b = bob.encrypt(m = 2035, k = 1520)
print('Encryption :')
print('a :', a)
print('b :', b)

m = alice.decrypt(a = a, b = b)
print('Decryption :')
print('m :', m)