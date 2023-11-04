import tkinter as tk
from openFile import openFile
from saveFile import saveFile
from welcome import Welcome

if __name__ == "__main__":
    window = tk.Tk()
    window.title("文件阅读器")
    window.minsize(width=500, height=300)
    welcome = Welcome(openFile=openFile, saveFile=saveFile, quit=window.quit)
    welcome.pack(window)
    window.mainloop()
