from tkinter import *
from sql_crud import sql_connection, create_table, select_all

con = sql_connection()
cursor = con.cursor()
create_table(con)

def read(root):
    global user
    global code
    global screen

    screen = Toplevel(root)
    screen.resizable(False, False)
    screen.title('App')
    screen.geometry('425x500+300+100')
    screen.config(bg='white')

    frame = Frame(screen, width=350, height=350, bg="white")
    frame.place(x=50, y=70)

    heading = Label(frame, text='Usuários', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)   

    # Lista de usuários
    users_list = select_all(con)

    # Criar o widget de lista
    users_listbox = Listbox(frame, width=35, height=10, font=('Arial', 12))
    
    # Adicionar usuários à lista
    for user in users_list:
        users_listbox.insert('end', user[0])  # user[0] porque select_all retorna uma lista de tuplas
    
    users_listbox.place(x=0, y=50) 

    screen.mainloop()


def select_all(con):
    print("\n")
    try:
        cur = con.cursor()
        cur.execute('SELECT nickname FROM users')
        rows = cur.fetchall()
        return rows
    except Exception as e:
        print(e)


