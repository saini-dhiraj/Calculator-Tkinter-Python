import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Calculator")   #Heading

heading_label = tk.Label(mainWindow, text="Enter first Number",padx=20,pady=10)
heading_label.pack()  # linear layout

name_field1 = tk.Entry(mainWindow)
name_field1.pack()


heading_label = tk.Label(mainWindow, text="Enter second Number",padx=20,pady=10)
heading_label.pack()  # linear layout

name_field2 = tk.Entry(mainWindow)
name_field2.pack()


heading_label = tk.Label(mainWindow, text="Operations",padx=20,pady=10)
heading_label.pack()  # linear layout

button = tk.Button(mainWindow,text="+",command= lambda: add(),padx=20,pady=10)
button.pack()

button = tk.Button(mainWindow,text="-",command= lambda: minus(),padx=20,pady=10)
button.pack()

button = tk.Button(mainWindow,text="*",command= lambda: mul(),padx=20,pady=10)
button.pack()

button = tk.Button(mainWindow,text="/",command= lambda: div(),padx=20,pady=10)
button.pack()

result_label = tk.Label(mainWindow, text="",padx=20,pady=10)
result_label.pack()

def add():
    value1 = int(name_field1.get())
    value2 = int(name_field2.get())
    result = value1+value2
    result_label.config(text="Result:"+str(result))
    #print(value1+value2)
def minus():
    value1 = int(name_field1.get())
    value2 = int(name_field2.get())
    result = value1 - value2
    result_label.config(text="Result:" + str(result))
    #print(value1 - value2)
def mul():
    value1 = int(name_field1.get())
    value2 = int(name_field2.get())
    result = value1 * value2
    result_label.config(text="Result:" + str(result))
    #print(value1 * value2)
def div():
    value1 = int(name_field1.get())
    value2 = int(name_field2.get())
    result = value1 / value2
    result_label.config(text="Result: " + str(result))
    #print(value1 / value2)


mainWindow.mainloop()
