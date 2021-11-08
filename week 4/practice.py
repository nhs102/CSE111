from tkinter import *

window=Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

label=Label(window, text="파이썬", anchor='center', width=10, height=5, fg="red", relief="solid", bg='green')
label.pack()

window.mainloop()