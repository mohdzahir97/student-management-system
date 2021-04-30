from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as msgbox
class loginformwindow(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600+0+0")
        self.title("Login Form")

        f1 = Frame(self, bg="grey")
        f1.place(x=350, y=130, width=600, height=500)
        lbl_head = Label(f1, text="Admin Login Panel", bg="black", fg="white",font="cosmicsansms 20 bold", borderwidth=5, relief=SUNKEN)
        lbl_head.place(x=90,y=20,height=60,width=450)

        lbl_name_email = Label(f1, text="Email ID", borderwidth=5, relief=SUNKEN, padx=10, font="lucida 12 bold",bg="grey")
        lbl_name_email.place(x=90,y=100,height=40,width=200)
        lbl_pass = Label(f1, text="Password", padx=10, borderwidth=5, relief=SUNKEN, font="lucida 12 bold",bg="grey")
        lbl_pass.place(x=90,y=180,height=40,width=200)

        self.txtnameemailvar = StringVar()
        self.txtpassvar = StringVar()
        self.emailnameentry = Entry(f1, textvariable=self.txtnameemailvar, borderwidth=5, relief=SUNKEN, font="lucida 10 bold")
        self.passentry = Entry(f1, textvariable=self.txtpassvar, borderwidth=5, relief=SUNKEN, font="lucida 10 bold")
        self.emailnameentry.place(x=332,y=100,height=40,width=200)
        self.passentry.place(x=332,y=180,height=40,width=200)

        btnlogin = Button(f1, text="LOGIN", borderwidth=5, padx=10, font="lucida 10 bold",command=self.login_fun)
        btnlogin.place(x=90,y=260,height=40,width=200)

        btnforgotpass = Button(f1, text="Reset Passowrd", bg="grey",bd=0, padx=10, font="lucida 13 bold",command=self.forgotcreate_window)
        btnforgotpass.place(x=90,y=320,height=40,width=200)

        btn_cancel = Button(f1, text="Register", borderwidth=5, padx=10, font="cosmicsansms 10 bold",command=self.registerfirst)
        btn_cancel.place(x=332,y=260,height=40,width=200)


    def clear_reform(self):
        self.emailnameentry.delete(0,END)
        self.txtquestion.delete(0)
        self.txt_answer.delete(0,END)
        self.txt_newpass.delete(0,END)
    def changepass_fun(self):
        if self.txtquestionvar.get()=="" or self.answervar.get()=="" or self.newpassvar.get()=="":
            msgbox.showerror("Error", "All Fields Are Requireds..", parent=self.root2)
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="",database="student_m_s")
            cur=con.cursor()
            cur.execute("select * from register_for_login where email=%s AND question=%s AND answer=%s",
                        (self.txtnameemailvar.get(),
                         self.txtquestionvar.get(),
                         self.answervar.get()
                        ))
            row=cur.fetchone()
            if row==None:
                msgbox.showerror("Error", "Please Select Correct Secuirity Question/Answer.", parent=self.root2)
            else:
                cur.execute("update register_for_login set password=%s,cpassword=%s where email=%s",
                            (self.newpassvar.get(),
                             self.newpassvar.get(),
                             self.txtnameemailvar.get()
                            ))
                con.commit()
                cur.close()
                con.close()
                msgbox.showinfo("Success","Your Password Succesfully Reset...Please Login With New Password.",parent=self.root2)
                self.clear_reform()
                self.root2.destroy()




    def forgotcreate_window(self):
        if self.txtnameemailvar.get() == "":
            msgbox.showerror("Error", "Please Enter Email For Reset Password.", parent=self)
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="student_m_s")
            cur = con.cursor()
            cur.execute("select * from register_for_login where email=%s", (self.txtnameemailvar.get(),))
            row = cur.fetchone()
            if row == None:
                msgbox.showerror("Error", "Please Enter Valid Email ID For Reset Password.", parent=self)
            else:
                con.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("325x480+10+150")
                self.root2.config(bg="white")
                self.root2.focus_force()
                self.root2.grab_set()
                lbl_foget_h = Label(self.root2, text="Forgot Password", fg="red", bg="white",font=("times new roman", 15, "bold"))
                lbl_foget_h.place(x=70, y=20, height=40, width=200)

                lbl_question_combo = Label(self.root2, text="Secuirity Question", font="cosmicsansms 16 bold",bg="white",fg="darkblue")
                lbl_question_combo.place(x=70, y=70, height=40, width=200)
                self.txtquestionvar = StringVar()
                self.txtquestion = ttk.Combobox(self.root2, textvariable=self.txtquestionvar,justify="center",state="readonly", font=("times new roman", 9))
                self.txtquestion['values'] = ("Your Best Friend Name?", "Your Best Pet Name?", "Your Birth Place Name?")
                self.txtquestion.place(x=70, y=110, height=40, width=200)

                lbl_answer = Label(self.root2, text="Answer", font="cosmicsansms 16 bold", bg="white", fg="darkblue")
                lbl_answer.place(x=70, y=150, height=40, width=200)
                self.answervar = StringVar()
                self.txt_answer = Entry(self.root2, textvariable=self.answervar, bd=5,font="cosmicsansms 10 bold")
                self.txt_answer.place(x=70, y=190, height=40, width=200)

                lbl_newpass = Label(self.root2, text="New Password", font="cosmicsansms 16 bold", bg="white",fg="darkblue")
                lbl_newpass.place(x=70, y=230, height=40, width=200)
                self.newpassvar = StringVar()
                self.txt_newpass = Entry(self.root2, textvariable=self.newpassvar, bd=5,font="cosmicsansms 10 bold")
                self.txt_newpass.place(x=70, y=270, height=40, width=200)

                btnforgotchangepass = Button(self.root2, text="Change Passowrd", borderwidth=5, padx=10,font="lucida 10 bold",command=self.changepass_fun)
                btnforgotchangepass.place(x=70, y=360, height=40, width=200)


    def registerfirst(self):
        self.destroy()
        import registerloginform
    def login_fun(self):
        if self.txtpassvar.get()=="" or self.txtnameemailvar.get()=="":
            msgbox.showerror("Error","All Fields Are Requireds.")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="",database="student_m_s")
            cur=con.cursor()
            cur.execute("select * from register_for_login where email=%s AND password=%s",
                        (self.txtnameemailvar.get(),
                         self.txtpassvar.get()
                         ))
            row=cur.fetchone()
            print(row)
            con.commit()
            if row==None:
                msgbox.showerror("Error", "There is No Email ID AND Password Found...You Need To Register First.")

            else:
                msgbox.showinfo("Success", "You are SuccessFully Login.")
                cur.close()
                con.close()
                self.destroy()
                import student_management_Registration_Form

winobj=loginformwindow()
winobj.mainloop()



