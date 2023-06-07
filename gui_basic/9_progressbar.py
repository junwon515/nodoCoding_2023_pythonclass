import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()



# def btncmd():
#     progressbar.stop() # 작동중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar.pack()

def btncmd():
    for i in range(1, 101):
        time.sleep(0.01)

        p_var2.set(i)
        progressbar.update()
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd)
btn.pack()

root.mainloop()
