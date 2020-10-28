import RSA

keygen = RSA.RSAKeygen(p=47, q=71, e=79)
print(keygen)
keygen.writeToFile("abjad")

print("Hasil Enkripsi = ", RSA.encrypt([0, 1, 2, 255], 79, 3337))
print("Hasil Dekripsi = ", RSA.decrypt([0, 0, 1, 0, 67, 12, 32, 4], 1019, 3337))