from tkinter import *
root = Tk()
root.title("My Title")
root.geometry("400x300")

b=5

def square(a):
    print(a*a)

def value(x):
    print("2");

#b=4
button1 = Button(root, text="Square", command= lambda:square(b))    #lambda lgane se button dbane pe hoga
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = Button(root, text ="2", command = lambda:value(b))
button2.grid(row=1, column=0, padx=0, pady=0)

root.resizable(10,0)
root.mainloop()