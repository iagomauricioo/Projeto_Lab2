from tkinter import *
from tkinter import messagebox
from user import User
from sql_crud import insert_data, sql_connection, create_table, update_data
from register import on_enter_focus, on_leave_focus, sign_up

con = sql_connection()
cursor = con.cursor()
create_table(con)

def delete(root):
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

        heading=Label(frame, text='Deletar conta', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=50, y = 5)

        ###################################################################
        #NOME DE USUARIO E SENHA

        nickname = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11))
        nickname.place(x = 30, y = 100)
        nickname.insert(0, 'Apelido: ')
        

        #Apagar 'placeholder' quando entra em foco do input
        nickname.bind('<FocusIn>', lambda e: on_enter_focus(e, nickname))
        nickname.bind('<FocusOut>', lambda e: on_leave_focus(e, nickname, "Apelido: "))
    

        Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 127)

        code = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11), show='*')
        code.place(x = 30, y = 170)
        code.insert(0, 'Senha: ')
        


        #Apagar 'placeholder' quando entra em foco do input
        code.bind('<FocusIn>', lambda e: on_enter_focus(e, code))
        code.bind('<FocusOut>', lambda e: on_leave_focus(e, code, "Senha: "))
        


        Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 197)

        Button(frame, width=39, pady=7, text='Confirmar', bg = '#57a1f8', fg='white', border=0, cursor='hand2', command=lambda: delete_record(con, nickname.get(), code.get())).place(x = 35, y = 230)

        ###################################################################
        
        screen.mainloop()

def delete_record(con, nickname, code):
    query = "DELETE FROM users WHERE nickname LIKE ? AND password LIKE ?;"
    try:
        cur = con.cursor()
        cur.execute(query, (nickname, code))
        con.commit()
        screen.destroy()
    except Exception as e:
        print(e)


