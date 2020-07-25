from tkinter import *
from tkinter.messagebox import *
import math as m

from audio_helper import play_audio

import threading

ob = play_audio()

# some useful variables
font = ('Verdana', 19, 'bold')


# functions
def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)

    #calling voice object class(its only class: ob.speak(text))

    #calling object by using threading method
    t = threading.Thread(target=ob.speak, args=(text,))
    t.start()

    if text == 'x':
        text_field.insert(END, "*")
        return

    if text == '=':
        try:
            ex = text_field.get()
            answer = eval(ex)
            text_field.delete(0, END)
            text_field.insert(0, answer)
        except Exception as e:
            print("Error!", e)
            showerror("Error!", e)
        return

    text_field.insert(END, text)


def all_clear():
    ac = text_field.delete(0, END)
    t = threading.Thread(target=ob.speak, args=(ac))
    t.start()


def clear():
    ex = text_field.get()
    ex = ex[0:len(ex) - 1]
    text_field.delete(0, END)
    text_field.insert(0, ex)


# creating window
window = Tk()
window.title('Calculator')
window.geometry('430x510+400+30')

# picture label
pic = PhotoImage(file='image/calcpng1.png')
headingLabel = Label(window, image=pic, )
headingLabel.pack(side=TOP, pady=10)

# heading label
heading = Label(window, text='Calculator', font=font)
heading.pack(side=TOP)

# textfile
text_field = Entry(window, font=font, justify=CENTER)
text_field.pack(side=TOP, pady=10, fill=X, padx=10)

# button
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP, padx=10)

# adding button
temp = 1
for i in range(0, 4):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='orange',
                     activeforeground='white', bg="#ccccff", border=0)
        btn.grid(row=i, column=j, padx=3, pady=3)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white', bg="#ccccff", border=0)
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white', bg="#ccccff", border=0)
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame, text='=', font=font, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white', bg="#ccccff", border=0)
equalBtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white', bg="#ccccff", border=0)
plusBtn.grid(row=0, column=3)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white', bg="#ccccff", border=0)
minusBtn.grid(row=1, column=3)

multBtn = Button(buttonFrame, text='x', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white', bg="#ccccff", border=0)
multBtn.grid(row=2, column=3)

divBtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white', bg="#ccccff", border=0)
divBtn.grid(row=3, column=3)

clearBtn = Button(buttonFrame, text='<-', font=font, width=11, relief='ridge', activebackground='orange',
                  activeforeground='white', bg="#ccccff", border=0, command=clear, )
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text='AC', font=font, width=11, relief='ridge', activebackground='orange',
                     activeforeground='white', bg="#ccccff", border=0, command=all_clear, )
allClearBtn.grid(row=4, column=2, columnspan=2)

# binding all other buttons
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)


#### adding the function while pressing the enter key ####
def enterClick(event):
    print('enter key pressed')
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)

text_field.bind('<Return>', enterClick)
#### ^^adding the function for enter key^^ ####


#######Scientific mode creation##########

# buttons for scientific mode

scFrame = Frame(window)

sqrtBtn = Button(scFrame, text='√', font=font, width=6, relief='ridge', activebackground='orange',
                 activeforeground='white', bg="#ccccff", border=0, )
sqrtBtn.grid(row=0, column=0)

pwrBtn = Button(scFrame, text='^', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white', bg="#ccccff", border=0, )
pwrBtn.grid(row=0, column=1)

factBtn = Button(scFrame, text='x!', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white', bg="#ccccff", border=0, )
factBtn.grid(row=0, column=2)

radBtn = Button(scFrame, text='rad', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white', bg="#ccccff", border=0, )
radBtn.grid(row=0, column=3)

degBtn = Button(scFrame, text='deg', font=font, width=6, relief='ridge', activebackground='orange',
                activeforeground='white', bg="#ccccff", border=0, )
degBtn.grid(row=1, column=0)

sinBtn = Button(scFrame, text='sinθ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white', bg="#ccccff", border=0, )
sinBtn.grid(row=1, column=1)

cosBtn = Button(scFrame, text='cosθ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white', bg="#ccccff", border=0, )
cosBtn.grid(row=1, column=2)

tanBtn = Button(scFrame, text='tanθ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white', bg="#ccccff", border=0, )
tanBtn.grid(row=1, column=3)

# functions for scientific calculations

simplecalc = True


def sc_click():
    global simplecalc

    if simplecalc:
        # sc...
        buttonFrame.pack_forget()
        # add sc frame
        scFrame.pack(side=TOP, pady=10)
        buttonFrame.pack(side=TOP)
        window.geometry('430x625+400+30')

        print("show scientific")
        simplecalc = False
    else:
        scFrame.pack_forget()
        window.geometry('430x510+400+30')
        print("show simple")
        simplecalc = True


def calculation_sc(event):
    print("sc btn clicked")
    btn = event.widget
    text = btn['text']
    print(text)

    answer = ''
    ex = text_field.get()

    if text == '√':
        answer = str(m.sqrt(float(ex)))
        print("cal sqrt")
    elif text == '^':
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))
        print("cal power")
    elif text == 'x!':
        answer = str(m.factorial(int(ex)))
        print("cal factorial")
    elif text == 'rad':
        answer = str(m.radians(float(ex)))
        print("cal power")
    elif text == 'deg':
        answer = str(m.degrees(float(ex)))
        print("cal power")
    elif text == 'sinθ':
        answer = str(m.sin(float(ex)))
        print("cal sin")
    elif text == 'cosθ':
        answer = str(m.cos(float(ex)))
        print("cal cos")
    elif text == 'tanθ':
        answer = str(m.tan(float(ex)))
        print("cal tan")

    text_field.delete(0, END)
    text_field.insert(0, answer)


# end functions

# binding scientific buttons

sqrtBtn.bind("<Button-1>", calculation_sc)
pwrBtn.bind("<Button-1>", calculation_sc)
factBtn.bind("<Button-1>", calculation_sc)
radBtn.bind("<Button-1>", calculation_sc)
degBtn.bind("<Button-1>", calculation_sc)
sinBtn.bind("<Button-1>", calculation_sc)
cosBtn.bind("<Button-1>", calculation_sc)
tanBtn.bind("<Button-1>", calculation_sc)

font_menu = ('', 15)

menubar = Menu(window)
mode = Menu(menubar, font=font_menu, tearoff=0, )
mode.add_checkbutton(label="Scientific Calculator", command=sc_click, )
menubar.add_cascade(label="Mode", menu=mode)

window.config(menu=menubar)

window.mainloop()

