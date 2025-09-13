import random
from tkinter import messagebox
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageFilter

jumbled_words_retry = False
riddle_retry = False
#write the file path according to your system
file_base_path=""

def JumbledWord(word):
    if word.lower() == "virtuous":
        messagebox.showinfo("CONGRATULATIONS!", "You have proven your worth! The 'MegaBlade' is now YOURS!")
        root.destroy()
        DisplayPuzzleTwo()
    else:
        global jumbled_words_retry
        if not jumbled_words_retry:
            answer = messagebox.askretrycancel("OOPS!", "Alas! You failed!")
            if answer == 1:
                jumbled_words_retry = True
                return
        else:
            messagebox.showinfo("OOPS!", "YOU FAILED!")
            root.destroy()


def Riddle(word, newroot):
    if word.lower() == "sword":
        messagebox.showinfo("CONGRATULATIONS!", "You have received the 'CB Egg'! You may proceed back to your friend. ")
        newroot.destroy()

    else:
        global riddle_retry
        if not riddle_retry:
            answer = messagebox.askretrycancel("OOPS!", "Alas! You failed!")
            if answer == 1:
                riddle_retry = True
                return
        else:
            messagebox.showinfo("OOPS!", "YOU FAILED!")
            newroot.destroy()


def get_resized_image(filename, width, height):
    img = Image.open(filename).resize((width, height), Image.LANCZOS)
    blurimg = img.filter(ImageFilter.BLUR)
    return ImageTk.PhotoImage(blurimg)

class ResizableCanvas(Canvas):
    def __init__(self, parent, *args, **kwargs):
        Canvas.__init__(self, parent, *args, **kwargs)
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.config(width=event.width, height=event.height)
        self.image = get_resized_image(file_base_path + r'\images\bg.jpg', event.width, event.height)
        self.create_image(event.width // 2, event.height // 2, image=self.image)

def DisplayPuzzleOne():
    global root
    root = tb.Toplevel(title="TEXT BASED ADVENTURE GAME")
    root.geometry("2000x1300")
    canvas = ResizableCanvas(root, bg='#999999', highlightthickness=0)
    canvas.pack(fill=BOTH, expand=YES)

    width, height = root.winfo_width(), root.winfo_height()
    canvas.image = get_resized_image(file_base_path + r'\images\bg.jpg', width, height)
    canvas.create_image(width // 2, height // 2, image=canvas.image)

    mainlabel = tb.Label(canvas, text="A Spectral Presence Materializes before you, \nholding the legendary weapon "
                                      "'MageBlade'.\nTo claim this weapon, you must prove your \nvalor. Be "
                                      "prepared to face the trial!", font=("Times New Roman", 25, "bold", "italic"),
                         background='#999999', foreground='black')
    mainlabel.pack(pady=20)

    jumbled_puzzle_word = "virtuous"
    shuffled = ','.join(random.sample(jumbled_puzzle_word, len(jumbled_puzzle_word)))
    letterslabel = tb.Label(canvas, text="Enter the word formed using these letters - \n " + shuffled,
                            font=("Times New Roman", 20, "bold", "italic"),
                            background='#999999', foreground='black')
    letterslabel.pack(pady=20)

    jumbled_puzzle_word_input = Entry(canvas, width=15, font=('Georgia 20'))
    jumbled_puzzle_word_input.pack(pady=20)
    jumbled_puzzle_word_input.focus()

    Button(canvas, text="Submit", font="Times 20", bg='#eeeeee', borderwidth='1',
           command=lambda: JumbledWord(jumbled_puzzle_word_input.get())).pack(pady=20)

def DisplayPuzzleTwo():
    newroot = tb.Toplevel(title="TEXT BASED ADVENTURE GAME")
    newroot.geometry("2000x1300")

    canvas = ResizableCanvas(newroot, bg='#eeeeee', highlightthickness=0)
    canvas.pack(fill=BOTH, expand=YES)

    width, height = newroot.winfo_width(), newroot.winfo_height()
    canvas.image = get_resized_image(file_base_path + r'\images\bg.jpg', width, height)
    canvas.create_image(width // 2, height // 2, image=canvas.image)

    mainlabel = tb.Label(canvas, text="Forged in echoes of battles untold,\nA relic of ages, its tale to "
                                      "unfold.\nTempered in the fires of battles fought,\nA silent warrior in shadows "
                                      "sought.\nAdorned with runes of power and might,\nIt gleams in the moon's "
                                      "ethereal light.\nIn hands of heroes, its legacy prevails,\nWhat am I, "
                                      "as ancient history trails?", font=("Times New Roman", 20, "bold", "italic"),
                         background='#eeeeee', foreground='black')
    mainlabel.pack(pady=20)

    riddlelabel = tb.Label(canvas, text="What am I, from an era long past,\n A guardian's weapon, steadfast?",
                           font=("Times New Roman", 18, "bold", "italic"),
                           background='#eeeeee', foreground='black')
    riddlelabel.pack(pady=20)

    riddle_word_input = Entry(canvas, width=15, font=('Georgia 20'))
    riddle_word_input.pack(pady=20)
    riddle_word_input.focus()

    Button(canvas, text="Submit", font="Times 18", bg='#eeeeee', borderwidth='1',
           command=lambda: Riddle(riddle_word_input.get(), newroot)).pack(pady=20)


#DisplayPuzzleOne()
#root.mainloop()

