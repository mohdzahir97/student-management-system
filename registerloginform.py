from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msgbox
import mysql.connector
class registerloginuser(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600+0+0")
        self.title("zahir")
        self.config(bg="white")



        framebackground=Frame(self,bg="purple",bd=5)
        framebackground.place(x=350,y=0,relheight=600,relwidth=600)

        frameregister = Frame(framebackground, bg="grey", bd=5)
        frameregister.place(x=100, y=126, height=400,width=700)
        #**********************Register Widget******************
        lbl_register=Label(frameregister,text="REGISTER HERE",font="cosmicsansms 13 bold",bg="grey")
        lbl_register.grid(row=0,column=0)

        lbl_fname=Label(frameregister,text="First Name",font="cosmicsansms 16 bold",bg="grey")
        lbl_fname.grid(row=1,column=0,padx=5,pady=20,sticky="w")
        self.txtfnamevar=StringVar()
        txt_fname=Entry(frameregister,textvariable=self.txtfnamevar,font="cosmicsansms 10 bold",bd=3)
        txt_fname.grid(row=1,column=1,padx=10,pady=20,sticky="w")

        lbl_fname=Label(frameregister,text="Last Name",font="cosmicsansms 16 bold",bg="grey")
        lbl_fname.grid(row=1,column=2,padx=5,pady=20,sticky="w")
        self.txtlnamevar=StringVar()
        txt_lname=Entry(frameregister,textvariable=self.txtlnamevar,font="cosmicsansms 10 bold",bd=3)
        txt_lname.grid(row=1,column=3,padx=10,pady=20,sticky="w")

        lbl_contact=Label(frameregister,text="Contact No",font="cosmicsansms 16 bold",bg="grey")
        lbl_contact.grid(row=2,column=0,padx=5,pady=10,sticky="w")
        self.txtcontactvar=StringVar()
        txt_contact=Entry(frameregister,textvariable=self.txtcontactvar,font="cosmicsansms 10 bold",bd=3)
        txt_contact.grid(row=2,column=1,padx=10,pady=10,sticky="w")

        lbl_emailid=Label(frameregister,text="Email ID",font="cosmicsansms 16 bold",bg="grey")
        lbl_emailid.grid(row=2,column=2,padx=5,pady=10,sticky="w")
        self.emailidvar=StringVar()
        txt_emailid=Entry(frameregister,textvariable=self.emailidvar,font="cosmicsansms 10 bold",bd=3)
        txt_emailid.grid(row=2,column=3,padx=10,pady=10,sticky="w")


        lbl_question_combo=Label(frameregister,text="Question",font="cosmicsansms 16 bold",bg="grey")
        lbl_question_combo.grid(row=3,column=0,padx=5,pady=10,sticky="w")
        self.txtquestionvar=StringVar()
        self.txtquestion=ttk.Combobox(frameregister,textvariable=self.txtquestionvar,justify="center",state="readonly",font=("times new roman", 9))
        self.txtquestion['values']=("Your Best Friend Name?","Your Best Pet Name?","Your Birth Place Name?")
        self.txtquestion.grid(row=3,column=1,padx=1,pady=10)

        lbl_answer=Label(frameregister,text="Answer",font="cosmicsansms 16 bold",bg="grey")
        lbl_answer.grid(row=3,column=2,padx=5,pady=10,sticky="w")
        self.answervar=StringVar()
        self.txt_answer=Entry(frameregister,textvariable=self.answervar,font="cosmicsansms 10 bold",bd=3)
        self.txt_answer.grid(row=3,column=3,padx=10,pady=10,sticky="w")


        lbl_pass=Label(frameregister,text="Password",font="cosmicsansms 16 bold",bg="grey")
        lbl_pass.grid(row=4,column=0,padx=5,pady=20,sticky="w")
        self.txtpassvar=StringVar()
        self.txt_pass=Entry(frameregister,textvariable=self.txtpassvar,font="cosmicsansms 10 bold",bd=3)
        self.txt_pass.grid(row=4,column=1,padx=10,pady=20,sticky="w")

        lbl_conpass=Label(frameregister,text="Confirm Password",font="cosmicsansms 16 bold",bg="grey")
        lbl_conpass.grid(row=4,column=2,padx=5,pady=20,sticky="w")
        self.txtconpassvar=StringVar()
        self.txt_conpass=Entry(frameregister,textvariable=self.txtconpassvar,font="cosmicsansms 10 bold",bd=3)
        self.txt_conpass.grid(row=4,column=3,padx=10,pady=20,sticky="w")

        lbl_conpass=Label(frameregister,text="I Agree Terms And Conditions.",font="cosmicsansms 16 bold",bg="grey")
        lbl_conpass.grid(row=5,columnspan=2,padx=5,pady=20,sticky="w")
        self.txtcheckbutton=IntVar()
        self.agree_check=Checkbutton(frameregister,variable=self.txtcheckbutton,bg="grey")
        self.agree_check.grid(row=5,column=2,sticky="w")

        btn_register=Button(frameregister,text="Register",font="cosmicsansms 16 bold",bg="green",fg="white",command=self.registerlogindata)
        btn_register.grid(row=6,column=0)


        frameregisterlogo = Frame(self, bg="red", bd=5)
        frameregisterlogo.place(x=50, y=130, height=400,width=405)

        lbl_signin=Label(frameregisterlogo,text="Click on Sign In Button For Sign In.",bd=3,font="cosmicsansms 16 bold",bg="red",fg="white")
        lbl_signin.place(x=25,y=120,width=350,height=30)


        btn_register=Button(frameregisterlogo,text="Sign In",font="cosmicsansms 16 bold",bg="green",fg="white",command=self.signin_fun)
        btn_register.place(x=145,y=170,width=100,height=35)

    def registerlogindata(self):
        if self.txtfnamevar.get()=="" or self.txtcontactvar.get()=="" or self.emailidvar.get()=="" or self.txtquestionvar.get()=="" or self.answervar.get()=="" or self.txtpassvar.get()=="" or self.txtconpassvar.get()=="":
            msgbox.showerror("Error","All Fields Are Required.")
        elif self.txtconpassvar.get()!=self.txtpassvar.get():
            msgbox.showerror("Error","You Entered Password And Confirm Password Does Not Match.")
        elif self.txtcheckbutton.get()==0:
            msgbox.showerror("Error","Please Agree Our Terms And Condtions.")
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="",database="student_m_s")
                cur=con.cursor()
                cur.execute("select * from register_for_login where email=%s",(self.emailidvar.get(),))
                row_email=cur.fetchone()
                if row_email==None:
                    cur.execute("insert into register_for_login(fname,lname,contact,email,question,answer,password,cpassword)values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.txtfnamevar.get(),
                                 self.txtlnamevar.get(),
                                 self.txtcontactvar.get(),
                                 self.emailidvar.get(),
                                 self.txtquestionvar.get(),
                                 self.answervar.get(),
                                 self.txtpassvar.get(),
                                 self.txtconpassvar.get()
                                 ))
                    con.commit()
                    cur.close()
                    con.close()
                    msgbox.showinfo("Success","SuccessFully Register")
                    self.clear_data()
                else:
                    msgbox.showerror("Error", "You Entered Email Already Register.")
            except Exception as e:
                msgbox.showerror("Error",f"Error Occurs Due To This Error{e}.")

    def signin_fun(self):
        self.destroy()
        import loginwindowform
    def clear_data(self):
        self.txtfnamevar.set("")
        self.txtlnamevar.set("")
        self.txtcontactvar.set("")
        self.emailidvar.set("")
        self.txtquestionvar.set("")
        self.answervar.set("")
        self.txtpassvar.set("")
        self.txtconpassvar.set("")
        self.txtcheckbutton.set(0)









objroot=registerloginuser()
objroot.mainloop()