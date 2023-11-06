import tkinter as tk

root = tk.Tk()
root.title("文件阅读器")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

canvas = tk.Canvas(frame)
# 设置滚动条
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")


canvas.bind_all("<MouseWheel>", _on_mousewheel)


# 设置横向的滚动条

# 设置滚动条的位置
canvas.pack(side="left", fill="both", expand=True)

# 设置画布的位置
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# 设置两行10列的文本框
for i in range(100):
    for j in range(10):
        tk.Entry(master=scrollable_frame, text='hello').grid(
            row=i, column=j)

scrollable_frame.update_idletasks()  # 更新画布的尺寸
canvas.config(scrollregion=canvas.bbox("all"))  # 配置画布的滚动区域


root.mainloop()
