import tkinter as tk
import playsound
window = tk.Tk()
window.title('음식계산기')
window.geometry('600x400+100+100')

def func():
    print('click')

image1 = tk.PhotoImage(file='짜장면.png')
button = tk.Button(image=image1, command = func, bd=0)
button2 = tk.Button(image=image1, command = func, bd=0)
button.pack()
button2.pack()

window.mainloop()