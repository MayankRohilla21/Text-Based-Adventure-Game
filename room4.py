import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from ttkbootstrap import Style
from PIL import Image, ImageTk

#write the file path according to your system
file_base_path=r""

def launch():
    root = tk.Toplevel()
    root.title("Room 4")
    root.geometry("2000x1300")

    # Create a Style object from ttkbootstrap
    style = Style(theme="darkly")

    

    # Load and resize the background image
    background_image = Image.open(file_base_path + r"\images\bg.jpg")  # Replace with your image file
    background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a Canvas widget for the background
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)
    canvas.pack()

    # Create a Label widget to display the message
    message_label = ttk.Label(root, text="Thank you so much ******** for saving my life,you are always my true friend and I owe it to you for the rest of my life.", font=("Times New Roman", 18), background='#999999', foreground='black')
    message_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    # Set the background image as a window attribute to prevent garbage collection
    root.background_photo = background_photo




