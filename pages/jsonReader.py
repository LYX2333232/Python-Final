
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
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
        # 设定滚动条
        self.scrollbar = tk.Scrollbar(master=self.tree)
        self.scrollbar.config(command=self.tree.yview)  # 绑定滚动条和文本框
        self.tree.config(yscrollcommand=self.scrollbar.set)  # 绑定文本框和滚动条

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
        print(self.data)
        save(self.path, self.data, suffix=self.suffix)

    def saveAs(self):
        saveAs(self.data, self.suffix)

    def delete(self):
        item = self.tree.selection()[0]
        # 找到对应的位置
        data = self.data
        parents = []  # 用于存储所有父节点
        parent = self.tree.parent(item)
        while parent != '':
            parents.append(self.tree.item(parent)['text'].split(':')[0])
            parent = self.tree.parent(parent)
        # 在data中删除对应的元素
        parents.reverse()
        for i in parents:
            if isinstance(data, list):
                data = data[int(i)]
            else:
                data = data[i]
        parent = self.tree.parent(item)
        # 删除元素
        if isinstance(data, list):
            data.pop(int(self.tree.item(item)['text'].split(':')[0]))
        else:
            data.pop(self.tree.item(item)['text'].split(':')[0])
        self.tree.delete(item)
        print(self.data)
        if isinstance(data, list):
            # 需要重新渲染序号
            for i in range(len(data)):
                value = data[i]
                if isinstance(value, dict):
                    value = 'dict'
                elif isinstance(value, list):
                    value = 'list'
                else:
                    value = str(value)
                self.tree.item(self.tree.get_children(parent)[i],
                               text=str(i)+':   '+value)

    def add_brother(self):
        # -----------------------------------------------------------------------
        # 获取选中节点及其父节点
        if self.tree.selection() == ():  # 如果没有选中任何元素
            # 视为在根节点添加元素
            parent = ''
        else:
            item = self.tree.selection()[0]
            parent = self.tree.parent(item)
        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        # 找到最近的父节点
        data = self.data
        if parent == '':
            pass
        else:
            parents = []  # 用于存储所有父节点

            # 循环找到所有父节点以确认最近的父节点的text
            while parent != '':
                parents.append(self.tree.item(parent)['text'].split(':')[0])
                parent = self.tree.parent(parent)

            parents.reverse()
            # 找到最近的父节点
            for i in parents:
                data = data[i]
        parent = self.tree.parent(item)
        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        # 弹出对话框请求用户输入
        # 判断是否是数组
        if isinstance(data, list):
            while True:
                Type = simpledialog.askstring(
                    title='输入类型', prompt='请输入元素类型(1代表数值，2代表数组，3代表对象)')
                if Type == None:
                    return
                if Type not in ['1', '2', '3']:
                    messagebox.showerror(title='错误', message='类型错误！请重试')
                    continue
                if Type == '1':
                    value = simpledialog.askinteger(
                        title='输入键值', prompt='请输入键值')
                    if value == None:
                        return
                    self.tree.insert(parent, 'end', text=str(
                        len(data))+':   '+str(value))
                    data.append(value)
                    break
                elif Type == '2':
                    self.tree.insert(parent, 'end', text=str(
                        len(data))+':   array')
                    data.append([])
                    break
                elif Type == '3':
                    self.tree.insert(parent, 'end', text=str(
                        len(data))+':   dict')
                    data.append({})
                    break
        else:
            text = ''
            while True:
                text = simpledialog.askstring(title='输入键名', prompt='请输入元素名')
                if text == '':
                    # 弹窗提示用户输入为空
                    messagebox.showerror(title='错误', message='键名不能为空！')
                    continue
                if text is None:
                    #  用户关闭输入
                    return
                break

            # 输入的键名已存在
            if text in data:
                # 弹出对话框提示用户
                if simpledialog.askstring(title='提示', prompt='键名已存在，是否覆盖？') == 'yes':
                    pass
                else:
                    return
            while True:
                Type = simpledialog.askstring(
                    title='输入类型', prompt='请输入元素类型(1代表数值，2代表数组，3代表对象)')
                if Type == None:
                    return
                if Type not in ['1', '2', '3']:
                    messagebox.showerror(title='错误', message='类型错误！请重试')
                    continue
                break
            if Type == '1':
                value = simpledialog.askinteger(title='输入键值', prompt='请输入键值')
                # 用户关闭输入
                if value == None:
                    return
                # 将数据添加到data中和tree中
                self.tree.insert(parent, 'end', text=str(
                    text)+':   '+str(value))
                # 将数据放入data的对应位置
            elif Type == '2':
                value = []
                self.tree.insert(parent, 'end', text=str(
                    text)+':   array')
            elif Type == '3':
                value = {}
                self.tree.insert(parent, 'end', text=str(
                    text)+':   dict')
            data[text] = value
        print(self.data)

    def add_child(self):
        # -----------------------------------------------------------------------
        # 获取选中节点及其父节点
        if self.tree.selection() == ():  # 如果没有选中任何元素
            # 视为在根节点添加元素
            messagebox.showerror(title='错误', message='请先选中一个元素！')
            return
        else:
            item = self.tree.selection()[0]
        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        # 找到最近的父节点
        data = self.data
        parents = []  # 用于存储所有父节点
        parent = item

        # 循环找到所有父节点以确认最近的父节点的text
        while parent != '':
            parents.append(self.tree.item(parent)['text'].split(':')[0])
            parent = self.tree.parent(parent)

        parents.reverse()
        # 找到最近的父节点
        for i in parents:
            if isinstance(data, list):
                data = data[int(i)]
            else:
                data = data[i]
        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        # 弹出对话框请求用户输入
        # 判断是否是数组
        if isinstance(data, list):
            while True:
                Type = simpledialog.askstring(
                    title='输入类型', prompt='请输入元素类型(1代表数值，2代表数组，3代表对象)')
                if Type == None:
                    return
                if Type not in ['1', '2', '3']:
                    messagebox.showerror(title='错误', message='类型错误！请重试')
                    continue
                if Type == '1':
                    value = simpledialog.askinteger(
                        title='输入键值', prompt='请输入键值')
                    if value == None:
                        return
                    self.tree.insert(item, 'end', text=str(
                        len(data))+':   '+str(value))
                    data.append(value)
                    break
                elif Type == '2':
                    self.tree.insert(item, 'end', text=str(
                        len(data))+':   array')
                    data.append([])
                    break
                elif Type == '3':
                    self.tree.insert(item, 'end', text=str(
                        len(data))+':   dict')
                    data.append({})
                    break
        elif isinstance(data, dict):
            text = ''
            while True:
                text = simpledialog.askstring(title='输入键名', prompt='请输入元素名')
                if text == '':
                    # 弹窗提示用户输入为空
                    messagebox.showerror(title='错误', message='键名不能为空！')
                    continue
                if text is None:
                    #  用户关闭输入
                    return
                break

            # 输入的键名已存在
            if text in data:
                # 弹出对话框提示用户
                if simpledialog.askstring(title='提示', prompt='键名已存在，是否覆盖？') == 'yes':
                    pass
                else:
                    return
            while True:
                Type = simpledialog.askstring(
                    title='输入类型', prompt='请输入元素类型(1代表数值，2代表数组，3代表对象)')
                if Type == None:
                    return
                if Type not in ['1', '2', '3']:
                    messagebox.showerror(title='错误', message='类型错误！请重试')
                    continue
                break
            if Type == '1':
                value = simpledialog.askinteger(title='输入键值', prompt='请输入键值')
                # 用户关闭输入
                if value == None:
                    return
                # 将数据添加到data中和tree中
                self.tree.insert(item, 'end', text=str(
                    text)+':   '+str(value))
                # 将数据放入data的对应位置
            elif Type == '2':
                value = []
                self.tree.insert(item, 'end', text=str(
                    text)+':   array')
            elif Type == '3':
                value = {}
                self.tree.insert(item, 'end', text=str(
                    text)+':   dict')
            data[text] = value
        else:
            messagebox.showerror(title='错误', message='叶子节点不支持添加子元素！')
            return
        print(self.data)

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
                # 对象类
                if isinstance(value, dict):
                    child = self.tree.insert(
                        parent, 'end', text=str(key)+':   '+'dict')
                    self.build_tree(child, value)
                # 数组类
                elif isinstance(value, list):
                    child = self.tree.insert(
                        parent, 'end', text=str(key)+':   '+'list')
                    self.build_tree(child, value)
                # 叶子
                else:
                    self.tree.insert(
                        parent, 'end', text=str(key)+':   '+str(value))
        elif isinstance(data, list):
            for index in range(len(data)):
                # 对象类
                if isinstance(data[index], dict):
                    child = self.tree.insert(
                        parent, 'end', text=str(index)+':   '+'dict')
                    self.build_tree(child, data[index])
                # 数组类
                elif isinstance(data[index], list):
                    child = self.tree.insert(
                        parent, 'end', text=str(index)+':   '+'list')
                    self.build_tree(child, data[index])
                else:
                    self.tree.insert(parent, 'end', text=str(
                        index)+':   '+str(data[index]))

    def readJson(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            self.data = json.loads(f.read())

    def pack(self, window):
        window.config(menu=self.menu_bar)
        self.scrollbar.pack(side='right', fill='y')
        self.tree.config(yscrollcommand=self.scrollbar.set)
        self.tree.pack(fill='both', expand=True)
