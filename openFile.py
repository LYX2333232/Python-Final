import tkinter as tk
from tkinter import filedialog


def openFile():
    # 弹出文件选择框
    filepath = filedialog.askopenfilename(initialdir="./")
    # print(filepath)
    with open(filepath, 'r') as file:
        content = file.read()
        print(content)
