import tkinter as tk


class Welcome:
    def __init__(self, openFile, saveFile, quit) -> None:
        self.label = tk.Label(text="欢迎使用文件阅读器", font=("Arial", 24, "bold"))
        self.open_button = tk.Button(text="Open", command=openFile)
        self.menu_bar = tk.Menu()
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=openFile)
        self.file_menu.add_command(label="Save", command=saveFile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

    def pack(self, window):
        self.label.pack()
        self.open_button.pack()
        window.config(menu=self.menu_bar)
