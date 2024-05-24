import tkinter as tk

window = tk.Tk()
window.title('Calculator v2.0')
window.resizable(False,False)
window.iconbitmap(r'C:\Users\ABDELAZIZ\Downloads\Graphicloads-100-Flat-2-Calculator.256.ico')
window.geometry('290x450+700+130')
window.config(background='gray',highlightthickness=5,highlightcolor='brown')
window.wm_attributes('-topmost',1)
#Important
List = []
a = 0
#Functions
def write(x):
    global a
    if a == 0:
        if x =='*':
            List.append('x')
            output_T.set(''.join(List))
        else:
            List.append(x)
            output_T.set(''.join(List))
    else:
        a = 0
        if x!='1' and x!='2'and x!='3'and x!='4' and x!='5'and x!='6'and x!='7' and x!='8'and x!='9'and x!='0':
            if x =='*':
                List.append('x')
                output_T.set(''.join(List))         
            else:
                List.append(x)
                output_T.set(''.join(List))
                
            
        else:
            List.clear()
            List.append(x)
            output_T.set(''.join(List))
    if len(output_T.get()) >10:
        output.config(font='Calibri 30')
    if len(output_T.get()) >=14:
        output.config(font='Calibri 20')
    if len(output_T.get()) >=20:
        output.config(font='Calibri 10')
    if len(output_T.get()) >=40:
        output_T.set('error')
        List.clear()
        output.config(font='Calibri 40')
def equal():
    global a,b,c,d
    c = -1
    for i in List:
        c+=1
        if i == 'x':
            List[c] = '*'
    try:
        b = str(round(eval(''.join(List)),4))
        pass
    except :
        List.clear()
        output_T.set('error')
    b = str(round(eval(''.join(List)),4))
    output_T.set(b)
    List.clear()
    List.append(b)
    a = 1
    if len(output_T.get()) <=10:
        output.config(font='Calibri 40')
    if len(output_T.get()) >=14:
        output.config(font='Calibri 20')
    if len(output_T.get()) >=20:
        output.config(font='Calibri 10')

def Clear():
    List.clear()
    output_T.set('0')
    output.config(font='Calibri 40')

def POP():
    List.pop()
    output_T.set(''.join(List))
    if List == []:
        output_T.set('0')
    if len(output_T.get()) >=10:
        output.config(font='Calibri 40')
    if len(output_T.get()) >=14:
        output.config(font='Calibri 20')
    if len(output_T.get()) >=20:
        output.config(font='Calibri 10')
#output
output_T=tk.Variable(value='0')
output = tk.Label(master=window,textvariable=output_T,font='Calibri 40',foreground='black',background='gray')
output.grid(column=0,row=0,columnspan=4)

#Buttons

NUM_1 = tk.Button(master=window,text='C',font='Calibri 20',command=Clear,bg='#FF5C05',activebackground='#B84406')
NUM_1.place(x=0,y=100,width=70,height=60)
NUM_2 = tk.Button(master=window,text='<-',font='Calibri 20',command=POP,bg='#FF5C05',activebackground='#B84406')
NUM_2.place(x=70,y=100,width=70,height=60)
NUM_3 = tk.Button(master=window,text='%',font='Calibri 20',command=lambda:write('%'),bg='Orange',activebackground='#B84406')
NUM_3.place(x=140,y=100,width=70,height=60)
NUM_4 = tk.Button(master=window,text='/',font='Calibri 20',command=lambda:write('/'),bg='Orange',activebackground='#B84406')
NUM_4.place(x=210,y=100,width=70,height=60)

NUM_5 = tk.Button(master=window,text='7',font='Calibri 20',command=lambda:write('7'),background='#202020',foreground='white')
NUM_5.place(x=0,y=160,width=70,height=60)
NUM_6 = tk.Button(master=window,text='8',font='Calibri 20',command=lambda:write('8'),background='#202020',foreground='white')
NUM_6.place(x=70,y=160,width=70,height=60)
NUM_7 = tk.Button(master=window,text='9',font='Calibri 20',command=lambda:write('9'),background='#202020',foreground='white')
NUM_7.place(x=140,y=160,width=70,height=60)
NUM_8 = tk.Button(master=window,text='X',font='Calibri 20',command=lambda:write('*'),bg='Orange',activebackground='#B84406')
NUM_8.place(x=210,y=160,width=70,height=60)
#row = 3
NUM_9 = tk.Button(master=window,text='4',font='Calibri 20',command=lambda:write('4'),background='#202020',foreground='white')
NUM_9.place(x=0,y=220,width=70,height=60)
NUM_10 = tk.Button(master=window,text='5',font='Calibri 20',command=lambda:write('5'),background='#202020',foreground='white')
NUM_10.place(x=70,y=220,width=70,height=60)
NUM_11 = tk.Button(master=window,text='6',font='Calibri 20',command=lambda:write('6'),background='#202020',foreground='white')
NUM_11.place(x=140,y=220,width=70,height=60)
NUM_12 = tk.Button(master=window,text='-',font='Calibri 20',command=lambda:write('-'),bg='Orange',activebackground='#B84406')
NUM_12.place(x=210,y=220,width=70,height=60)

NUM_13 = tk.Button(master=window,text='1',font='Calibri 20',command=lambda:write('1'),background='#202020',foreground='white')
NUM_13.place(x=0,y=280,width=70,height=60)
NUM_14 = tk.Button(master=window,text='2',font='Calibri 20',command=lambda:write('2'),background='#202020',foreground='white')
NUM_14.place(x=70,y=280,width=70,height=60)
NUM_15 = tk.Button(master=window,text='3',font='Calibri 20',command=lambda:write('3'),background='#202020',foreground='white')
NUM_15.place(x=140,y=280,width=70,height=60)
NUM_16 = tk.Button(master=window,text='+',font='Calibri 20',command=lambda:write('+'),bg='Orange',activebackground='#B84406')
NUM_16.place(x=210,y=280,width=70,height=60)

NUM_17 = tk.Button(master=window,text='0',font='Calibri 20',command=lambda:write('0'),background='#202020',foreground='white')
NUM_17.place(x=0,y=340,width=140,height=100)
NUM_19 = tk.Button(master=window,text='.',font='Calibri 20',command=lambda:write('.'),background='#202020',foreground='white')
NUM_19.place(x=140,y=340,width=70,height=100)
NUM_20 = tk.Button(master=window,text='=',font='Calibri 20',command=equal,bg='Orange',activebackground='#B84406')
NUM_20.place(x=210,y=340,width=70,height=100)

window.mainloop()