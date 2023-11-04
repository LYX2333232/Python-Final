import tkinter as tk
# txt文件阅读器


class TxtReader:
    def __init__(self, path, name, save, quit):
        self.path = path
        # 以name为标题
        self.label = tk.Label(text=name)
        with open(path, 'r') as f:
            self.content = f.read()
        # 将数据放入可修改的文本框中
        self.text = tk.Text()
        # 设置文本框大小与页面一致
        self.text.insert('end', self.content)
        # 滚动条
        # self.scrollbar = tk.Scrollbar(master=self.text)
        # self.scrollbar.config(command=self.text.yview)  # 绑定滚动条和文本框
        # self.text.config(yscrollcommand=self.scrollbar.set)  # 绑定文本框和滚动条
        # 底部按钮
        self.buttonFrame = tk.Frame()
        self.buttonFrame.pack(side='top', fill='x')
        self.saveButton = tk.Button(
            master=self.buttonFrame, text='保存', command=save)

        self.quitButton = tk.Button(
            master=self.buttonFrame, text='退出', command=quit)

    def pack(self, window):
        self.label.pack()
        self.saveButton.pack(side='right')
        self.quitButton.pack(side='right')
        self.text.pack(fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y')
