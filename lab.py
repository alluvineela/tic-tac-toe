from tkinter import*
from tkinter import messagebox
import random
root=Tk()
root.title("knoughts and crosses")
root.geometry('300x300')

clicked = True
count = 0

def click(bt):
    global clicked,count

   
    if bt["text"] == "" and clicked == True:
        bt["text"] = "X"
        clicked = False
        count += 1
        checkwhowon()
    elif bt["text"] == "" and clicked == False:
        bt["text"] = "O"
        clicked = True
        count += 1
        checkwhowon()
 
    


def disable_all_buttons():
   bt1.config(state=DISABLED)
   bt2.config(state=DISABLED)
   bt3.config(state=DISABLED)
   bt4.config(state=DISABLED)
   bt5.config(state=DISABLED)
   bt6.config(state=DISABLED)
   bt7.config(state=DISABLED)
   bt8.config(state=DISABLED)
   bt9.config(state=DISABLED)
    
def checkwhowon():
    global winner
    winner = False
    if bt1["text"] == "X" and bt2["text"] == "X" and bt3["text"] == "X":
        bt1.config(bg = "red")
        bt2.config(bg = "red")
        bt3.config(bg = "red")
        winner = True
        messagebox.showinfo("congrats"," X wins")
        disable_all_buttons()
    elif bt1["text"] == "O" and bt2["text"] == "O" and bt3["text"] == "O":
        bt1.config(bg = "blue")
        bt2.config(bg = "blue")
        bt3.config(bg = "blue")
        winner = True
        messagebox.showinfo("congrats"," X wins")
        disable_all_buttons()
    elif bt4["text"] == "X" and bt5["text"] == "X" and bt6["text"] == "X":
        bt4.config(bg = "red")
        bt5.config(bg = "red")
        bt6.config(bg = "red")
        winner = True
        messagebox.showinfo("congrats"," X wins")
        disable_all_buttons()
    elif bt4["text"] == "O" and bt5["text"] == "O" and bt6["text"] == "O":
        bt4.config(bg = "blue")
        bt5.config(bg = "blue")
        bt6.config(bg = "blue")
        winner = True
        messagebox.showinfo("congrats"," O wins")
        disable_all_buttons()
    elif bt7["text"] == "X" and bt8["text"] == "X" and bt9["text"] == "X":
        bt7.config(bg = "red")
        bt8.config(bg = "red")
        bt9.config(bg = "red")
        winner = True
        messagebox.showinfo("congrats"," X wins")
        disable_all_buttons()
    elif bt7["text"] == "O" and bt8["text"] == "O" and bt9["text"] == "O":
        bt7.config(bg = "blue")
        bt8.config(bg = "blue")
        bt9.config(bg = "blue")
        winner = True
        messagebox.showinfo("congrats"," O wins")
        disable_all_buttons()
    elif bt1["text"] == "X" and bt5["text"] == "X" and bt9["text"] == "X":
        bt1.config(bg = "red")
        bt5.config(bg = "red")
        bt9.config(bg = "red")
        winner = True
        messagebox.showinfo("congrats"," X wins")
        disable_all_buttons()
    elif bt1["text"] == "O" and bt5["text"] == "O" and bt9["text"] == "O":
        bt1.config(bg = "blue")
        bt5.config(bg = "blue")
        bt9.config(bg = "blue")
        winner = True
        messagebox.showinfo("congrats"," O wins")
        disable_all_buttons()
    elif bt3["text"] == "X" and bt5["text"] == "X" and bt7["text"] == "X":
        bt3.config(bg = "red")
        bt5.config(bg = "red")
        bt7.config(bg = "red")
        winner = True
        messagebox.showinfo("congrats"," X wins")
        disable_all_buttons()
    elif bt3["text"] == "O" and bt5["text"] == "O" and bt7["text"] == "O":
        bt3.config(bg = "blue")
        bt5.config(bg = "blue")
        bt7.config(bg = "blue")
        winner = True
        messagebox.showinfo("congrats"," O wins")
        disable_all_buttons()
    elif bt1["text"] == "X" and bt4["text"] == "X" and bt7["text"] == "X":
        bt1.config(bg = "red")
        bt4.config(bg = "red")
        bt7.config(bg = "red")
        winner = True
        messagebox.showinfo("congrats"," X wins")
        disable_all_buttons()
    elif bt1["text"] == "O" and bt4["text"] == "O" and bt7["text"] == "O":
        bt3.config(bg = "blue")
        bt5.config(bg = "blue")
        bt7.config(bg = "blue")
        winner = True
        messagebox.showinfo("congrats"," O wins")
        disable_all_buttons()
    elif bt2["text"] == "X" and bt5["text"] == "X" and bt8["text"] == "X":
        bt2.config(bg = "red")
        bt5.config(bg = "red")
        bt8.config(bg = "red")
        winner = True
        messagebox.showinfo("congrats"," X wins")
        disable_all_buttons()
    elif bt2["text"] == "0" and bt5["text"] == "O" and bt8["text"] == "O":
        bt2.config(bg = "blue")
        bt5.config(bg = "blue")
        bt8.config(bg = "blue")
        winner = True
        messagebox.showinfo("congrats"," O wins")
        disable_all_buttons()
    elif bt3["text"] == "0" and bt6["text"] == "O" and bt9["text"] == "O":
        bt3.config(bg = "blue")
        bt6.config(bg = "blue")
        bt9.config(bg = "blue")
        winner = True
        messagebox.showinfo("congrats"," O wins")
        disable_all_buttons()
    elif bt3["text"] == "X" and bt6["text"] == "X" and bt9["text"] == "X":
        bt3.config(bg = "red")
        bt6.config(bg = "red")
        bt9.config(bg = "red")
        winner = True
        messagebox.showinfo("congrats"," X wins")
        disable_all_buttons()
    
bt1=Button(root,text="",command=lambda:click(bt1))
bt2=Button(root,text="",command=lambda:click(bt2))
bt3=Button(root,text="",command=lambda:click(bt3))

bt4=Button(root,text="",command=lambda:click(bt4))
bt5=Button(root,text="",command=lambda:click(bt5))
bt6=Button(root,text="",command=lambda:click(bt6))

bt7=Button(root,text="",command=lambda:click(bt7))
bt8=Button(root,text="",command=lambda:click(bt8))
bt9=Button(root,text="",command=lambda:click(bt9))

bt1.grid(row=0,column=0,ipadx = 45,ipady = 37)
bt2.grid(row=0,column=1,ipadx = 45,ipady = 37)
bt3.grid(row=0,column=2,ipadx = 45,ipady = 37)

bt4.grid(row=1,column=0,ipadx = 45,ipady = 37)
bt5.grid(row=1,column=1,ipadx = 45,ipady = 37)
bt6.grid(row=1,column=2,ipadx = 45,ipady = 37)

bt7.grid(row=2,column=0,ipadx = 45,ipady = 37)
bt8.grid(row=2,column=1,ipadx = 45,ipady = 37)
bt9.grid(row=2,column=2,ipadx = 45,ipady = 37)
    
root.mainloop()
