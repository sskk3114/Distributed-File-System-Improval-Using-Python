from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import localSupport,globalSupport,threading, os, shutil

def show_entry_fields():
	print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
	
def select_folder_1():
	filename = filedialog.askdirectory()
	e1.delete(0,END)
	e1.insert(0,filename)
	
def select_folder_2():
	filename = filedialog.askdirectory()
	e2.delete(0,END)
	e2.insert(0,filename)	

def local_support():

	if os.path.exists('temp'):
		shutil.rmtree('temp')
		for x in range(0,10):
			os.makedirs('temp/R'+str(x)+'_temp/FrequentPatterns')

	elif not os.path.exists('temp'):
		for x in range(0,10):
			os.makedirs('temp/R'+str(x)+'_temp/FrequentPatterns')

	var.set("Creating Local Patterns...")
	localSupport.freq_patterns(e1.get(),e2.get())
	
def global_support():

	if os.path.exists('temp_global'):
		shutil.rmtree('temp_global')
		for x in range(0,10):
			os.makedirs('temp_global/R'+str(x)+'_temp/FrequentPatterns')

	elif not os.path.exists('temp_global'):
		for x in range(0,10):
			os.makedirs('temp_global/R'+str(x)+'_temp/FrequentPatterns')

	var.set("Global patterns")
	globalSupport.freq_patterns(e1.get(),e2.get())


window=Tk()

window.geometry("400x140")
window.resizable(False, False)
window.title("Project zero")

Label(window, text="Input folder").grid(row=0)
Label(window, text="Output folder").grid(row=1)

e1 = Entry(window,width=48)
e2 = Entry(window,width=48)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#Button(window, text='Quit', command=window.quit).grid(row=4, column=3, sticky=W, pady=4)
Button(window, text='...', command=select_folder_1).grid(row=0, column=3, sticky=W, pady=4)
Button(window, text='...', command=select_folder_2).grid(row=1, column=3, sticky=W, pady=4)
Button(window, text='Global patterns', command=global_support,width=15).place(x = 225,y = 75)
Button(window, text='Local patterns', command=local_support,width=15).place(x = 50,y = 75)

var = StringVar()
label = Label( window, textvariable = var).place(x = 0,y = 110)

window.mainloop()
