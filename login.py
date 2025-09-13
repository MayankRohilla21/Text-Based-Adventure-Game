"""
login.py - simple login/registration GUI for the final_project
This file provides a small, robust login window that reads/writes a CSV user_data file
located next to this script. On successful login it imports welcome and starts the app.
"""

import os
import csv
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb

BASE_DIR = os.path.dirname(__file__)
USER_CSV = os.path.join(BASE_DIR, "user_data.csv")

def ensure_user_csv():
    # Ensure the CSV exists and has a simple header if empty
    if not os.path.exists(USER_CSV):
        with open(USER_CSV, "w", newline='', encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow(["Username", "Password"])
    else:
        # If file exists but is empty, write header
        if os.path.getsize(USER_CSV) == 0:
            with open(USER_CSV, "w", newline='', encoding="utf-8") as fh:
                writer = csv.writer(fh)
                writer.writerow(["Username", "Password"])

def load_users():
    users = {}
    try:
        with open(USER_CSV, newline='', encoding="utf-8") as fh:
            reader = csv.reader(fh)
            for row in reader:
                # Skip empty rows and rows that don't have at least 2 columns
                if not row or len(row) < 2:
                    continue
                username = row[0].strip()
                password = row[1].strip()
                if username == "" or username.lower() == "username":
                    continue
                users[username] = password
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read users file: {e}")
    return users

def add_user(username, password):
    # Append a new user to the CSV
    try:
        with open(USER_CSV, "a", newline='', encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow([username, password])
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save user: {e}")
        return False

def try_login(username, password, root):
    users = load_users()
    if username in users and users[username] == password:
        messagebox.showinfo("Success", f"Welcome back, {username}!")
        root.destroy()
        # Import and launch the welcome window. Importing may create the GUI defined
        # in welcome.py; we then run its mainloop if a `wel` object exists.
        try:
            import welcome
            # If welcome defines a 'wel' window (ttkbootstrap.Window), call mainloop on it
            if hasattr(welcome, "wel"):
                welcome.wel.mainloop()
            else:
                # If welcome defines a main() function, call it
                if hasattr(welcome, "main"):
                    welcome.main()
                else:
                    messagebox.showinfo("Info", "Logged in — welcome.py does not expose a GUI object to show.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch welcome screen: {e}")
    else:
        messagebox.showerror("Login failed", "Username or password incorrect. You can register a new account.")

def register_user(username, password):
    if not username or not password:
        messagebox.showwarning("Invalid", "Username and password cannot be empty.")
        return
    users = load_users()
    if username in users:
        messagebox.showwarning("Exists", "That username already exists.")
        return
    ok = add_user(username, password)
    if ok:
        messagebox.showinfo("Registered", "Account created. You can now login.")

def build_login_window():
    ensure_user_csv()
    root = tb.Window(themename="cyborg")
    root.title("Login - Final Project")
    root.geometry("550x350")
    root.resizable(False, False)

    frm = tb.Frame(root, padding=20)
    frm.pack(expand=True, fill="both")

    title = tb.Label(frm, text="Final Project — Login", font=("Helvetica", 18, "bold"))
    title.pack(pady=(0,10))

    lbl_user = tb.Label(frm, text="Username")
    lbl_user.pack(anchor="w", pady=(6,0))
    ent_user = tb.Entry(frm)
    ent_user.pack(fill="x", pady=(0,6))

    lbl_pass = tb.Label(frm, text="Password")
    lbl_pass.pack(anchor="w", pady=(6,0))
    ent_pass = tb.Entry(frm, show="*")
    ent_pass.pack(fill="x", pady=(0,6))

    btn_frame = tb.Frame(frm)
    btn_frame.pack(pady=10, fill="x")

    def on_login():
        uname = ent_user.get().strip()
        pword = ent_pass.get().strip()
        if not uname or not pword:
            messagebox.showwarning("Missing", "Enter both username and password.")
            return
        try_login(uname, pword, root)

    def on_register():
        uname = ent_user.get().strip()
        pword = ent_pass.get().strip()
        register_user(uname, pword)

    btn_login = tb.Button(btn_frame, text="Login", command=on_login)
    btn_login.pack(side="left", expand=True, fill="x", padx=5)

    btn_register = tb.Button(btn_frame, text="Register", command=on_register)
    btn_register.pack(side="left", expand=True, fill="x", padx=5)

    # Helpful footer: show existing usernames (non-sensitive) for testing
    users = load_users()
    if users:
        footer = tb.Label(frm, text="Existing users: " + ", ".join(list(users.keys())[:8]))
        footer.pack(side="bottom", pady=(8,0))

    return root

if __name__ == "__main__":
    app = build_login_window()
    app.mainloop()
