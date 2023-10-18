from tkinter import *
from tkinter import messagebox
from auth import authenticator
from app import open_diary
from register import on_enter_focus, on_leave_focus

def open_toplevel(root):
        screen = Toplevel(root)
        screen.resizable(False, False)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        def close_toplevel():
            if authenticator(google_code.get()) == True:
                messagebox.showinfo('Logado', 'Autenticação feita com sucesso, bem vindo!')
                screen.destroy()
                open_diary(root)
            else:
                messagebox.showerror('Erro', 'Código inválido.')

        google_code = Entry(screen, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11))
        Button(screen, width=50, pady=14, padx=35, text='Enviar código', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=lambda: [authenticator(google_code.get()), close_toplevel()]).place(x=35, y=304)
    

        google_code.place(x = 40, y = 180)
        google_code.insert(0, 'Código google authenticator: ')

        google_code.bind('<FocusIn>', lambda e: on_enter_focus(e, google_code))
        google_code.bind('<FocusOut>', lambda e: on_leave_focus(e, google_code, "Código google authenticator: "))
        google_code.bind('<Return>', lambda e: close_toplevel())

        qrcode_google = PhotoImage(file='qrcode.png')
        Label(screen, image=qrcode_google, bg='white').place(x=500, y=50)
        Frame(screen, width = 410, height=2, bg='black').place(x = 37, y = 207)
        frameCode=Frame(screen, width=350, height=350, bg="transparent")
        frameCode.place(x=480, y = 70)

        ###################################################################
        screen.mainloop()
