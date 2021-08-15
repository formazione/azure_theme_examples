import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk
# create the window
root= tk.Tk()
root.title("Example Error handling")
root.geometry("400x200")

# Give it this theme (put the folder azure dark here
style = ttk.Style(root)
root.tk.call('source', 'theme/azure dark/azure dark.tcl')
style.theme_use('azure')

# Entry widget
strvar= tk.IntVar()
entry = ttk.Entry(root,textvariable=strvar)
entry.place(x=10,y=10)
def check():
    print(entry.get())
    button.config(relief="flat")
    if int(entry.get()) < 1:
        entry.state(["invalid"])

btnimage = ImageTk.PhotoImage(file=('button.png'))
button=tk.Button(root,image=btnimage,bd=0,activebackground="#333333",relief="flat", text="Click", compound=tk.CENTER, command=check)
button.place(x=5,y=50)
root.mainloop()