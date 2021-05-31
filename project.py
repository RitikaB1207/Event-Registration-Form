import tkinter as tk
from tkinter import *
import mail






from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import sqlite3
import smtplib

# datetime object containing current date and time
now = datetime.now()
print("now =", now)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)




win = Tk()
win.geometry("500x500+100+100")
win.title("EVENT REGISTRATION FORM")
#win.config(background='grey')
#bg = PhotoImage("event1.jpg")
gender = IntVar()
agree = IntVar()
email=StringVar()
fname= StringVar()
lname=StringVar()
age= StringVar()
contact=StringVar()
category=StringVar()
event=StringVar()
event1=['Cultural','Sport','Academic']
Cultural =['singing competition','Dancing competition','Drawing competition','Mehendi competition','Drama Competition']
Sport = ['Cricket','Volleyball','Badminton','Football','Tennis']
Academic = ['Microprocessor quiz','Current affair quiz','Coding quiz']


def pick_event(e) :
    if category_event.get()  == 'Cultural':
        event_Sel.config(value=Cultural)
        event_Sel.current()
    if category_event.get() == 'Sport':
        event_Sel.config(value=Sport)
        event_Sel.current()
    if category_event.get() == 'Academic':
        event_Sel.config(value=Academic)
        event_Sel.current()

def checkcont(con):
    if con.isdigit():
        return True
    if len(str(con==0)):
        return True

    else:
        messagebox.showwarning("Invalid", " Invalid Entry")
        return False


def reset():
    firstname.delete(0, END)
    gender.set(0)
    lastname.delete(0, END)
    contact.delete(0, END)
    email.set(0)
    Age.delete(0, END)
    category_event.set(0)
    event_Sel.set(0)

#email validation
import re
def validateEmail(email):
    return re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$',email)



def on_press():
    firstname_entry = fname.get()
    lastname_entry = lname.get()
    contact_entry = contact.get()
    emailid = email.get()
    gender_entry = gender.get()
    category_entry = category.get()
    event_entry = event.get()
    age_entry = age.get()
    if firstname.get()=='':
        messagebox.showwarning('Error','please enter firstname')
    elif lname.get() == '':
        messagebox.showwarning('Error', 'please enter lastname')
    elif contact.get() == ''or len(contact.get()) !=10 :
        messagebox.showwarning('Error','please enter contact')
    elif email.get() == '' :
        messagebox.showwarning('Error','please enter Email')
    elif age.get()=='':
        messagebox.showwarning('Error','please enter Age')
    elif gender.get() == 0:
        messagebox.showwarning('Error','please enter gender')
    elif category.get()=='':
        messagebox.showwarning('Error','please enter category_event')
    elif event.get()=='':
        messagebox.showwarning('Error','please enter event_Sel')
    elif agree.get()==0:
        messagebox.showwarning('Error','please agree to the terms and conditions')

    if validateEmail(emailid):

        if firstname_entry==''or lastname_entry==''or contact_entry==''or emailid==''or gender_entry==''or age_entry==''or category_entry=='' or event_entry=='':
            messagebox.showwarning('something went wrong','please enter all the details')


        else:
            conn = sqlite3.connect('form.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS '
                               'signup(Email TEXT PRIMARY KEY,'
                               'FirstName TEXT,'
                               'LastName TEXT,'
                               'Contact INTEGER,'
                               'Gender INTEGER,'
                               'Age INTEGER,'
                               'CategoryofEvent TEXT,'
                               'Event TEXT)')
                cursor.execute('INSERT INTO signup(Email,FirstName,LastName,Contact,Gender,Age,CategoryofEvent,Event)'
                               ' VALUES(?,?,?,?,?,?,?,?)',(emailid,firstname_entry,lastname_entry,contact_entry,gender_entry,age_entry,category_entry,event_entry))
                conn.commit()
                messagebox.showwarning('Registered Successfully', 'Your data has been recorded')
                receiver = email.get()
                message = "Subject: Registered Event Details" + '\n' + "Hello ," + '\n' + (str(firstname_entry.capitalize()) + '' + str(lastname_entry.capitalize())) + '\n' + 'Participated Event:' + str(category_entry.capitalize()) + '-' + str(event_entry.capitalize()) + '\n' + 'Date of the Event: 28th Feb,2021' + '\n' + 'Venue:Datta Meghe College of Engineering,Auditorium' + '\n' + "Thankyou"
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(mail.sender, mail.password)
                s.sendmail(mail.sender, receiver, message)
                s.quit()

                #messagebox.showwarning('Registered Successfully','Your data has been recorded')
                #conn.close()
    else:
        messagebox.showwarning('email not valid!','enter valid email')


    #new
    final = StringVar()

def query():
        conn = sqlite3.connect('form.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM signup')
            result = cursor.fetchall()
            final = ''
            for tup in result:
                final += str(tup)
                final += '\n'
            txtbox.insert(END, final)
        conn.commit()




label9 =Label(win,text="REGISTRATION FORM",fg='black',font='Times 16')
label9.place(x=380,y=25)

label1 =Label(win,text="Firstname:",fg='black',font='Times 16' )
label1.place(x=5,y=100)
firstname = Entry(win, width=25,textvariable=fname,font='Times 16')
firstname.place(x=120, y=100)
label2 = Label(win, text="Lastname:", fg='black',font='Times 16')
label2.place(x=580, y=100)
lastname = Entry(win, width=25,textvariable=lname,font='Times 16')
lastname.place(x=740, y=100)
label4 = Label(win, text="Email:", fg='black',font='Times 16')
label4.place(x=580, y=200)
email_entry = Entry(win, width=25,textvariable=email,font='Times 16')
email_entry.place(x=740, y=200)

label3 = Label(win, text="Contact:", fg='black',font='Times 16')
label3.place(x=5, y=200)
contact= Entry(win,textvariable=contact,width=25,font='Times 16')
contact.place(x=120,y=200)
validate_contact = win.register(checkcont)
contact.config(validate='key', validatecommand=(validate_contact, '%P'))



label5 = Label(win, text='',font='Times 16')
label5.pack()
label5 = Label(win, text='Gender',font='Times 16')
label5.place(x=5, y=300)
male_gender = Radiobutton(win, text='Male', variable=gender, value=1,font='Times 16')
male_gender.place(x=80, y=300)
female_gender = Radiobutton(win, text='Female', variable=gender, value=2,font='Times 16')
female_gender.place(x=155, y=300)
other_gender = Radiobutton(win, text='Other', variable=gender, value=3,font='Times 16')
other_gender.place(x=250, y=300)
label6 = Label(win, text="Age:", fg='black',font='Times 16')
label6.place(x=580, y=300)
Age = Entry(win, width=25,textvariable=age,font='Times 16')
Age.place(x=740,y=300)
categoryofevent = Label(win, text='Select the category of event:', fg='darkred',font='Times 16')
categoryofevent.place(x=5,y=400)
category_event= ttk.Combobox(win, width=20,font='Times 16',value=event1,textvariable=category)
category_event.place(x=249,y=400)
category_event.current()
category_event.bind("<<ComboboxSelected>>",pick_event)

event_Sel=Label(win ,text='Select event:' ,fg='darkred',font='Times 16')
event_Sel.place(x=580,y=400)
event_Sel= ttk.Combobox(win,width=20,font='Times 16',value='',textvariable=event)
event_Sel.place(x=740,y=400)

Event = Label(win,text='Agree to the terms and conditions', width=30)
Event.place(x=400, y=500)
agree_button = Checkbutton(win, variable=agree, onvalue=1, offvalue=0)
agree_button.place(x=390,y=500)

Register_button = Button(win, text='Register', width=25, fg='white', bg='blue', command=on_press)
Register_button.place(x=350,y=550)
Reset_button = Button(win, text='Reset', width=25, fg='white', bg='darkred', command=reset)
Reset_button.place(x=580,y=550)

def clear():
    txtbox.delete(1.0,END)

#for textbox
txtbox =Text(win,width=69,height=80)
txtbox.place(x=50,y=640)
View_all_entry_button = Button(win, text='VIEW ALL ENTRY', width=20, fg='white', bg='blue', command=query)
View_all_entry_button.place(x=700,y=650)
Clear_button = Button(win, text='Clear', width=20, fg='white', bg='darkred', command=clear)
Clear_button.place(x=700,y=690)

#for displaying time
def display_time():
    t = datetime.now()
    dt = t.strftime('%d %B %H:%M:%S')
    label10['text'] = dt
    win.after(1000,display_time)

#Function for displaying time
label10 = Label(win,bg="black",fg='white',font='Times 16')
label10.place(x=50, y=590)
display_time()

win.mainloop()