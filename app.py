from tkinter import *
from tkinter import messagebox


def open_diary():
    root = Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="white")
    root.resizable(False, False) #Não permitir ajustar o tamanho da tela