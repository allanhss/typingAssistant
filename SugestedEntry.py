from tkinter import *


class SugestedEntry:
    def __init__(self, root, optionsList):
        self.list = optionsList
        self.entry = Entry(root, bd=2)
        self.entry.pack()
        self.entry.focus_force()
        self.entry.bind("<KeyRelease-Up>", self.listNavigate)
        self.entry.bind("<KeyRelease-Down>", self.listNavigate)
        self.entry.bind("<Right>", self.selectSelection)
        self.entry.bind("<<ListBoxSelect>>", self.selectActive)
        self.entry.bind("<KeyRelease>", self.checkEntry)

        self.optionsList = Listbox(
            root,
            height=3,
            yscrollcommand="True",
            bd=1,
            background="Grey",
            fg="White",
        )
        self.optionsList.pack(pady=5)
        self.optionsList.yview()
        self.update_optionsList(self.list)
        self.selected_value = None

    def update_optionsList(self, data):
        self.optionsList.delete(0, END)
        for item in data:
            self.optionsList.insert(END, item)
        self.optionsList.configure(height=len(data) if len(data) < 3 else 3)

    def checkEntry(self, event):
        input = self.entry.get()
        if input == "":
            data = self.list
        else:
            data = []
            for item in self.list:
                if input.lower() in item.lower():
                    data.append(item)
        self.update_optionsList(data)

    def listNavigate(self, event):
        key_pressed = event.keysym
        current_selection = self.optionsList.curselection()
        if current_selection:
            if key_pressed == "Up" and current_selection[0] > 0:
                next_selection = current_selection[0] - 1
            else:
                next_selection = current_selection[0] + 1
        else:
            next_selection = 0
        self.optionsList.selection_clear(0, END)
        self.optionsList.selection_set(next_selection)
        self.optionsList.see(next_selection)

    def selectActive(self, event):
        if self.optionsList.curselection():
            self.entry.delete(0, END)
            self.entry.insert(0, self.optionsList.get(ACTIVE))

    def selectSelection(self, event):
        current_selection = self.optionsList.curselection()
        if current_selection:
            self.entry.delete(0, END)
            selected = self.optionsList.get(current_selection)
            self.entry.insert(0, selected)

    def getSelectedValue(self):
        current_selection = self.optionsList.curselection()
        if current_selection:
            self.entry.delete(0, END)
            selected = self.optionsList.get(current_selection)
            self.entry.insert(0, selected)
        return self.entry.get()


if __name__ == "__main__":

    def rootOnReturn(event):
        print(entry.getSelectedValue())
        root.destroy()

    root = Tk()
    root.overrideredirect(1)  # Remove a borda da janela

    fakeList = [
        "Brasil",
        "Argentina",
        "Canadá",
        "França",
        "Alemanha",
        "Índia",
        "Japão",
        "Austrália",
        "China",
        "Rússia",
    ]
    entry = SugestedEntry(root=root, optionsList=fakeList)

    root.bind("<Return>", rootOnReturn)
    root.bind("<FocusOut>", lambda x: root.destroy())
    root.bind("<Escape>", lambda x: root.destroy())

    root.mainloop()
