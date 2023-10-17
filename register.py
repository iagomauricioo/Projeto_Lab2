from tkinter import *
from tkinter import messagebox
from user import User

EMPTY_USERNAME_FIELD = 'Nome de usuário: '
EMPTY_PASSWORD_FIELD = 'Senha: '



def open_register(root):
        global user
        global code

        screen = Toplevel(root)
        screen.resizable(False, False)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')


        frame=Frame(screen, width=350, height=350, bg="white")
        frame.place(x=320, y = 70)

        heading=Label(frame, text='Registrar', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y = 5)

        ###################################################################
        #NOME DE USUARIO E SENHA

        user = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11))
        user.place(x = 30, y = 100)
        user.insert(0, 'Nome de usuário: ')

        #Apagar 'placeholder' quando entra em foco do input
        user.bind('<FocusIn>', on_enter_username)
        user.bind('<FocusOut>', on_leave_username)

        Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 127)

        code = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11), show='*')
        code.place(x = 30, y = 170)
        code.insert(0, 'Senha: ')


        #Apagar 'placeholder' quando entra em foco do input
        code.bind('<FocusIn>', on_enter_password)
        code.bind('<FocusOut>', on_leave_password)
        


        Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 197)

        Button(frame, width=39, pady=7, text='Registrar', bg = '#57a1f8', fg='white', border=0, cursor='hand2', command=sign_up).place(x = 35, y = 224)

        ###################################################################

        screen.mainloop()

def on_enter_username(e):
    user.delete(0, 'end')

def on_leave_username(e):
    name=user.get()
    if name == '':
        user.insert(0, 'Nome de usuário: ')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
            
def on_enter_password(e):
    code.delete(0, 'end')

def on_leave_password(e):
    name=code.get()
    if name == '':
        code.insert(0, 'Senha: ')
    
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

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
