from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3

def Application(root):
    
    root.geometry('{}x{}'.format(700, 600)) # 700 x 600 window
    root.resizable(width=False, height=False) # disabling maximize button
    root.title('PDF to Audio')
    root.configure(background='light grey')
    global rate, male, female

    frame1 = Frame(root, width=500, height=200, bg='indigo')
    frame2 = Frame(root, width=500, height=450, bg='light grey')
    frame1.pack(side='top', fill='both')
    frame2.pack(side='top', fill='y')
    
    

    #frame1 widgets
    name1 = Label(frame1, text='PDF to AUDIO', fg='black', bg='blue', font=('Arial 28 bold'))
    name1.pack()
    name2 = Label(frame1, text='Hear your PDF File', fg='red', bg='indigo', font=('Calibri 25 bold'))
    name2.pack()

    #frame2 widgets (btns, checkboxes)
    btn = Button(frame2, text='Select PDF File', activeforeground='red', \
         padx=70, pady='10', fg='white', bg='black', font=('Arial 12 bold')) # command=extract_text(),
    btn.grid(row=0, pady=20, columnspan=2)
    
    rate_text = Label(frame2, text='Enter Rate of Speech', fg='black', bg='aqua',\
        font=('Arial 12'))
    rate_text.grid(row=1, column=0, pady=15, padx=0, sticky=W)

    rate = Entry(frame2, text='200', fg='black', bg='white', font=('Arial 12'))
    rate.grid(row=1, column=1, padx=30, pady=15, sticky=W)


    mainloop()


if __name__ == '__main__':
    window = Tk()
    Application(window)
    