import pyotp
import qrcode

key = pyotp.random_base32()

url = pyotp.totp.TOTP(key).provisioning_uri(name='Iago', issuer_name='Teste')

qrcode.make(url).save("qrcode.png")

totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Code: ")))

