from tkinter import *
from tkinter import messagebox
from user import User
from sql_crud import insert_data, sql_connection, create_table

EMPTY_USERNAME_FIELD = 'Nome de usuário: '
EMPTY_PASSWORD_FIELD = 'Senha: '

con = sql_connection()
cursor = con.cursor()
create_table(con)


def open_register(root):
        global user
        global code
        global nickname
        global screen

        screen = Toplevel(root)
        screen.resizable(False, False)
        screen.title('App')
        screen.geometry('425x500+300+100')
        screen.config(bg='white')


        frame=Frame(screen, width=350, height=350, bg="white")
        frame.place(x=50, y = 70)

        heading=Label(frame, text='Registrar', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y = 5)

        ###################################################################
        #NOME DE USUARIO E SENHA

        user = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11))
        user.place(x = 30, y = 100)
        user.insert(0, 'Nome de usuário: ')

        #Apagar 'placeholder' quando entra em foco do input
        user.bind('<FocusIn>', lambda e: on_enter_focus(e, user))
        user.bind('<FocusOut>', lambda e: on_leave_focus(e, user, "Nome de usuário: "))

        Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 127)
        
        nickname = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11))
        nickname.place(x = 30, y = 170)
        nickname.insert(0, 'Apelido: ')

        nickname.bind('<FocusIn>', lambda e: on_enter_focus(e, nickname))
        nickname.bind('<FocusOut>', lambda e: on_leave_focus(e, nickname, "Apelido: "))


        code = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11), show='*')
        code.place(x = 30, y = 240)
        code.insert(0, 'Senha: ')


        #Apagar 'placeholder' quando entra em foco do input
        code.bind('<FocusIn>', lambda e: on_enter_focus(e, code))
        code.bind('<FocusOut>', lambda e: on_leave_focus(e, code, "Senha: "))
        


        Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 197)
        Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 260)

        Button(frame, width=39, pady=7, text='Registrar', bg = '#57a1f8', fg='white', border=0, cursor='hand2', command=sign_up).place(x = 35, y = 300)

        ###################################################################

        screen.mainloop()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def on_enter_focus(e, entry):
    entry.delete(0, 'end')

def on_leave_focus(e, entry, placeholder):
    name=entry.get()
    if name == '':
        entry.insert(0, placeholder)
    
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def sign_up():
    new_username = user.get()
    new_password = code.get()
    new_nickname = nickname.get()
    new_user = User(username=new_username, nickname=new_nickname, password=new_password)

    if new_username == EMPTY_USERNAME_FIELD or new_password == EMPTY_PASSWORD_FIELD:
        messagebox.showerror("Erro", "Digite seu login e senha para poder criar o usuário.")
        return
    else:
        try: 
            entities = (new_user.username, new_user.nickname, new_user.password)
            insert_data(con, entities)

            screen.destroy()
            messagebox.showinfo("Sucesso", 'Conta criada com sucesso!')

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar conta: {e}")


