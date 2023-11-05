import tkinter as tk
from FILE.saveFile import save, saveAs
from FILE.openFile import openFile
import csv


class CsvReader:
    def __init__(self, path, name, quit):
        self.path = path
        self.name = name
        self.suffix = 'csv'
        self.quit = quit
        # 创建类似于excel的表格
        self.table = tk.Frame()
        # 创建滚动条
        self.scrollbar = tk.Scrollbar(self.table)
        # self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # 创建表格
        self.canvas = tk.Canvas(self.table, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.canvas.yview)
        self.tableFrame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.tableFrame, anchor='nw')
        # 读取数据
        self.readCsv()
        # 创建表头
        self.createHeader()
        # 创建表格
        self.createTable()
        # 创建按钮
        self.createButton()

    def readCsv(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            self.data = [row for row in reader]

    def createHeader(self):
        for i in range(len(self.data[0])):
            tk.Label(self.tableFrame, text=self.data[0][i]).grid(
                row=0, column=i)

    def createTable(self):
        for i in range(1, len(self.data)):
            for j in range(len(self.data[i])):
                tk.Label(self.tableFrame, text=self.data[i][j]).grid(
                    row=i, column=j)

    def createButton(self):
        tk.Button(self.tableFrame, text='返回', command=self.quit).grid(
            row=len(self.data), column=0)
        # 另存为
        tk.Button(self.tableFrame, text='另存为', command=lambda: saveAs(
            self.data, 'csv')).grid(row=len(self.data), column=2)
        tk.Button(self.tableFrame, text='保存', command=save).grid(
            row=len(self.data), column=1)

    def pack(self, window):
        window.config(menu=None)
        self.table.pack(fill='both', expand=True)
