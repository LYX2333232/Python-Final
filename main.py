import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
label.pack()

window.mainloop()
