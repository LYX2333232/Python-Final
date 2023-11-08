import tkinter as tk
from FILE.openFile import openFile
from FILE.saveFile import saveAs, save
# txt文件阅读器


class TxtReader:
    def __init__(self, path, name, quit):
        self.path = path
        self.name = name
        self.suffix = 'txt'
        self.quit = quit
        # 以name为标题
        self.label = tk.Label(text=name)
        with open(path, 'r') as f:
            self.content = f.read()
        # 将数据放入可修改的文本框中
        self.text = tk.Text()
        # 设置文本框大小与页面一致
        self.text.insert('end', self.content)
        # 滚动条
        self.scrollbar = tk.Scrollbar(master=self.text)
        self.scrollbar.config(command=self.text.yview)  # 绑定滚动条和文本框
        self.text.config(yscrollcommand=self.scrollbar.set)  # 绑定文本框和滚动条
        self.createMenu()
        # 底部按钮
        self.createButton()

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
        save(self.path, self.text.get('1.0', 'end'), suffix=self.suffix)

    def saveAs(self):
        saveAs(self.text.get('1.0', 'end'), self.suffix)

    def pack(self, window):
        self.label.pack()
        self.saveButton.pack(side='right')
        self.saveAsButton.pack(side='right')
        self.quitButton.pack(side='right')
        window.config(menu=self.menu_bar)
        self.scrollbar.pack(side='right', fill='y')
        self.text.pack(fill='both', expand=True)
