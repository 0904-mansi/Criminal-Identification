
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk
import PIL.Image
from tkinter import Tk, Toplevel, Button
import pymysql

# def mainfunction():
#       global bgg, pimg, label
def clear():
      userentry.delete(0,END)
      passentry.delete(0,END)

def close():
      win.destroy()	


def login():
      if user_name.get()=="" or password.get()=="":
            messagebox.showerror("Error","Enter username and password",parent=win)	
      else:
            try:
                  con = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
                  cur = con.cursor()

                  cur.execute("select * from user_information where username=%s and password = %s",(user_name.get(),password.get()))
                  row = cur.fetchone()

                  if row==None:
                        messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

                  else:
                        messagebox.showinfo("Success" , "Successfully Login" , parent = win)
                        close()
                        

                  con.close()
            except Exception as es:
                  messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)






#----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
      # signup database connect 
      def action():
            if first_name.get()=="" or last_name.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
                  messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
            elif password.get() != very_pass.get():
                  messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
            else:
                  try:
                        con = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
                        cur = con.cursor()
                        cur.execute("select * from user_information where username=%s",user_name.get())
                        row = cur.fetchone()
                        if row!=None:
                              messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
                        else:
                              cur.execute("insert into user_information(first_name,last_name,gender,username,password) values(%s,%s,%s,%s,%s)",
                                    (
                                    first_name.get(),
                                    last_name.get(),
                                    var.get(),
                                    user_name.get(),
                                    password.get()
                                    ))
                              con.commit()
                              con.close()
                              messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
                              clear()
                              switch()
                        
                  except Exception as es:
                        messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = winsignup)

      # close signup function			
      def switch():
            winsignup.destroy()

      # clear data function
      def clear():
            first_name.delete(0,END)
            last_name.delete(0,END)
            var.set("Male")
            user_name.delete(0,END)
            password.delete(0,END)
            very_pass.delete(0,END)


      # start Signup Window	

      winsignup = Toplevel()
      winsignup.title("User Sign-Up")
      winsignup.maxsize(width=800 ,  height=600)
      winsignup.minsize(width=800 ,  height=600)
      bgg1 = PIL.Image.open("bg.png")
      bgg1 = bgg1.resize((1500, 900),PIL.Image.ANTIALIAS)
      pimg1 = ImageTk.PhotoImage(bgg1)
      label = tk.Label(winsignup,image=pimg1)
      label.place(x=0, y=0,width=1500, height=900)


      #heading label
      heading = Label(winsignup , text = "Sign-Up" , font = 'Verdana 20 bold')
      heading.place(x=80 , y=60)

      # form data label
      first_name = Label(winsignup, text= "First Name :" , font='Verdana 10 bold')
      first_name.place(x=80,y=130)

      last_name = Label(winsignup, text= "Last Name :" , font='Verdana 10 bold')
      last_name.place(x=80,y=160)

      Gender = Label(winsignup, text= "Gender :" , font='Verdana 10 bold')
      Gender.place(x=80,y=190)

      user_name = Label(winsignup, text= "User Name :" , font='Verdana 10 bold')
      user_name.place(x=80,y=250)

      password = Label(winsignup, text= "Password :" , font='Verdana 10 bold')
      password.place(x=80,y=280)

      very_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold')
      very_pass.place(x=80,y=310)

      # Entry Box ------------------------------------------------------------------

      first_name = StringVar()
      last_name = StringVar()
      var= StringVar()
      user_name = StringVar()
      password = StringVar()
      very_pass = StringVar()


      first_name = Entry(winsignup, width=40 , textvariable = first_name)
      first_name.place(x=200 , y=133)


      
      last_name = Entry(winsignup, width=40 , textvariable = last_name)
      last_name.place(x=200 , y=163)

      
      Radio_button_male = ttk.Radiobutton(winsignup,text='Male', value="Male", variable = var).place(x= 200 , y= 193)
      Radio_button_female = ttk.Radiobutton(winsignup,text='Female', value="Female", variable = var).place(x= 200 , y= 220)

      user_name = Entry(winsignup, width=40,textvariable = user_name)
      user_name.place(x=200 , y=250)

      
      password = Entry(winsignup, width=40, textvariable = password)
      password.place(x=200 , y=280)

      
      very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
      very_pass.place(x=200 , y=310)


      # button login and clear

      btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
      btn_signup.place(x=200, y=340)


      btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
      btn_login.place(x=280, y=340)


      sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
      sign_up_btn.place(x=350 , y =20)


      winsignup.mainloop()

      

#------------------------------------------------------------ Login Window -----------------------------------------

win = Tk()

# app title
win.title("User Login")

# window size
win.maxsize(width=800 ,  height=500)
win.minsize(width=800 ,  height=500)
bgg1 = PIL.Image.open("bg.png")
bgg1 = bgg1.resize((1500, 900),PIL.Image.ANTIALIAS)
pimg1 = ImageTk.PhotoImage(bgg1)
label = tk.Label(win,image=pimg1)
label.place(x=0, y=0,width=1500, height=900)


#heading label
heading = Label(win , text = "Login" , font = 'Verdana 25 bold')
heading.place(x=80 , y=150)

username = Label(win, text= "User Name :" , font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = Label(win, text= "Password :" , font='Verdana 10 bold')
userpass.place(x=80,y=260)

# Entry Box
user_name = StringVar()
password = StringVar()
      
userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=223)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=260)


# button login and clear

btn_login = Button(win, text = "Login" ,font='Verdana 10 bold',command = login)
btn_login.place(x=200, y=293)


btn_login = Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear)
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = Button(win , font='Verdana 10 bold',text="Switch To Sign up" , command = signup )
sign_up_btn.place(x=350 , y =20)



win.mainloop()

