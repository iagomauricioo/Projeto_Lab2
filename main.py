from tkinter import *
from tkinter import messagebox
import os
from user import User
from auth import generator
from toplevel import open_toplevel
from register import open_register, on_enter_focus, on_leave_focus
from sql_crud import sql_connection
from nickname_reset import reset
from delete_user import delete
from read import read

EMPTY_USERNAME_FIELD = 'Nome de usuário: '
EMPTY_PASSWORD_FIELD = 'Senha: '

con = sql_connection()
cursor = con.cursor()

def main():

    root = Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="white")
    root.resizable(False, False) #Não permitir ajustar o tamanho da tela

    global user
    global code
    
    img = PhotoImage(file='Projeto_Lab2\imgs\login.gif')

    Label(root, image=img, bg='white').place(x=50, y=50)


    frame=Frame(root, width=350, height=400, bg="white")
    frame.place(x=480, y = 70)

    heading=Label(frame, text='Entrar', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y = 5)

    ###################################################################
    #NOME DE USUARIO E SENHA

    user = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11))
    user.place(x = 30, y = 80)
    user.insert(0, 'Nome de usuário: ')

    #Apagar 'placeholder' quando entra em foco do input
    user.bind('<FocusIn>', lambda e: on_enter_focus(e, user))
    user.bind('<FocusOut>', lambda e: on_leave_focus(e, user, "Nome de usuário: "))

    Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 107)

    code = Entry(frame, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11), show='*')
    code.place(x = 30, y = 150)
    code.insert(0, 'Senha: ')
    


    #Apagar 'placeholder' quando entra em foco do input
    code.bind('<FocusIn>', lambda e: on_enter_focus(e, code))
    code.bind('<FocusOut>', lambda e: on_leave_focus(e, code, "Senha: "))
    


    Frame(frame, width = 295, height=2, bg='black').place(x = 25, y = 177)

    ###################################################################

    Button(frame, width=39, pady=7, text='Entrar', bg = '#57a1f8', fg='white', border=0, cursor='hand2', command=lambda: sign_in(root)).place(x = 35, y = 204)
    
    label = Label(frame, text='Não tem uma conta?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).place(x = 75, y = 270)


    Button(frame, width=8, text='Criar conta', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda: open_register(root)).place(x = 200, y = 271)
    
    Button(frame, width=15, text='Alterar apelido', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda: reset(root)).place(x = 116, y = 300)
    
    Button(frame, width=15, text='Deletar conta', border=0, bg='white', cursor='hand2', fg='darkRed', command=lambda: delete(root)).place(x = 116, y = 330)

    Button(frame, width=15, text='Ver usuários', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda: read(root)).place(x = 116, y = 360)

    root.mainloop()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def sign_in(root):
    username = user.get()
    password = code.get()

    query = "SELECT * FROM users WHERE name=? AND password=?"
    cursor.execute(query, (username, password))
    user_data = cursor.fetchone()
    
    if not user_data:
        messagebox.showerror('Erro', 'Usuário inexistente ou senha incorreta.')
    else:
        generator()
        open_toplevel(root)
        
    
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

if __name__ == "__main__":
    main()
