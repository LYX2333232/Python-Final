import tkinter as tk
import csv
from tkinter.filedialog import asksaveasfilename


def save(path, data, suffix):
    print(path)
    print(data)
    # 保存文件
    if suffix == 'txt':
        with open(path, 'w') as f:
            f.write(data)
    elif suffix == 'csv':
        # 将数据转变为字符串
        res = []
        maxX = len(data)
        maxY = len(data[0])
        for i in range(len(data)):
            arr = []
            for j in range(len(data[i])):
                if i >= maxX or j >= maxY:
                    if data[i][j].get() != '':
                        tk.messagebox.showerror(
                            title='错误', message='不成行的数据无法保存，请进行修改！\n错误位置：第'+str(i+1)+'行，第'+str(j+1)+'列')
                        return
                    continue
                if data[i][j].get() == '':
                    if j == 0 and i < maxX:
                        maxX = i
                    elif i == 0 and j < maxY:
                        maxY = j
                    else:
                        tk.messagebox.showerror(
                            title='错误', message='不成行的数据无法保存，请进行修改！\n错误位置：第'+str(i+1)+'行，第'+str(j+1)+'列')
                        return
                    continue
                arr.append(data[i][j].get())
            res.append(arr)
        with open(path, 'w', newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)
            for row in res:
                writer.writerow(row)
    tk.messagebox.showinfo(title='提示', message='保存成功')


def saveAs(data, suffix):
    # 选择保存路径
    path = asksaveasfilename(
        filetypes=[(suffix, '.'+suffix)], defaultextension='.'+suffix)
    # 用户取消保存
    if path == '':
        return
    # 保存文件
    save(path, data, suffix)
