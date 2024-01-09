from tkinter import *
import pyautogui


def rootOnReturn(event):
    command = entry.get()
    root.destroy()
    print(command)


root = Tk()
root.overrideredirect(1)  # Remove a borda da janela
mouse_x, mouse_y = pyautogui.position()
root.geometry(f"+{mouse_x+10}+{mouse_y+10}")
entry = Entry(root)
entry.pack()
entry.focus_force()
root.bind("<Return>", rootOnReturn)
root.bind("<FocusOut>", lambda x: root.destroy())
root.bind("<Escape>", lambda x: root.destroy())

root.mainloop()
