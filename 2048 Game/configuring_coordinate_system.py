# from tkinter import *
#
# screen = Tk()
# screen.geometry("600x810")
#
# canvas = Canvas(screen, height=600, width=600, borderwidth=0, highlightthickness=0)
# canvas.grid(row=2, column=0)
#
# textvariable = StringVar()
# textvariable.set('2')
# label = Label(canvas, font=("Arial", 22, "bold"), textvariable=textvariable)
# label.pack()
#
# for n in range(1, 12):
#     textvariable.set(2**n)
#     screen.update()
#     print(label.winfo_width(), label.winfo_height())
#
# screen.mainloop()

from tkinter import *

screen = Tk()
screen.geometry("600x810")

canvas = Canvas(screen, height=600, width=600, borderwidth=0, highlightthickness=0)
canvas.grid(row=2, column=0)

textvariable = StringVar()
textvariable.set('Score: 0')
label = Label(canvas, font=("Arial", 30, "bold"), textvariable=textvariable)
label.pack()

for n in [0] + ["2"*n for n in range(1, 20)]:
    textvariable.set(f"Score: {n}")
    screen.update()
    print(label.winfo_width()/2, label.winfo_height())

screen.destroy()

