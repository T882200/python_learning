import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

'''
root = Tk()

root.title("First GUI")

ttk.Button(root, text="Hello TkInter").grid()

root.mainloop()
'''

'''
root = Tk()

frame = Frame(root)

lableText = StringVar()

lable = Label(frame, textvariable=lableText)

button = Button(frame, text="Click me")

lableText.set("I am a lable")

lable.pack()

button.pack()

frame.pack()

root.mainloop()
'''

'''
root = Tk()

frame = Frame(root)

Label(frame, text="A Bunch of Buttons").pack()

Button(frame, text="B1").pack(side=LEFT, fill=Y)
Button(frame, text="B2").pack(side=TOP, fill=X)
Button(frame, text="B3").pack(side=RIGHT, fill=X)
Button(frame, text="B4").pack(side=LEFT, fill=X)

frame.pack()

root.mainloop()
'''
'''
root = Tk()

Label(root, text="First Name").grid(row=0, sticky=W, padx=4)
Entry(root).grid(row=0, column=1, sticky=E, pady=4)

Label(root, text="Last Name").grid(row=1, sticky=W, padx=4)
Entry(root).grid(row=1, column=1, sticky=E, pady=4)

Button(root, text="Submit").grid(row=3)

root.mainloop()
'''
'''
root = Tk()

Label(root, text="Description").grid(row=0, column=0, sticky=W)
Entry(root, width=50).grid(row=0, column=1)
Button(root, text="Submit").grid(row=0, column=8)

Label(root, text="Quality").grid(row=1, column=0, sticky=W)
Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)



Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)
root.mainloop()
'''

'''
def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum = num1 + num2
    sumEntry.delete(0, "end")
    sumEntry.insert(0, sum)

root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()
'''

'''
def get_data(event):

    print("String :", strVar.get())
    print("Integer :", intVar.get())
    print("Double :", dblVar.get())
    print("Boolean :", boolVar.get())

def bind_button(event):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>", get_data)


root = Tk()

strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

strVar.set("Enter String")
intVar.set("Enter Integer")
dblVar.set("Enter Double")
boolVar.set(True)

strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)


theCheckBut = Checkbutton(root, text="Switch", variable=boolVar)
theCheckBut.bind("<Button-1>", bind_button)
theCheckBut.pack(side=LEFT)

getDataButton = Button(root, text="Get Data")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side=LEFT)

root.mainloop()
'''
'''
def open_msg_box():
    messagebox.showwarning(
    "Event Triggered",
    "Button Clicked"
    )

root = Tk()


root.geometry("400x400+300+300")

root.resizable(width=False, height=False)

frame = Frame(root)

style = ttk.Style()

style.configure("TButton",
                foreground="midnight blue",
                font="Times 20 bold italic",
                padding=20)

print(ttk.Style().theme_names())

print(style.lookup("TButton", "font"))
print(style.lookup("TButton", "foreground"))
print(style.lookup("TButton", "padding"))

ttk.Style().theme_use('clam')

theButton = ttk.Button(frame,
                       text="Important Button",
                       command=open_msg_box)

theButton['state'] = 'disabled'
theButton['state'] = 'normal'

theButton.pack()

frame.pack()

root.mainloop()
'''

def quit_app():
    root.quit()

def show_about(event=None):
    messagebox.showwarning(
        "About",
        "This Awesome Program was Made in 2016"
    )

root = Tk()

the_menu = Menu(root)

#File
file_menu = Menu(the_menu, tearoff=0)

file_menu.add_command(label="Open")

file_menu.add_command(label="Save")

file_menu.add_separator()

file_menu.add_command(label="Quit", command=quit_app)

the_menu.add_cascade(label="File", menu=file_menu)

#Font

text_font = StringVar()
text_font.set("Times")

def change_font(event=None):
    print("Font Picked :", text_font.get())

font_menu = Menu(the_menu, tearoff=0)

font_menu.add_radiobutton(label="Times",
                        variable=text_font,
                        command=change_font)

font_menu.add_radiobutton(label="Courier",
                        variable=text_font,
                        command=change_font)

font_menu.add_radiobutton(label="Ariel",
                        variable=text_font,
                        command=change_font)



#View

view_menu = Menu(the_menu, tearoff=0)

line_numbers = IntVar()

line_numbers.set(1)

view_menu.add_checkbutton(label="Line Numbers",
                          variable=line_numbers)

view_menu.add_cascade(label="Fonts", menu=font_menu)

the_menu.add_cascade(label="View", menu=view_menu)


#Help

help_menu = Menu(the_menu, tearoff=0)
help_menu.add_command(label="About",
                    accelerator="command-H",
                    command=show_about)

the_menu.add_cascade(label="Help", menu=help_menu)

root.bind("<Command-A>", show_about)
root.bind("<Command-a>", show_about)
root.config(menu=the_menu)

root.mainloop()





















