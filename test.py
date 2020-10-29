s = "abc"
b = s.encode()
b = bytearray(b)
b = list(b)
print(b)
c = bytearray(b)
c = c.decode("ascii")
print(c)