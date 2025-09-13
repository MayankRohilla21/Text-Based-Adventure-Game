from tkinter import *
from PIL import ImageTk, Image
import ttkbootstrap as tb
import os
import pygame


#write the file path according to your system

file_base_path=r""
 
def launch(my_egg):
    global root
    root = tb.Toplevel()
    style = tb.Style(theme="cyborg")
    root.geometry("1600x900")

    root.rowconfigure((0,1,2), weight = 1)
    root.columnconfigure((0,1,2,3), weight = 1)
    global egg
    egg = my_egg
    if egg == "N":
        eggNo()
    else:
        eggYes()
       


def eggNo():
    global main_label
    global inicont
    main_label = tb.Label(root, text = "It's Vary Dark in Here. Maybe there's a switch for Light?", font = "Helvetica, 40", bootstyle = "light")
    inicont = tb.Button(root, text = "Click this img" , bootstyle = 'warning', command = lightroom)  
    main_label.grid(row = 1, column = 1, columnspan=3)
    inicont.grid(row = 2, column = 3)

counterp = 0
def lightroom():
    main_label.destroy()
    inicont.destroy()
    tohiro()

def eggYes():
    main_labelY = tb.Label(root, text = "I have got the egg. Give me the key", font = "Helvetica, 40", bootstyle = "light")
    main_labelY.grid(row = 1, column = 1, columnspan=3)

pygame.mixer.init()
def play():
    pygame.mixer.music.load(file_base_path + r"\images\ShiroganeFinal.mp3")
    pygame.mixer.music.play(loops=2)


def npcproceed():
    if counterp % 2 == 0:
        Tohirolabel.config(text = "Perhaps your little friend would be of more importance to \nyou than my very existence.", font = 'Helvetica, 38', bootstyle = 'info', justify='center' )
        ask_button1.config(text = "Where is Alex?", command = npcproceed2)

def npcproceed2():
    if counterp % 2 == 0:
        Tohirolabel.config(text = "Now that's a question I can help in answering, that's why \n you are here afterall, right", font = 'Helvetica, 38', bootstyle = 'info', justify='center')
        ask_button1.config(text = "...", command = continuer)

def continuer():
    if counterp % 2 == 0:
        Tohirolabel.config(text = "But you may have heard the saying, everything that's \nworthwile has it's price my friend.", font = 'Helvetica, 38', bootstyle = 'info', justify='center')
        ask_button1.config(text = "What do you want?", command = npcproceed3)

def npcproceed3():
    if counterp % 2 == 0:
        Tohirolabel.config(text = "Somewhere around this big Mansion, lies a golden egg, I \n want you to bring it back to me", font = 'Helvetica, 38', bootstyle = 'info', justify='center')
        ask_button1.config(text = "But..", command = continuer2 )

def continuer2():
    if counterp % 2 == 0:
        Tohirolabel.config(text = "You want to see your friend alive right? No Questions, Bring \n me the egg, then we'll talk", font = 'Helvetica, 38', bootstyle = 'info', justify='center')
        ask_button1.config(text = "Alright, I will get you the egg", command = waiting_dialogue)
        altask_button.config(text = "No, I will NOT get the egg")

def gamequitter():
    if counterp % 2 ==0:
        Tohirolabel.config(text = "So you have chosen not to save your friend, \n Have it your way!", font = 'Helvetica, 46', bootstyle = 'danger', justify='center')
        ask_button1.config(text = '...')
    altask_button.destroy()

def waiting_dialogue():
    if counterp % 2 == 0:
        Tohirolabel.config(text = "Very well, when you find the egg, I will be waiting for \nyou here.", font = 'Helvetica, 38', bootstyle = 'info', justify='center')

def tohiro():
    global bgimg
    global img
    global jumpscare_label
    global dot_button
    global panel
    bgimg = PhotoImage(file = file_base_path + r"\images\darkroom2.png")
    bglabel = tb.Label(root, image= bgimg)
    #bglabel.place(x = 0, y = 0)
    bglabel.grid(row = 0, column = 0, rowspan = 3, columnspan= 4)

    img = ImageTk.PhotoImage(file=file_base_path + r"\images\TohiroTbig.png")
    panel = tb.Label(root, image = img)
    panel.grid(row = 1, column = 1, columnspan=2)

    jumpscare_label = tb.Label(root, text = "Bwah Ha Ha !!", bootstyle = 'info', font = 'Helvetica, 48' )
    jumpscare_label.grid(row = 2, column = 1, columnspan = 2, sticky = 'n')

    dot_button = tb.Button(root, text = "...", bootstyle = 'secondary', command = second_scene )
    dot_button.grid(row =0 , column = 1, columnspan= 2, sticky = 's')
    music_button = tb.Button(root, text = "Music", bootstyle = 'success', command = play)
    music_button.grid(row = 0, column = 3, sticky = 'w')

def second_scene():
    global Tohirolabel
    global ask_button1
    global altask_button
    if counterp % 2 == 0:
        Tohirolabel = tb.Label(root, text = "Ha Ha Ha! You Seem to be one of those people looking for  \n  more people in this mansion", font = 'Helvetica, 38', bootstyle = 'info', justify='center')
        Tohirolabel.grid(row = 1, column = 0, columnspan = 3)
        ask_button1 = tb.Button(root, text = "Who are You??", bootstyle = 'default',command = npcproceed)
        ask_button1.grid(row = 2, column = 1, sticky = 'n')
        altask_button = tb.Button(root, text = 'Leave Me Alone', bootstyle = 'danger', command = gamequitter)
        altask_button.grid(row = 2, column = 2, sticky = 'n')
    jumpscare_label.destroy()
    dot_button.destroy()
    panel.grid(row = 0, column = 3, rowspan = 3)




