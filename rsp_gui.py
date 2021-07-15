from tkinter import *
import random

root = Tk()
root.title("가위바위보")
root.geometry("250x80")

root.resizable(False, False)

def setTextInput(text):
    rsp.delete(0, "end")
    rsp.insert(0, text)

lbl = Label(root, text="가위바위보\n가위,바위,보만 입력하셔야됩니다.")
lbl.pack()

rsp = Entry(root)
rsp.pack()

btn = Button(root, text="클릭", command=lambda:setTextInput(random.choice(['승리', '패배', '무승부'])))
btn.pack()
    
root.mainloop()