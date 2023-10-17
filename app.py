from tkinter import Toplevel, Text, Button

import os
import datetime

def open_diary(root):

    screen = Toplevel(root)
    screen.title('Diary')
    screen.resizable(False, False)
    screen.geometry('425x400+200+100')

    text_entry = Text(screen, height=18, width=50, border=0, bg="lightBlue")
    text_entry.pack()


    save_button = Button(screen, text='Salvar', command=lambda: save_entry(screen, text_entry), bg='#57a1f8', fg='white', border=0, width=50)
    save_button.place(x=35, y=330)

    quit_button = Button(screen, text='Sair', command=screen.quit, bg='#57a1f8', fg='white', border=0, width=50)
    quit_button.place(x=35, y=360)

    screen.mainloop()
    

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

def save_entry(screen, text_entry):
    current_date_time = datetime.datetime.now()
    file_name = current_date_time.strftime('%Y-%m-%d %H-%M-%S')
    entry = text_entry.get('1.0', 'end-1c')
    directory_path = create_directory()
    file_path = os.path.join(directory_path, file_name + '.txt')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(entry)
