import tkinter as tk
from tkinter import ttk
import json


def build_tree(tree, parent, data):
    if isinstance(data, dict):
        for key, value in data.items():
            item = tree.insert(parent, 'end', text=key)
            build_tree(tree, item, value)
    elif isinstance(data, list):
        for item in data:
            child = tree.insert(parent, 'end', text=' ')
            build_tree(tree, child, item)
    else:
        tree.insert(parent, 'end', text=data)


def display_json_tree(data):
    root = tk.Tk()
    root.title('JSON Tree')

    tree = ttk.Treeview(root)
    build_tree(tree, '', data)
    tree.pack()

    root.mainloop()


json_data = {
    "name": "John",
    "age": 30,
    "cars": [
        {
            "name": "Ford",
            "models": [
                "Fiesta",
                "Focus",
                "Mustang"
            ]
        },
        {
            "name": "BMW",
            "models": [
                "320",
                "X3",
                "X5"
            ]
        }
    ]
}

data = json.loads(json.dumps(json_data))

display_json_tree(data)
