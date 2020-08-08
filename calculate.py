from  tkinter import *
exp = " "
def Input(num) :
    global exp
    exp = exp + str(num)
    eq.set(exp)
def Result() :
    try :
        global exp
        total = str(eval (exp))
        eq.set(total)
        exp = " "
    except :
        eq.set ("  error  ")
        exp = ""
def CE () :
    global exp
    exp  = " "
    eq.set (" ")
if  __name__=="__main__":
    win = Tk ()
    win.configure (background="blue")
    win.title (" VVDev Calculator")
    win.option_add (' *Font ' , ' arial 15 bold ')
    win.geometry ("460x340")
    eq = StringVar ()
    
    Display = Entry (win , relief=RIDGE, textvariable=eq, justify="right" ,bd= 25)
    
    eq.set ( ' 0 ' )
    
    Display.grid(columnspan=4 ,  ipadx=100)
    
    btn1 = Button (win, text=' 1 ', fg="black", bg= "red" , 
                   command = lambda:  input (1), bd=10, height=2,  width=10)
    btn1.grid(row=1, column=0)
       
    btn2 = Button (win, text=' 2  ', fg="black", bg= "red" ,  
                   command = lambda:  input (2), bd=10, height=2,  width=10)
    btn2.grid(row=1, column=1)
      
    btn3 = Button (win, text=' 3 ',fg="black", bg= "red" , 
                   command = lambda: input (3), bd=10, height=2,  width=10)
    btn3.grid(row=1, column=2)
      
    plus = Button (win, text=' + ', fg="black", bg= "red" ,   
                   command = lambda:  input ("+") ,bd=10, height=2,  width=10)
    plus.grid(row=1, column=3)
    
    btn4 = Button (win, text=' 4 ', fg="black", bg= "red" , 
                   command = lambda:  input (4), bd=10, height=2,  width=10)
    btn4.grid(row=2, column=0)
       
    btn5 = Button (win, text=' 5  ', fg="black", bg= "red" ,  
                   command = lambda:  input (5), bd=10, height=2,  width=10)
    btn5.grid(row=2, column=1)
      
    btn6 = Button (win, text=' 3 ',fg="black", bg= "red" ,  
                   command = lambda: input (3), bd=10, height=2,  width=10)
    btn6.grid(row=2, column=2)
      
    minus = Button (win, text=' - ', fg="black", bg= "red" , 
                   command = lambda:  input ("-") ,bd=10, height=2,  width=10)
    minus.grid(row=2, column=3)
    
    btn7 = Button (win, text=' 7 ',fg="black", bg= "red" ,  
                   command = lambda:  input (7), bd=10, height=2,  width=10)
    btn7.grid(row=3, column=0)
       
    btn8 = Button (win, text=' 8  ', fg="black", bg= "red" ,  
                   command = lambda:  input (8), bd=10, height=2,  width=10)
    btn8.grid(row=3, column=1)
      
    btn9 = Button (win, text=' 9 ', fg="black", bg= "red" , 
                   command = lambda: input (9), bd=10, height=2,  width=10)
    btn9.grid(row=3, column=2)
      
    multiply = Button (win, text=' * ',fg="black", bg= "red" ,  
                   command = lambda:  input ("*") ,bd=10, height=2,  width=10)
    multiply.grid(row=3, column=3)
    
    btn0 = Button (win, text=' 0 ',fg="black", bg= "red" ,  
                   command = lambda:  input (0), bd=10, height=2,  width=10)
    btn0.grid(row=4, column=0)
       
    divide = Button (win, text=' /  ', fg="black", bg= "red" ,   
                   command = lambda:  input (" / "), bd=10, height=2,  width=10)
    divide.grid(row=4, column=1)
      
    equal = Button (win, text=' = ', fg="black", bg= "red" , 
                   command = lambda: input (" = "), bd=10, height=2,  width=10)
    equal.grid(row=4, column=2)
      
    CE = Button (win, text=' CE ',fg="black", bg= "red" , 
                   command = lambda:  input ("+") ,bd=10, height=2,  width=10)
    CE.grid(row=4, column=3)
    
    win.mainloop ()