from tkinter import*

window = Tk()

w = Canvas(window, width = 300, height = 300)
w.pack

w.create_rectangle(50,25,200,100, fill='#FF24B5')
w.create_line(5,5,25,25, fill='Moccasin')

window.mainloop()