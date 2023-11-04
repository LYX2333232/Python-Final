import tkinter as tk
from FILE.openFile import openFile
from FILE.saveFile import saveFile
from pages.welcome import Welcome
from pages.txtReader import TxtReader

window = tk.Tk()
window.title("文件阅读器")
window.minsize(width=500, height=300)


def readPage():
    global window
    path, suffix, name = openFile()
    # 用户取消读取
    if path == '':
        return
    for widget in window.winfo_children():
        widget.destroy()
    if suffix == 'txt':
        txtReader = TxtReader(path=path, name=name,
                              save=saveFile, quit=welcomePage)
        txtReader.pack(window)


def welcomePage():
    global window
    for widget in window.winfo_children():
        widget.destroy()
    welcome = Welcome(openFile=readPage, saveFile=saveFile, quit=window.quit)
    welcome.pack(window)
    window.mainloop()


if __name__ == "__main__":
    welcomePage()
