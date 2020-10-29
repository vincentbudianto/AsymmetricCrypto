import RSA
import util.file as file

keygen = RSA.RSAKeygen(p=47, q=71, e=79)
print(keygen)
keygen.writeToFile("abjad")

# print("Hasil Enkripsi = ", RSA.encrypt([0, 1, 2, 255], 79, 3337))
# print("Hasil Dekripsi = ", RSA.decrypt([0, 0, 1, 0, 67, 12, 32, 4], 1019, 3337))

pub = file.readFromJson("abjad.pub")
pri = file.readFromJson("abjad.pri")
print(pub)
print(pri)

data = file.readFile("testMedia/demo-image.jpg")
encrypted = RSA.encrypt(data, pub['e'], pub['n'])
file.writeFile("encrypted.jpg", encrypted)

data = file.readFile("encrypted.jpg")
decrypted = RSA.decrypt(data, pri['d'], pri['n'])
file.writeFile("decrypted.jpg", decrypted)