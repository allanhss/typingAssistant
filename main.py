from tkinter import *
import pyautogui
import time
from sugested_entry import SugestedEntry
import functions_base


def rootSetClipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    time.sleep(0.5)
    root.update()
    time.sleep(0.5)
    print("done")


def rootOnReturn(event):
    command = entry.getSelectedValue()
    print(f"command -> {command}")
    ## Executa o código ##
    if clipboard_text != None:
        dataOut = functionsDict[command](clipboard_text)
    else:
        dataOut = functionsDict[command]()
    ## Atualiza o Clipboard ##
    rootSetClipboard(f"{dataOut}")
    print(f"dataOut -> {dataOut}")
    root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.overrideredirect(1)  # Remove a borda da janela
    mouse_x, mouse_y = pyautogui.position()
    root.geometry(f"+{mouse_x+10}+{mouse_y+10}")

    ##
    functionsDict = {}
    for clsName in functions_base.classes:
        functionsDict.update(clsName.getFunctionsDict())
    functionsList = functionsDict.keys()
    ##
    entry = SugestedEntry(root=root, optionsList=functionsList)
    try:
        clipboard_text = root.clipboard_get()  # Pega o valor salvo no clipboard
    except:
        clipboard_text = None

    # Root Finish
    root.bind("<Return>", rootOnReturn)
    root.bind("<FocusOut>", lambda x: root.destroy())
    root.bind("<Escape>", lambda x: root.destroy())

    root.mainloop()
