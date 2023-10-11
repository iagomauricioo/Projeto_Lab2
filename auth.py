import os
import pyotp
import qrcode

def generator():
    # Nome do arquivo QR Code
    qrcode_filename = "qrcode.png"

    # Verifica se o arquivo já existe e exclui se necessário
    if os.path.exists(qrcode_filename):
        os.remove(qrcode_filename)

    # Gera uma nova chave
    key = pyotp.random_base32()

    # Gera a URL para o TOTP
    url = pyotp.totp.TOTP(key).provisioning_uri(name='Login admin')

    # Cria e salva o QR Code
    qrcode.make(url).save(qrcode_filename)
    # Inicializa o TOTP com a chave
    global totp
    totp = pyotp.TOTP(key)


def authenticator(code):
    # Loop para verificação contínua
        if totp.verify(code):
             print('True')
             return True
        else:
             print('False')
             return 1