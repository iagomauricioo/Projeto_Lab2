from tkinter import *
from tkinter import messagebox
from user import User
from sql_crud import insert_data, sql_connection, create_table, update_data
from register import on_enter_focus, on_leave_focus, sign_up

EMPTY_USERNAME_FIELD = 'Nome de usuário: '
EMPTY_PASSWORD_FIELD = 'Senha: '

con = sql_connection()
cursor = con.cursor()
create_table(con)



def reset(root):
        global user
        global code
        global screen

        screen = Toplevel(root)
        screen.resizable(False, False)
        screen.title('App')
        screen.geometry('425x500+300+100')
        screen.config(bg='white')


        frame=Frame(screen, width=350, height=350, bg="white")
        frame.place(x=50, y = 70)

        heading=Label(frame, text='Alterar apelido', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=50, y = 5)

        ###################################################################
        #NOME DE USUARIO E SENHA

        nickname = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11))
        nickname.place(x = 30, y = 100)
        nickname.insert(0, 'Apelido antigo: ')
        
        new_nickname = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11))
        new_nickname.place(x = 30, y = 170)
        new_nickname.insert(0, 'Novo apelido: ')

        #Apagar 'placeholder' quando entra em foco do input
        nickname.bind('<FocusIn>', lambda e: on_enter_focus(e, nickname))
        nickname.bind('<FocusOut>', lambda e: on_leave_focus(e, nickname, "Apelido: "))
        
        new_nickname.bind('<FocusIn>', lambda e: on_enter_focus(e, new_nickname))
        new_nickname.bind('<FocusOut>', lambda e: on_leave_focus(e, new_nickname, "Novo apelido: "))

        Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 127)
        Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 197)

        code = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11), show='*')
        code.place(x = 30, y = 240)
        code.insert(0, 'Senha: ')
        


        #Apagar 'placeholder' quando entra em foco do input
        code.bind('<FocusIn>', lambda e: on_enter_focus(e, code))
        code.bind('<FocusOut>', lambda e: on_leave_focus(e, code, "Senha: "))
        


        Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 267)

        Button(frame, width=39, pady=7, text='Confirmar', bg = '#57a1f8', fg='white', border=0, cursor='hand2', command=lambda: update_data(con, new_nickname.get(), nickname.get(), code.get())).place(x = 35, y = 300)

        ###################################################################
        
        screen.mainloop()

def update_data(con, new_nickname, nickname, password):
    """Update the table with given new values"""
    try:
        cur = con.cursor()
        cur.execute("UPDATE users SET nickname = ? WHERE nickname LIKE ? AND password = ?", (new_nickname, nickname, password))
        con.commit()
        print("The record updated successfully")
        screen.destroy()
    except Exception as e:
        print(e)


