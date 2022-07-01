from tkinter import *   
from tkinter import messagebox 

top = Tk()  
  
top.geometry("200x100")  
  
def fun():  
    import PacMangame
    messagebox("LEVEL1", PacMangame) 
 

def happy(): 
     import level2
     messagebox("LEVEL2", level2 )
 
def close_window(): 
    exit() 
b1 = Button(top,text = "LEVEL1",command = fun,activeforeground = "red",activebackground = "pink",pady=10)  
  
b2 = Button(top, text = "LEVEL2", command= happy , activeforeground = "blue",activebackground = "pink",pady=10)  
  
b3 = Button(top, text = "   EXIT  ", command= close_window,  activeforeground = "green",activebackground = "pink",pady = 10)  
  
b1.pack(side = TOP)  
  
b2.pack(side = TOP)  
  
b3.pack(side = TOP)  
top.mainloop()  