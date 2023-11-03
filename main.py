import tkinter as tk
from openFile import *

window = tk.Tk()
window.title("文件阅读器")
window.minsize(width=500, height=300)

# Label
label = tk.Label(text="欢迎使用文件阅读器", font=("Arial", 24, "bold"))
label.pack()

# Button
open_button = tk.Button(text="Open", command=openFile)
open_button.pack()

# 头部菜单栏
menu_bar = tk.Menu()
# 文件菜单
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# 添加到菜单栏
menu_bar.add_cascade(label="File", menu=file_menu)

# 编辑菜单
window.config(menu=menu_bar)

window.mainloop()
