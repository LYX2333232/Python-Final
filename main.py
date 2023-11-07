import tkinter as tk
from FILE.openFile import openFile
from FILE.saveFile import save, saveAs
from pages.welcome import Welcome
from pages.txtReader import TxtReader
from pages.csvReader import CsvReader
from pages.jsonReader import JsonReader

window = tk.Tk()
window.title("文件阅读器")
window.minsize(width=500, height=300)


def readPage():
    global window
    path, suffix, name = openFile()
    # 用户取消读取
    if path == '':
        return
    if suffix not in ['txt', 'json', 'csv', 'xls', 'xlsx', 'json']:
        tk.messagebox.showerror(title='错误', message='不支持的文件格式')
        return
    for widget in window.winfo_children():
        widget.destroy()
    if suffix == 'txt':
        txtReader = TxtReader(
            path=path, name=name,  quit=welcomePage)
        txtReader.pack(window)
    if suffix == 'csv':
        csvReader = CsvReader(path=path, name=name, quit=welcomePage)
        csvReader.pack(window)
    if suffix == 'json':
        jsonReader = JsonReader(path=path, quit=welcomePage)
        jsonReader.pack(window)


def welcomePage():
    global window
    for widget in window.winfo_children():
        widget.destroy()
    welcome = Welcome(openFile=readPage,  quit=window.quit)
    welcome.pack(window)


if __name__ == "__main__":
    welcomePage()
    window.mainloop()
