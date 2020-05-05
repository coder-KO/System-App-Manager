import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

#========== Functions for buttons ==========#

# Function for selecting applications


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

# Funciton for running application


def runApp():
    for app in apps:
        os.startfile(app)

#========== ./Functions for buttons ==========#


#========== Main App Canvas ==========#
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

#========== Center Frame ==========#
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#========== Buttons ==========#

# Button for selecting apps
selectButton = tk.Button(root, text="Select Apps", padx=10,
                         pady=5, fg="white", bg="#263D42", command=selectApp)
selectButton.pack()

# Button for running apps
runButton = tk.Button(root, text="Run Apps", padx=10,
                      pady=5, fg="white", bg="#263D42", command=runApp)
runButton.pack()


root.mainloop()

with open('yourApps.txt', 'w') as f:
    for app in apps:
        f.write(app + '\n')
