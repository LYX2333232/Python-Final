import tkinter as tk
from FILE.openFile import openFile
from FILE.saveFile import saveFile
from pages.welcome import Welcome


def welcomePage():
    window = tk.Tk()
    window.title("文件阅读器")
    window.minsize(width=500, height=300)
    welcome = Welcome(openFile=openFile, saveFile=saveFile, quit=window.quit)
    welcome.pack(window)
    window.mainloop()


if __name__ == "__main__":
    welcomePage()
