import tkinter as tk
from ttkbootstrap import Style
import random
#write the file path according to your system

file_base_path=r""

class AdventureGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Text-Based Adventure Game")
        self.master.geometry("1900x700")
        self.style = Style(theme='darkly')

          # Replace the path with the actual path to your background image
        self.background_image = tk.PhotoImage(file=file_base_path + r"\images\puzzle.png")
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.current_room = 1
        self.player_health = 100
        self.boss_health = 100

        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.master, text="Welcome to the Mansion!", font=("Helvetica", 35))
        self.info_label.pack(pady=10)

        self.attack_buttons = []
        moves = ["Sword Slash", "Sword Thrust", "Sword Spin"]
        for move in moves:
            button = tk.Button(self.master, text=move, command=lambda m=move: self.attack(m), font=("Helvetica", 20))
            button.pack(pady=5)
            self.attack_buttons.append(button)
            self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game, font=("Helvetica", 20))
            self.restart_button.pack(pady=5)

    def attack(self, move):
         # Perform attack logic
        player_damage = random.randint(5, 15)
        boss_damage = random.randint(5, 15)

        self.boss_health -= player_damage
        self.player_health -= boss_damage

        self.update_info_label(f"Player attacked Boss with {move} for {player_damage} damage. Boss counterattacked for {boss_damage} damage.")

        if self.boss_health <= 0:
            self.update_info_label("Congratulations! You defeated the Boss. You saved your friend.")
            self.restart_button.config(state=tk.NORMAL)
            for button in self.attack_buttons:
                button.config(state=tk.DISABLED)
        elif self.player_health <= 0:
            self.update_info_label("GAME OVER! The Boss defeated you. Try again.")
            self.restart_button.config(state=tk.NORMAL)
            for button in self.attack_buttons:
                button.config(state=tk.DISABLED)
        else:
            self.update_info_label(f"Player Health: {self.player_health} | Boss Health: {self.boss_health}")

    def restart_game(self):
        self.current_room = 1
        self.player_health = 100
        self.boss_health = 100
        self.update_info_label("Welcome to the Mansion!")
        self.restart_button.config(state=tk.DISABLED)
        for button in self.attack_buttons:
            button.config(state=tk.NORMAL)

    def update_info_label(self, text):
        self.info_label.config(text=text)


def launch():
    global root
    root = tk.Toplevel()
    app = AdventureGame(root)
 



