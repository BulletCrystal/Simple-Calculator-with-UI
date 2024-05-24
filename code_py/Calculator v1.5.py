import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Calculator v 1.2')
window.geometry('307x427+800+200')
window.iconbitmap(r'C:\Users\ABDELAZIZ\Desktop\Python\Nouveau dossier\MyIcon (1).ico')
window.resizable(False,False)
#Important
List = []
a = 0
c = 0
b = 0
g = 0
#Functions 

# For MAin Text
def write(x):
    global a,c,g,p
    I_number["foreground"] = I_number["background"]
    if a == 0:
        List.append(x)
        output.set(''.join(List))
    else:
        a = 0
        if x!='1' and x!='2'and x!='3'and x!='4' and x!='5'and x!='6'and x!='7' and x!='8'and x!='9'and x!='0':
            c = len(Data.get())
            List.append(x)
            output.set(''.join(List))
            I_number.config(font=f'Calibri 1 bold')
            print('hello')

            
        else:
            List.clear()
            List.append(x)
            output.set(''.join(List))
    if len(List)+c>15:
        S_number.config(font=f'Calibri 20 bold')
        g =10
        I_number.config(font=f'Calibri {g+45} bold')
        if len(List)+c>21:
            S_number.config(font=f'Calibri 10 bold')
            g+=8
            I_number.config(font=f'Calibri {g+45} bold')
            g = 0
            if len(List)+c>50 :
                    Clear()
                    Data.set('Error')
                    g = 0



    else:
        S_number.config(font='Calibri 30 bold')
        I_number.config(font=f'Calibri 40 bold')

def Clear():
    global a,c,b,g
    Data.set('0')
    output.set('')
    List.clear()
    a = 0
    c = 0
    S_number.config(font='Calibri 30 bold')
    M_number.config(font='Calibri 40 bold')
    I_number.config(font='Calibri 40 bold')
    g = 0
    b = 0
  

def POP():
    global a,c,b,g
    List.pop()
    output.set(''.join(List))
    a = 0
    if len(List)-c <=15:
        I_number.config(font=f'Calibri 40 bold')


def equal():
    global List,a,B,b,p
    a = 1
    B = eval(output.get())
    output.set('')

    List = []         
    Data.set(str(B))
    List.append(Data.get())
    #output.set('')
    if len(Data.get())>11:
        M_number.config(font='Calibri 30 bold')
        b = 10
        I_number.config(font=f'Calibri {40+b} bold')
        if len(Data.get())>15:
            M_number.config(font='Calibri 24 bold')
            b += 15
            I_number.config(font=f'Calibri {40+b} bold')
            p = b+40
            if len(Data.get())>18:
                        Clear()
                        output.set('Error')
                        b = 0
"""def add():
    global a
    a = float(Data.get()) + a
    Data.set(a)
    List.clear()

def sub():
    global a
    a = float(Data.get()) - a
    Data.set(a)
    List.clear()

def mul():
    global a 
    if a != 0:
        a = float(Data.get()) * a
        Data.set(a)
        List.clear()
    else :
        a = float(Data.get())
        Data.set(a)
        List.clear()

def equal():
    global a
    Data.set(a)
    List.clear()
"""
#######

#The data
Data = tk.StringVar (value='0')

M_number = tk.Label(master=window,font=f'Calibri 40 bold',textvariable=Data,foreground='blue',)
M_number.grid(column=1,row=1,columnspan=4,sticky='e')
#the ouput
output = tk.StringVar ()
S_number = tk.Label(master=window,font=f'Calibri 30 bold',textvariable=output,foreground='Gray')
S_number.grid(column=1,row=2,columnspan=4,sticky='e')
#lol

I_number = tk.Label(master=window,font='Calibri 40 bold',text='SMD',foreground='Blue')
I_number.grid(column=1,row=0,columnspan=4)

#NUM Buttons

NUM_1 = ttk.Button(master=window,text='C',command=Clear)
NUM_1.grid(row=4,column=1,ipady=10)
NUM_2 = ttk.Button(master=window,text='<-',command=POP)
NUM_2.grid(row=4,column=2,ipady=10)
NUM_3 = ttk.Button(master=window,text='%',command=lambda:write('%'))
NUM_3.grid(row=4,column=3,ipady=10)
NUM_4 = ttk.Button(master=window,text='/',command=lambda:write('/'))
NUM_4.grid(row=4,column=4,ipady=10)

NUM_5 = ttk.Button(master=window,text='7',command=lambda:write('7'))
NUM_5.grid(row=5,column=1,ipady=10)
NUM_6 = ttk.Button(master=window,text='8',command=lambda:write('8'))
NUM_6.grid(row=5,column=2,ipady=10)
NUM_7 = ttk.Button(master=window,text='9',command=lambda:write('9'))
NUM_7.grid(row=5,column=3,ipady=10)
NUM_8 = ttk.Button(master=window,text='X',command= lambda:write('*'))
NUM_8.grid(row=5,column=4,ipady=10)
#row = 3
NUM_9 = ttk.Button(master=window,text='4',command=lambda:write('4'))
NUM_9.grid(row=6,column=1,ipady=10)
NUM_10 = ttk.Button(master=window,text='5',command=lambda:write('5'))
NUM_10.grid(row=6,column=2,ipady=10)
NUM_11 = ttk.Button(master=window,text='6',command=lambda:write('6'))
NUM_11.grid(row=6,column=3,ipady=10)
NUM_12 = ttk.Button(master=window,text='-',command=lambda:write('-'))
NUM_12.grid(row=6,column=4,ipady=10)

NUM_13 = ttk.Button(master=window,text='1',command=lambda:write('1'))
NUM_13.grid(row=7,column=1,ipady=10)
NUM_14 = ttk.Button(master=window,text='2',command=lambda:write('2'))
NUM_14.grid(row=7,column=2,ipady=10)
NUM_15 = ttk.Button(master=window,text='3',command=lambda:write('3'))
NUM_15.grid(row=7,column=3,ipady=10)
NUM_16 = ttk.Button(master=window,text='+',command=lambda:write('+'))
NUM_16.grid(row=7,column=4,ipady=10)

NUM_17 = ttk.Button(master=window,text='0',command=lambda:write('0'),width=24)
NUM_17.grid(row=8,column=1,ipady=10,columnspan=2)
NUM_19 = ttk.Button(master=window,text='.',command=lambda:write('.'))
NUM_19.grid(row=8,column=3,ipady=10)
NUM_20 = ttk.Button(master=window,text='=',command=equal)
NUM_20.grid(row=8,column=4,ipady=10)
###

# win loop
window.mainloop()