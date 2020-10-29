import diffHell

alice = diffHell.DiffHell(36, 97, 5)
bob = diffHell.DiffHell(58, 97, 5)
alice.exchange(bob.send())
bob.exchange(alice.send())
print("alice = ", alice)
print("\nbob = ", bob)
print("\nAgreed Key = ", bob.agreedKey())