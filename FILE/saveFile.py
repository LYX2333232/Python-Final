import tkinter as tk
from tkinter.filedialog import asksaveasfilename


def saveFile(path, data, suffix):
    print(path)
    # 选择保存路径
    path = asksaveasfilename(filetypes=[(suffix, '.' + suffix)])
    # 用户取消保存
    if path == '':
        return
    # 保存文件
    with open(path, 'w') as f:
        f.write(data)
    tk.messagebox.showinfo(title='提示', message='保存成功')
