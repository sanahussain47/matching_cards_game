import tkinter as tk

root = tk.Tk()
root.title("Test Window")
root.geometry("300x200")
tk.Label(root, text="Hello, tkinter!").pack()
root.mainloop()
