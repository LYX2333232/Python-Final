import tkinter as tk
from FILE.saveFile import save, saveAs
from FILE.openFile import openFile
import csv
# import time


class CsvReader:
    def __init__(self, path, name, quit):
        self.path = path
        self.name = name
        self.suffix = 'csv'
        self.quit = quit
        self.data = [[tk.StringVar() for i in range(50)] for j in range(50)]
        # 创建类似于excel的可编辑的表格
        self.table = tk.Frame()
        self.readCsv()
        self.createMenu()
        self.createButton()
        frame = tk.Frame(self.table)
        frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(frame)
        # 为画布添加横向滚动条
        hbar = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
        hbar.pack(side="bottom", fill="x")
        canvas.configure(xscrollcommand=hbar.set)

        # 为画布添加纵向滚动条
        vbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        vbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=vbar.set)

        canvas.pack(side="left", fill="both", expand=True)

        scrollable_frame = tk.Frame(canvas)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # 设置50行50列的文本框
        for i in range(50):
            for j in range(50):
                # 创建文本框
                entry = tk.Entry(scrollable_frame,
                                 textvariable=self.data[i][j], width=10)
                entry.grid(row=i, column=j)

        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def readCsv(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            data = [row for row in reader]
            # print(data)
            for i in range(len(data)):
                for j in range(len(data[i])):
                    self.data[i][j].set(data[i][j])

    def createMenu(self):
        self.menu_bar = tk.Menu()
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="打开", command=openFile)
        self.file_menu.add_command(label="保存", command=self.save)
        self.file_menu.add_command(label="另存为", command=self.saveAs)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="退出", command=quit)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)

    def createButton(self):
        self.buttonFrame = tk.Frame()
        self.buttonFrame.pack(side='top', fill='x')
        self.saveButton = tk.Button(
            master=self.buttonFrame, text='保存', command=self.save)
        self.saveAsButton = tk.Button(
            master=self.buttonFrame, text='另存为', command=self.saveAs)
        self.quitButton = tk.Button(
            master=self.buttonFrame, text='退出', command=self.quit)

    def save(self):
        save(path=self.path, data=self.data, suffix=self.suffix)

    def saveAs(self):
        saveAs(self.data, self.suffix)

    def pack(self, window):
        window.config(menu=self.menu_bar)
        # self.saveButton.pack(side='right')
        # self.saveAsButton.pack(side='right')
        # self.quitButton.pack(side='right')
        self.table.pack(fill='both', expand=True)
