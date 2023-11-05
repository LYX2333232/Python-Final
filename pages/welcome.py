import tkinter as tk


class Welcome:
    def __init__(self, openFile,  quit) -> None:
        self.label = tk.Label(text="欢迎使用文件阅读器", font=("Arial", 24, "bold"))
        self.open_button = tk.Button(text="Open", command=openFile)
        self.menu_bar = tk.Menu()
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="打开", command=openFile)
        # 设置为不可用
        self.file_menu.add_command(label="保存", state="disabled")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="退出", command=quit)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)

    def pack(self, window):
        self.label.pack()
        self.open_button.pack()
        window.config(menu=self.menu_bar)
