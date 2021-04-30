from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as msgbox
class Register_Form(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600+0+0")
        self.title("STUDENT MANAGEMENT SYSTEM")


        heading_label=Label(self,text="STUDENT MANAGEMENT SYSTEM",bg="#00ffff",fg="red",font=("cosmicsansms 20 bold"),bd=6,relief=SUNKEN)
        heading_label.pack(side=TOP,fill=X)
        #*************Frame Of Widget Registration******************
        frame_widget=Frame(self,bg="red",bd=6,relief=SUNKEN)
        frame_widget.place(x=20,y=60,width=500,height=670)
        heading_widget_label=Label(frame_widget,text="STUDENT MANAGEMENT SYSTEM",padx=70,bg="yellow",fg="red",font=("cosmicsansms 15 bold"),bd=6)
        heading_widget_label.grid(row=0,columnspan=2,padx=3,pady=8)


        lbl_name=Label(frame_widget,text="Name:",font="cosmicsansms 14 bold",padx=29,bg="red",fg="white")
        lbl_name.grid(row=1,column=0,sticky="w",padx=4,pady=4)
        self.txtnamevar=StringVar()
        self.txt_name=Entry(frame_widget,textvariable=self.txtnamevar,font="cosmicsansms 14 ",bd=4)
        self.txt_name.grid(row=1,column=1,pady=4,sticky="w")

        lbl_roll=Label(frame_widget,text="Roll No:",font="cosmicsansms 14 bold",padx=25,bg="red",fg="white")
        lbl_roll.grid(row=2,column=0,sticky="w",padx=4,pady=4)
        self.txtrollvar=IntVar()
        self.txt_roll=Entry(frame_widget,textvariable=self.txtrollvar,font="cosmicsansms 14 ",bd=4)
        self.txt_roll.grid(row=2,column=1,pady=4,sticky="w")


        lbl_class=Label(frame_widget,text="Class:",font="cosmicsansms 14 bold",padx=24,bg="red",fg="white")
        lbl_class.grid(row=3,column=0,sticky="w",padx=4,pady=4)
        self.class_combo=ttk.Combobox(frame_widget,state="readonly",justify="center",font=("times new roman",15 ))
        self.class_combo['values']=("BCA","MCA","BBA","MBA","IMCA","BE_MECHANICAL","BE_COMPUTER","BE_CIVIL","BE_ELECTRONICS")
        self.class_combo.grid(row=3,column=1,sticky="w",padx=4,pady=4)

        lbl_email=Label(frame_widget,text="Email:",font="cosmicsansms 14 bold",padx=33,bg="red",fg="white")
        lbl_email.grid(row=4,column=0,sticky="w",padx=4,pady=4)
        self.txtemailvar=StringVar()
        self.txt_email=Entry(frame_widget,textvariable=self.txtemailvar,font="cosmicsansms 14 ",bd=4)
        self.txt_email.grid(row=4,column=1,pady=4,sticky="w")

        lbl_gender=Label(frame_widget,text="Gender:",font="cosmicsansms 14 bold",padx=24,bg="red",fg="white")
        lbl_gender.grid(row=5,column=0,sticky="w",padx=4,pady=4)
        self.gerder_combo=ttk.Combobox(frame_widget,state="readonly",justify="center",font=("times new roman",15 ))
        self.gerder_combo['values']=("Male","Female","Other")
        self.gerder_combo.grid(row=5,column=1,sticky="w",padx=4,pady=4)

        contact_lbl=Label(frame_widget,text="Contact:",font="cosmicsansms 14 bold",padx=25,bg="red",fg="white")
        contact_lbl.grid(row=6,column=0,sticky="w",padx=4,pady=4)
        self.txtcontactvar=StringVar()
        self.txt_contact=Entry(frame_widget,textvariable=self.txtcontactvar,font="cosmicsansms 14 ",bd=4)
        self.txt_contact.grid(row=6,column=1,sticky="w",pady=4)

        dbo_lbl = Label(frame_widget, text="DOB:", font="cosmicsansms 14 bold", padx=40,bg="red",fg="white")
        dbo_lbl.grid(row=7, column=0, sticky="w", padx=4, pady=4)
        self.txtdobvar = StringVar()
        self.txt_dob = Entry(frame_widget, textvariable=self.txtdobvar, font="cosmicsansms 14 ", bd=4)
        self.txt_dob.grid(row=7, column=1, sticky="w", pady=4)

        lbl_address=Label(frame_widget,text="Address:",font="cosmicsansms 14 bold", padx=23,bg="red",fg="white")
        lbl_address.grid(row=8,column=0, sticky="w", padx=4, pady=4)
        self.txt_address=Text(frame_widget,font="cosmicsansms 14 ", bd=4,height=5,width=20)
        self.txt_address.grid(row=8,column=1, sticky="w", pady=4)

        #***********************Frame For Delete Update Add Clear********************************
        frame_btn_operation=Frame(frame_widget, bg="grey", bd=6, relief=SUNKEN)
        frame_btn_operation.place(x=20, y=500, width=440, height=120)

        self.btn_add=Button(frame_btn_operation,text="Add",font="cosmicsansms 14 bold",padx=10,command=self.addrecords)
        self.btn_add.grid(row=0,column=0,padx=14,pady=25)

        btn_update=Button(frame_btn_operation,text="Update",font="cosmicsansms 14 bold",padx=10,command=self.update_records)
        btn_update.grid(row=0,column=1,padx=5,pady=25)

        # btn_delte=Button(frame_btn_operation,text="Delete",font="cosmicsansms 14 bold",padx=10)
        btn_delte=Button(frame_btn_operation,text="Delete",font="cosmicsansms 14 bold",padx=10,command=self.delete_recors)
        btn_delte.grid(row=0,column=3,padx=5,pady=25)

        btn_clear=Button(frame_btn_operation,text=" Clear",font="cosmicsansms 14 bold",padx=10,command=self.clear_page)
        btn_clear.grid(row=0,column=4,padx=5,pady=25)
        #*************Frame Of  Details Registration******************

        frame_Details= Frame(self, bg="red", bd=6, relief=SUNKEN)
        frame_Details.place(x=525, y=60, width=740, height=670)
        search_lbl_combo=Label(frame_Details,text="Search By",font="cosmicsansms 14 bold",padx=10,bd=0,bg="red",fg="white")
        search_lbl_combo.grid(row=0,column=0,sticky="w",padx=5,pady=5)

        self.searchby_combovar=StringVar()
        self.txtsearchvar=StringVar()
        self.searchby_combo=ttk.Combobox(frame_Details,state="readonly",justify="center",font=("times new roman",12),textvariable=self.searchby_combovar)
        self.searchby_combo['values']=("rollno","class","name","email","contact")
        self.searchby_combo.grid(row=0,column=1,sticky="w",padx=5,pady=5)

        self.search_txt=Entry(frame_Details,textvariable=self.txtsearchvar,font="cosmicsansms 13 bold")
        self.search_txt.grid(row=0,column=2,sticky="w",padx=5,pady=5)
        txtsearchbtn=Button(frame_Details,text="Search",font="cosmicsansms 12 bold",padx=10,command=self.search_records)
        txtsearchbtn.grid(row=0,column=3,sticky="w",padx=5,pady=5)
        txtshowallbtn = Button(frame_Details, text="Show All", font="cosmicsansms 12 bold", padx=10,command=self.fetch_data_details)
        txtshowallbtn.grid(row=0, column=4, sticky="w", padx=5, pady=5)

        #************************Frame For student Details Show on TreeView*************
        d_show=Frame(frame_Details,bg="red", bd=4, relief=SUNKEN)
        d_show.place(x=10,y=70,width=710,height=580)
        #SCROLL BAR X and Y
        scroll_x=Scrollbar(d_show,orient=HORIZONTAL)
        scroll_Y=Scrollbar(d_show,orient=VERTICAL)

        #Treeview studentTREEVIEW
        self.student_table=ttk.Treeview(d_show,columns=("id","name","rollno","class","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_Y.config(command=self.student_table.yview)

        #studennt_treeview Headings
        self.student_table.heading("id",text="Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("rollno",text="Roll_No")
        self.student_table.heading("class",text="Class")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("address",text="Address")
        self.student_table['show']='headings'

        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("class",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("address",width=100)
        self.student_table.pack(fill=BOTH,expand=True)
        self.student_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data_details()

    def addrecords(self):
        try:
            if self.txtnamevar.get() == "" or self.txtrollvar.get() == "" or self.class_combo.get() == "" or self.txtemailvar.get() == "" or self.gerder_combo.get() == "" or self.txtcontactvar.get() == "" or self.txtdobvar.get() == "" or self.txt_address.get('1.0',END) == "":
                msgbox.showerror("Error", "All Fields Are Required Please Fill Fields.")
            else:
                con = mysql.connector.connect(host="localhost", user="root", password="", database="student_m_s")
                cur = con.cursor()
                cur.execute("select * from students_registration where rollno="+str(self.txtrollvar.get()))
                rollno_check=cur.fetchone()
                print(rollno_check)
                if rollno_check==None:
                    cur.execute(
                        "insert into students_registration(name,rollno,class,email,gender,contact,dob,address)values(%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.txtnamevar.get(),
                         self.txtrollvar.get(),
                         self.class_combo.get(),
                         self.txtemailvar.get(),
                         self.gerder_combo.get(),
                         self.txtcontactvar.get(),
                         self.txtdobvar.get(),
                         self.txt_address.get('1.0', END)
                         ))
                    con.commit()
                    msgbox.showinfo("SuccessFullyRegister", "Register SuccessFully ")
                    self.clear_page()
                    self.fetch_data_details()
                    cur.close()
                    con.close()
                else:
                    msgbox.showerror("All Ready Inserted","Roll No Already Inserted.")
        except Exception as e:
            print(f"Error Occur Due To{e}")


    def clear_page(self):
        try:
            self.txtnamevar.set("")
            self.txtrollvar.set("")
            self.class_combo.set("")
            self.txtemailvar.set("")
            self.gerder_combo.set("")
            self.txtcontactvar.set("")
            self.txtdobvar.set("")
            self.txt_address.delete('1.0',END)
        except Exception as e:
            print(f"Error Occur Due To{e}")

    def fetch_data_details(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="student_m_s")
            cur = con.cursor()
            cur.execute("select * from students_registration")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('',END,values=row)
                    con.commit()
                con.close()
            else:
                self.student_table.delete(*self.student_table.get_children())
        except Exception as e:
            print(f"Error Occur Due To{e}")




    def delete_recors(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="student_m_s")
            cur = con.cursor()
            cur.execute("delete from students_registration where rollno='%s'",(self.txtrollvar.get(),))
            con.commit()
            con.close()
            self.fetch_data_details()
            self.clear_page()
            msgbox.showinfo("Delete","Records Deleted Succesfuly.")
        except Exception as e:
            print()
            msgbox.showinfo("Error",f"Error Occur Due To{e}")


    def update_records(self):
        try:
            if self.txtnamevar.get() == "" or self.txtrollvar.get() == "" or self.class_combo.get() == "" or self.txtemailvar.get() == "" or self.gerder_combo.get() == "" or self.txtcontactvar.get() == "" or self.txtdobvar.get() == "" or self.txt_address.get('1.0',END) == "":
                msgbox.showerror("Error", "All Fields Are Required Please Fill Fields.")
            else:
                con = mysql.connector.connect(host="localhost", user="root", password="", database="student_m_s")
                cur = con.cursor()
                cur.execute("update students_registration set name=%s,rollno=%s,class=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where rollno=%s",
                            (self.txtnamevar.get(),
                             self.txtrollvar.get(),
                             self.class_combo.get(),
                             self.txtemailvar.get(),
                             self.gerder_combo.get(),
                             self.txtcontactvar.get(),
                             self.txtdobvar.get(),
                             self.txt_address.get('1.0',END),
                             self.txtrollvar.get()
                            ))
                con.commit()
                cur.close()
                con.close()
                msgbox.showinfo("SuccessFullyUpdated", "Records Update SuccessFully.")
                self.clear_page()
                self.fetch_data_details()
        except Exception as e:
            msgbox.showinfo("Error",f"Error Occur Due To{e}")


    def search_records(self):
        try:
            if self.txtsearchvar.get()=="" or self.searchby_combo.get()=="":
                msgbox.showerror("Error", "All Fields Are Required Please Fill Fields.")
            else:
                con = mysql.connector.connect(host="localhost", user="root", password="", database="student_m_s")
                cur = con.cursor()
                cur.execute("select * from students_registration where "+str(self.searchby_combovar.get())+" LIKE '%"+str(self.txtsearchvar.get())+"%'")
                # select * from students_registration where'?'LIKE'%?%'
                rows=cur.fetchall()
                print(rows)
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("",END,values=row)
                    con.commit()
                    con.close()
                else:
                    self.student_table.delete(*self.student_table.get_children())
        except Exception as e:
            msgbox.showinfo("Error",f"Error Occur Due To{e}")




    def get_cursor(self,evnt):
        try:
            cursor_row=self.student_table.focus()
            contents=self.student_table.item(cursor_row)
            rows1=contents['values']
            self.studeid=IntVar()
            self.studeid.set(rows1[0])
            self.txtnamevar.set(rows1[1])
            self.txtrollvar.set(int(rows1[2]))
            self.class_combo.set(rows1[3])
            self.txtemailvar.set(rows1[4])
            self.gerder_combo.set(rows1[5])
            self.txtcontactvar.set(rows1[6])
            self.txtdobvar.set(rows1[7])
            self.txt_address.delete('1.0', END)
            self.txt_address.insert(END, rows1[8])
        except Exception as e:
            msgbox.showinfo("Error",f"Error Occur Due To{e}")



win_obj=Register_Form()
win_obj.mainloop()