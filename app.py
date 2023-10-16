from tkinter import Tk, Text, Button, Toplevel, Label
import os
import datetime
from cryptography.fernet import Fernet
from decrypt import decrypt_and_display, decrypt_text
import pyperclip

# Função para gerar a chave criptográfica
def generate_key():
    return Fernet.generate_key().decode('utf-8')  # Converte a chave para string

# Função para criptografar o texto
def encrypt_text(text, key):
    cipher_suite = Fernet(key.encode('utf-8'))  # Converte a chave de string para bytes
    encrypted_text = cipher_suite.encrypt(text.encode('utf-8'))
    return encrypted_text

# Função para descriptografar o texto


def create_directory():
    current_date = datetime.date.today()
    directory_name = current_date.strftime('%Y-%m-%d')
    escritos_directory = "escritos"

    if not os.path.exists(escritos_directory):
        os.mkdir(escritos_directory)

    directory_path = os.path.join(escritos_directory, directory_name)

    if not os.path.exists(directory_path):
        os.mkdir(directory_path)

    return directory_path

def save_entry():
    current_date_time = datetime.datetime.now()
    file_name = current_date_time.strftime('%Y-%m-%d %H-%M-%S')
    entry = text_entry.get('1.0', 'end-1c')
    key = generate_key()
    encrypted_entry = encrypt_text(entry, key)
    
    def toplevel_key():
        screen = Toplevel(root)
        screen.title('Chave de descriptografia')
        screen.resizable(False, False)
        screen.geometry('425x400+200+100')
        screen.configure(bg='lightgray')
        Label(screen, text='Salve sua chave de\nde descriptografia em um local seguro.', fg='white', bg='red', font=('Microsoft YaHei UI Light', 15)).place(x = 35, y = 20)

        Button(screen, width=39, pady=7, text='Copiar chave', bg = 'red', fg='white', border=0, cursor='hand2', command=lambda: root.clipboard_append(key)).place(x = 70, y = 204)
    directory_path = create_directory()
    file_path = os.path.join(directory_path, file_name + '.txt')

    with open(file_path, 'wb') as file:
        file.write(encrypted_entry)

    toplevel_key()


root = Tk()
root.title('Diary')
root.resizable(False, False)
root.geometry('425x400+200+100')

text_entry = Text(root, height=18, width=50, border=0, bg="lightBlue")
text_entry.pack()

save_button = Button(root, text='Salvar', command=save_entry, bg='#57a1f8', fg='white', border=0, width=50).place(x=35, y=330)

quit_button = Button(root, text='Sair', command=root.quit, bg='#57a1f8', fg='white', border=0, width=50).place(x=35, y=360)

decrypt_button = Button(root, text='Mostrar mensagens', command=decrypt_and_display(root, key), bg='#57a1f8', fg='white', border=0, width=50).place(x=35, y=300)

create_directory()

root.mainloop()
