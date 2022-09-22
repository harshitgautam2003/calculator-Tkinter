from tkinter import *
wind=Tk()
wind.geometry('400x660')
wind.title('Calculator')

lbl=Label(wind,text='Calculator',font=('Arial Black',36),fg='#228844')
lbl.pack()
exp=Text(wind, height=1, width=13,font=('Comic Sans Ms',36))
exp.pack()
exp.focus()
def eqbut():
    res=eval(exp.get('1.0',END))
    exp.delete('1.0',END)
    exp.insert(END,res)
    
keypad=Frame(wind)
keypad.pack(side=BOTTOM)

lefbut=Frame(keypad,padx=2,pady=2)
lefbut.pack(side=LEFT)

opkey=Frame(keypad,padx=2,pady=2)
opkey.pack(side=RIGHT)

rigbut=Frame(keypad,padx=2,pady=2)
rigbut.pack(side=RIGHT)

cenbut=Frame(keypad,padx=2,pady=2)
cenbut.pack()

nichkey=Frame(keypad)
nichkey.pack(side=BOTTOM)

im1=PhotoImage(file='1.png')
im2=PhotoImage(file='2.png')
im3=PhotoImage(file='3.png')
im4=PhotoImage(file='4.png')
im5=PhotoImage(file='5.png')
im6=PhotoImage(file='6.png')
im7=PhotoImage(file='7.png')
im8=PhotoImage(file='8.png')
im9=PhotoImage(file='9.png')
im0=PhotoImage(file='0.png')
impl=PhotoImage(file='pl.png')
immi=PhotoImage(file='mi.png')
immu=PhotoImage(file='mu.png')
imdi=PhotoImage(file='di.png')
imba=PhotoImage(file='ba.png')
imcl=PhotoImage(file='cl.png')
imeq=PhotoImage(file='eq.png')
    
bpl=Button(lefbut,image=impl,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'+'))
bpl.pack(side=TOP)

bmi=Button(cenbut,image=immi,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'-'))
bmi.pack(side=TOP)

bmu=Button(rigbut,image=immu,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'*'))
bmu.pack(side=TOP)           

bba=Button(lefbut,image=imba,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.delete('end-2c',END))
bba.pack(side=BOTTOM)

bcl=Button(rigbut,image=imcl,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.delete('1.0',END))
bcl.pack(side=BOTTOM)

b1=Button(lefbut,image=im1,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'1'))
b1.pack(side=TOP)

b4=Button(lefbut,image=im4,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'4'))
b4.pack()

b7=Button(lefbut,image=im7,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'7'))
b7.pack(side=BOTTOM)

b2=Button(cenbut,image=im2,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'2'))
b2.pack(side=TOP)

b3=Button(rigbut,image=im3,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'3'))
b3.pack(side=TOP)

b5=Button(cenbut,image=im5,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'5'))
b5.pack(side=TOP)

b0=Button(cenbut,image=im0,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'0'))
b0.pack(side=BOTTOM)

b8=Button(cenbut,image=im8,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'8'))
b8.pack(side=BOTTOM)

b6=Button(rigbut,image=im6,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'6'))
b6.pack()

b9=Button(rigbut,image=im9,border=0,height=90,width=90,bg='#eeeeee',command=lambda:exp.insert(INSERT,'9'))
b9.pack()
 




bdi=Button(opkey,image=imdi,border=0,height=230,width=100,bg='#eeeeee',command=lambda:exp.insert(INSERT,'/'))
bdi.pack(side=TOP)

beq=Button(opkey,image=imeq,border=0,height=230,width=100,bg='#eeeeee',command=eqbut)
beq.pack(side=BOTTOM)  

wind.mainloop() 
