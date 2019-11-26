import tkinter as tk

class app(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.calculatorDisplay = tk.Label(self, bg="grey", width=20, height=2)
        self.calculatorDisplay.grid(row=0, columnspan=4)
        self.createNumberWidgets()
        
    def createNumberWidgets(self):
        columnNo = 0
        rowNo = 4
        for i in range(10):
            self.number = tk.Button(self, text=str(i), width=5, height=2)
            if i == 0:
                self.number.grid(row=5, column=0)
                continue
            self.number.grid(row=rowNo, column=columnNo)
            if columnNo == 2:
                columnNo = 0
                rowNo -= 1
            else: columnNo += 1
root = tk.Tk()
app(root)
root.mainloop()