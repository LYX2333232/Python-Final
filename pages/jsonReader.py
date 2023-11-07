
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from FILE.openFile import openFile
from FILE.saveFile import save, saveAs
import json


class JsonReader:
    def __init__(self, path, quit):
        self.path = path
        self.suffix = 'json'
        self.tree = ttk.Treeview()
        self.quit = quit
        self.createMenu()
        self.createSelectMenu()
        self.readJson()
        self.build_tree('', self.data)
        self.tree.bind("<Button-3>", self.on_right_click)

    def createMenu(self):
        self.menu_bar = tk.Menu()
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="打开", command=openFile)
        self.file_menu.add_command(label="保存", command=self.save)
        self.file_menu.add_command(label="另存为", command=self.saveAs)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="退出", command=quit)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)

    def save(self):
        save(self.path, self.data, suffix=self.suffix)

    def saveAs(self):
        saveAs(self.data, self.suffix)

    def delete(self):
        item = self.tree.selection()[0]
        self.tree.delete(item)

    def add_brother(self):
        item = self.tree.selection()[0]
        parent = self.tree.parent(item)
        # 弹出对话框请求用户输入
        text = simpledialog.askstring(title='输入', prompt='请输入元素名')
        # 用户取消输入
        if text == None:
            return
        self.tree.insert(parent, 'end', text=text)

    def add_child(self):
        item = self.tree.selection()[0]
        # 弹出对话框请求用户输入
        text = simpledialog.askstring(title='输入', prompt='请输入元素名')
        # 用户取消输入
        if text == None:
            return
        self.tree.insert(item, 'end', text=text)

    def createSelectMenu(self):
        self.select_bar = tk.Menu()
        self.select_bar.add_cascade(label="删除该元素及其子元素", command=self.delete)
        add_menu = tk.Menu(tearoff=0)
        add_menu.add_command(label="添加兄弟元素", command=self.add_brother)
        add_menu.add_command(label="添加子元素", command=self.add_child)
        self.select_bar.add_cascade(label="添加元素", menu=add_menu)

    def on_right_click(self, event):
        # item = self.tree.identify_row(event.y)
        # print(item)
        self.tree.selection_set(self.tree.identify_row(event.y))
        self.select_bar.post(event.x_root, event.y_root)

    def build_tree(self, parent, data):
        if isinstance(data, dict):
            for key, value in data.items():
                item = self.tree.insert(parent, 'end', text=key)
                self.build_tree(item, value)
        elif isinstance(data, list):
            for item in data:
                child = self.tree.insert(parent, 'end', text=' ')
                self.build_tree(child, item)
        else:
            self.tree.insert(parent, 'end', text=data)

    def readJson(self):
        with open(self.path, 'r') as f:
            self.data = json.loads(f.read())

    def pack(self, window):
        window.config(menu=self.menu_bar)
        self.tree.pack(fill='both', expand=True)
