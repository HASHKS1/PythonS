from tkinter import *
from random import choice
import string

class PasswdGenerator:

    # Class constructor 

    def __init__(self):
        self.window = Tk()
        self.window.title('App Pass Generator')
        self.window.iconbitmap('logo.ico')
        self.window.iconphoto(True, PhotoImage(file='logo.png'))
        self.window.geometry('500x255')
        self.window.config(bg='black')

        #component creation
        self.label()
        self.entry()
        self.passwd_button()
    
    def label(self):
        label_title = Label(self.window, text='Welcome to password generator', font=('Verdana', 20), bg='black', fg='white')
        label_title.pack() 


    def entry(self):
        self.password_entry = Entry(self.window, font=('Verdana', 25), bg='black', fg='white', width=30, relief='solid')
        self.password_entry.pack(pady=50)

    def passwd_button(self):
        password_generator = Button(self.window, text="Generate_password",  font=('Verdana', 12), bg='white', fg='black', width=15, command=self.generate_password)
        password_generator.pack()


    def generate_password(self):
        characters = string.ascii_letters + string.punctuation + string.digits
        password = ""
        for x in range(28):
            password+=choice(characters)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

if __name__ == "__main__":  

    #display
    dislay = PasswdGenerator()
    dislay.window.mainloop()