import tkinter as tk
from tkinter import filedialog


def openFile():
    # 弹出文件选择框
    filepath = filedialog.askopenfilename(initialdir="./")
    # 后缀
    suffix = filepath.split('.')[-1]
    # 文件名
    name = filepath.split('/')[-1].split('.')[0]
    # print(filepath)
    with open(filepath, 'r') as file:
        content = file.read()
        print(content)
    return content, suffix, name
