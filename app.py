import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

# Functions for buttons


def selectApp():

    filename = filedialog.askopenfilename(initialdir='C:', title='Select Application',
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    for widget in frame.winfo_children():
        widget.destroy()

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()


# Main App Canvas
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

# Center Frame
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Button for selecting apps
selectButton = tk.Button(root, text="Select Apps", padx=10,
                         pady=5, fg="white", bg="#263D42", command=selectApp)
selectButton.pack()

# Button for running apps
runButton = tk.Button(root, text="Run Apps", padx=10,
                      pady=5, fg="white", bg="#263D42")
runButton.pack()


root.mainloop()
