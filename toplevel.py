from tkinter import *
from tkinter import messagebox
from auth import authenticator, generator
from app import open_diary

def open_toplevel(root):
        screen = Toplevel(root)
        screen.resizable(False, False)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        def fechar_toplevel():
            if authenticator(google_code.get()) == True:
                messagebox.showinfo('Logado', 'Autenticação feita com sucesso, bem vindo!')
                screen.destroy()
                root.destroy()
                open_diary()
            else:
                messagebox.showerror('Erro', 'Código inválido.')

        google_code = Entry(screen, width = 25, fg='black',  border = 0, bg = 'white', font=('Microsoft YaHei UI Light', 11))
        Button(screen, width=50, pady=14, padx=35, text='Enviar código', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=lambda: [authenticator(google_code.get()), fechar_toplevel()]).place(x=35, y=304)

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
