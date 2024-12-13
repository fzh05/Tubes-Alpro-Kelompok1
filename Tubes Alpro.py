#Tubes Alpro

import tkinter as tk
from tkinter import messagebox

def login():
  username = username_entry.get()
  password = password_entry.get()

  # Replace with actual authentication logic
  if username == "user" and password == "akuData":
    messagebox.showinfo("Login Success", "Welcome!")
    # Navigate to the main GUI or close the login window
  else:
    messagebox.showerror("Login Error", "Invalid username or password")

# Create the main window
window = tk.Tk()
window.title("Login")

# Username label and entry
username_label = tk.Label(window, text="Username")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Password label and entry
password_label = tk.Label(window, text="Password")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Login button
login_button = tk.Button(window, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()