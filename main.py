from tkinter import *
from tkinter import messagebox
import os
from user import User
from auth import generator, authenticator

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="white")
root.resizable(False, False) #Não permitir ajustar o tamanho da tela

EMPTY_USERNAME_FIELD = 'Nome de usuário: '
EMPTY_PASSWORD_FIELD = 'Senha: '

def signin():
    username = user.get()
    password = code.get()
    

    new_user = User(username=username, password=password)

    if new_user.username == EMPTY_USERNAME_FIELD or new_user.password == EMPTY_PASSWORD_FIELD or new_user.username == '' or new_user.password == '':
        messagebox.showerror("Erro", "Campo de usuário ou senha vazio.")
        return
    elif check_credentials(new_user.username, new_user.password) == True:
        messagebox.showinfo('Sucesso!', "Verificação de 2 etapas necessário.")
    else:
        messagebox.showerror('Erro', "Usuário inexistente")



    if new_user.username == 'admin' and  new_user.password == 'admin':
        generator()
        screen = Toplevel(root)
        screen.resizable(False, False)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')


        google_code = Entry(screen, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11))
        Button(screen, width=50, pady=14, padx=35, text='Enviar código', bg = '#57a1f8', fg='white', border=0, cursor='hand2', command=authenticator(google_code.get())).place(x = 35, y = 304)
        google_code.place(x = 40, y = 180)
        google_code.insert(0, 'Código google authenticator: ')

        def on_enter_qr(e):
            google_code.delete(0, 'end')

        def on_leave_qr(e):
            digited_code = google_code.get()
            if digited_code == '':
                google_code.insert(0, 'Código google authenticator: ')

        google_code.bind('<FocusIn>', on_enter_qr)
        google_code.bind('<FocusOut>', on_leave_qr)

        qrcode_google = PhotoImage(file='qrcode.png')
        Label(screen, image=qrcode_google, bg='white').place(x=500, y=50)
        Frame(screen, width = 410, height=2, bg='black').place(x = 37, y = 207)
        frameCode=Frame(screen, width=350, height=350, bg="transparent")
        frameCode.place(x=480, y = 70)

        ###################################################################
                
        screen.mainloop()

##########----------------------------
##########----------------------------
##########----------------------------
##########----------------------------
##########----------------------------
##########----------------------------
##########----------------------------

def check_credentials(username, password):
    try:
        with open('passwords.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(', ')
                if len(dados) == 2 and dados[0] == username:
                    return True
        return False
    except Exception as e:
        print(f'Erro ao verificar credenciais: {e}')
        return False
    


def sign_up():
    new_username = user.get()
    new_password = code.get()

    # Verifique se ambos os campos obrigatórios foram preenchidos
    #Foi colocado esses 2 campos porque é o que está escrito antes do usuário colocar o input em foco
    if new_username == EMPTY_USERNAME_FIELD or new_password == EMPTY_PASSWORD_FIELD:
        messagebox.showerror("Erro", "Digite seu login e senha para poder criar o usuário.")
        return
    elif check_credentials(new_username, new_password) == True:
        messagebox.showerror('Erro', 'O Usuário já existe!')
    else:
        new_user = User(username=new_username, password=new_password)

        try: 
            with open('passwords.txt', 'a') as arquivo:
                arquivo.write(f"{new_user.username}, {new_user.password}\n")

            messagebox.showinfo("Sucesso", 'Conta criada com sucesso!')
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar conta: {e}")
            

    

img = PhotoImage(file='imgs\login.gif')
Label(root, image=img, bg='white').place(x=50, y=50)


frame=Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y = 70)

heading=Label(frame, text='Entrar', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y = 5)

###################################################################
#NOME DE USUARIO E SENHA

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0, 'Nome do usuário')


user = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11))
user.place(x = 30, y = 80)
user.insert(0, 'Nome de usuário: ')

#Apagar 'placeholder' quando entra em foco do input
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 107)


def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name == '':
        code.insert(0, 'Senha: ')

code = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11), show='*')
code.place(x = 30, y = 150)
code.insert(0, 'Senha: ')


#Apagar 'placeholder' quando entra em foco do input
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 177)

###################################################################

Button(frame, width=39, pady=7, text='Entrar', bg = '#57a1f8', fg='white', border=0, cursor='hand2', command=signin).place(x = 35, y = 204)
label = Label(frame, text='Não tem uma conta?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x = 75, y = 270)


sign_up = Button(frame, width=8, text='Criar conta', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign_up)
sign_up.place(x = 200, y = 271)




root.mainloop()