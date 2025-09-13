from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import ttkbootstrap as tb
import csv
import os
import room1 as room1
import room2 as room2
import room3 as room3
import room4 as room4

wel = tb.Window(themename = 'cyborg')
wel.geometry("1600x900")

wel.rowconfigure((0,1,2), weight = 1)
wel.columnconfigure((0,1,2,3), weight = 1, uniform="a")

#write the file path 
file_base_path=""


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.font_size = 12

        self.login_frame = tb.Frame(self.master)
        self.login_frame.place(relx=0.5, rely=0.35, anchor="center")

        self.username_label = tb.Label(self.login_frame, text='Username:', font=('Arial', self.font_size))
        self.username_label.pack()

        self.username_entry = tb.Entry(self.login_frame, font=('Arial', self.font_size))
        self.username_entry.pack(pady=5)

        self.password_label = tb.Label(self.login_frame, text='Password:', font=('Arial', self.font_size))
        self.password_label.pack(pady=5)

        self.password_entry = tb.Entry(self.login_frame, show='*', font=('Arial', self.font_size))
        self.password_entry.pack()

        self.login_button = tb.Button(self.login_frame, text='Login', command=self.login, bootstyle = 'info')
        self.login_button.pack(side="left", pady=10)

        self.register_button = tb.Button(self.login_frame, text='Register', command=self.register, bootstyle = 'info')
        self.register_button.pack(side="right", pady=10)

    def on_login_successful(self, username):
        self.login_frame.destroy()
        load_game_doors()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.check_credentials(username, password):
            self.on_login_successful(username)
        else:
            messagebox.showerror("Error", "Invalid username or password. Please try again.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.username_exists(username):
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        else:
            with open("user_data.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([username, password])
            messagebox.showinfo("Success", "Registration successful. You can now log in.")

    def username_exists(self, username):
        if os.path.exists("user_data.csv"):
            with open("user_data.csv", mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == username:
                        return True
        return False

    def check_credentials(self, username, password):
        if os.path.exists("user_data.csv"):
            with open("user_data.csv", mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == username and row[1] == password:
                        return True
        return False
    

def door1Click():
    room1.launch("N")

def door2Click():
    room2.DisplayPuzzleOne()

def door3Click():
    room3.launch()

def door4Click():
    room4.launch()          

def load_game_doors():
    global door_img
    #change the image file path according to your system
    door_img = PhotoImage(file = file_base_path + r"\images\door.png")
    door1_img_label = tb.Label(image= door_img)
    door1_img_label.grid(row = 0, column = 0)
    door2_img_label = tb.Label(image= door_img)
    door2_img_label.grid(row = 0, column = 1)
    door3_img_label = tb.Label(image= door_img)
    door3_img_label.grid(row = 0, column = 2)
    door4_img_label = tb.Label(image= door_img)
    door4_img_label.grid(row = 0, column = 3)
    door1 = tb.Button(text = "Door1" , bootstyle = 'info', command=door1Click) 
    door1.grid(row = 1, column = 0, sticky="n")
    door2 = tb.Button(text = "Door2" , bootstyle = 'info', command=door2Click)    
    door2.grid(row = 1, column = 1, sticky="n")
    door3 = tb.Button(text = "Door3" , bootstyle = 'info', command=door3Click)    
    door3.grid(row = 1, column = 2, sticky="n")
    door4 = tb.Button(text = "Door4" , bootstyle = 'info', command=door4Click)    
    door4.grid(row = 1, column = 3, sticky="n")

login_window = LoginWindow(wel)
wel.mainloop()
