import tkinter as tk

class MirrorMaker(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.buttons = []

        white = True
        for i in range(15):
            for j in range(15):
                button = tk.Label(self, bg='white' if white else 'gray', width=10, height=10)
                button.grid(column = i, row = j)
                white = not white


MirrorMaker().mainloop()
