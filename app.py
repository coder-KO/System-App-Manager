import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("System App Manager")
root.wm_iconbitmap("logo.ico")

global bgColor
bgColor = "#142952"
apps = []

if os.path.isfile('yourApps.txt'):
    with open('yourApps.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


#========== Functions for buttons ==========#

# Function for loading app list in UI

def loadUI():
    for app in apps:
        label = tk.Label(frame, text=app, bg="#c2d1f0")
        label.pack()

# Function for selecting applications


def selectApp():

    filename = filedialog.askopenfilename(initialdir='C:', title='Select Application',
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    for widget in frame.winfo_children():
        widget.destroy()

    apps.append(filename)
    loadUI()


# Funciton for running application


def runApp():
    for app in apps:
        os.startfile(app)

#========== ./Functions for buttons ==========#


#========== Main App Canvas ==========#
canvas = tk.Canvas(root, height=500, width=800, bg=bgColor)
canvas.pack()

#========== Center Frame ==========#
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.12)

#========== Buttons ==========#

# Button for selecting apps
selectButton = tk.Button(root, text="Select Apps", padx=10,
                         pady=5, fg="white", bg=bgColor, command=selectApp)
selectButton.pack(side=tk.RIGHT)

# Button for running apps
runButton = tk.Button(root, text="Run Apps", padx=10,
                      pady=5, fg="white", bg=bgColor, command=runApp)
runButton.pack(side=tk.RIGHT)

loadUI()

root.mainloop()

with open('yourApps.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
