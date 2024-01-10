from tkinter import *
import pyautogui
from SugestedEntry import SugestedEntry
from functions import Text


def rootOnReturn(event):
    command = entry.getSelectedValue()
    print(f"command -> {command}")
    ## Executa o código ##
    if clipboard_text != None:
        dataOut = "[]"
        dataOut = functionsDict[command](clipboard_text)
    else:
        dataOut = functionsDict[command]()
    ## Atualiza o Clipboard ##
    rootSetClipboard(dataOut)
    print(f"dataOut -> {dataOut}")


def rootSetClipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)


if __name__ == "__main__":
    root = Tk()
    root.overrideredirect(1)  # Remove a borda da janela
    mouse_x, mouse_y = pyautogui.position()
    root.geometry(f"+{mouse_x+10}+{mouse_y+10}")

    ##
    functionsDict = Text.getFunctionsDict()
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
