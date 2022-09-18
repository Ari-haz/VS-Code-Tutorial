from py_compile import main
from tkinter import*
from tkinter import ttk
from turtle import st, width
import mysql.connector
import tkinter
from tkinter import messagebox
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # ============================Variable===========================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()


        lbltitle=Label(self.root,text="Library Management System",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        # ============================DataFrameLeft===============================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address Line-1",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address Line-2",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Postal Code",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="powder blue",text="Book ID:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.bookid_var,width=34)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.booktitle_var,width=34)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.author_var,width=34)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date of isuued:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateborrowed_var,width=34)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Due Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.datedue_var,width=34)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days on Book:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.daysonbook_var,width=34)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.latereturnfine_var,width=34)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateoverdue_var,width=34)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.finalprice_var,width=34)
        txtActualPrice.grid(row=8,column=3)


        # ==============================DataFrame Right================================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=["Data Structures and Algorithms","The C Programming Language","Synthesis and Optimization of Digital Circuits",
                    "Compilers: Principles, Techniques, and Tools","Head First Java","The Art of Computer Programming",
                    "Data Structures and Algorithms in Java","Programming Languages: Concepts and Constructs","The Annotated C++ Reference Manual",
                    "Essentials of Programming Languages","The Unix Programming Environment","Java Concurrency in Practice",
                    "Programming Language Pragmatics","Pro JavaScript Techniques","Object-Oriented Modeling and Design","The Elements of Programming Style"]
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Data Structures and Algorithms"):
                self.bookid_var.set("BKID5865")
                self.booktitle_var.set("DSA for All")
                self.author_var.set("Alfred V. Aho")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")

            elif (x=="The C Programming Language"):
                self.bookid_var.set("BKID0251")
                self.booktitle_var.set("Fundamentals of C Language")
                self.author_var.set("Brian Kernighan, Dennis Ritchie")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.816")

            elif (x=="Synthesis and Optimization of Digital Circuits"):
                self.bookid_var.set("BKID8542")
                self.booktitle_var.set("Logic Design")
                self.author_var.set("Giovanni De Micheli")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1200")

            elif (x=="Compilers: Principles, Techniques, and Tools"):
                self.bookid_var.set("BKID5634")
                self.booktitle_var.set("Compilers")
                self.author_var.set("Jeffrey D. Ullman, Monica S. Lam")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.950")

            elif (x=="Head First Java"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("Basic JAVA")
                self.author_var.set("Kathy Sierra, Bert Bates")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1040")

            elif (x=="The Art of Computer Programming"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("Learn How to code")
                self.author_var.set("Roberto Tamassia, Michael T. Goodrich")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1240")

            elif (x=="Data Structures and Algorithms in Java"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("DSA for JAVA")
                self.author_var.set("Ravi Sethi")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.850")

            elif (x=="Programming Languages: Concepts and Constructs"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("In-depth Programming")
                self.author_var.set("Bjarne Stroustrup, Margaret A. Ellis")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.850")
            
            elif (x=="The Annotated C++ Reference Manual"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("C++ Manual")
                self.author_var.set("Daniel P. Friedman")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1070")

            elif (x=="Essentials of Programming Languages"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("Programming Language")
                self.author_var.set("Brian W. Kernighan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1120")

            elif (x=="The Unix Programming Environment"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("Programming IDE")
                self.author_var.set("Brian Goetz")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1050")

            elif (x=="Java Concurrency in Practice"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("Concurrency in JAVA")
                self.author_var.set("Michael L. Scott")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.980")

            elif (x=="Programming Language Pragmatics"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("Pragmatics of Languages")
                self.author_var.set("John Resig")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1070")

            elif (x=="Pro JavaScript Techniques"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("Techniques in JAVAScript")
                self.author_var.set("James Rumbaugh, Michael R. Blaha")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1290")

            elif (x=="Object-Oriented Modeling and Design"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("Design of OOA")
                self.author_var.set("James Rumbaugh, Michael R. Blaha")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1580")

            elif (x=="The Elements of Programming Style"):
                self.bookid_var.set("BKID7805")
                self.booktitle_var.set("Style of Programming")
                self.author_var.set("Brian W. Kernighan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1300")

        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


        # ============================Buttons Frame================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=60)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update Data",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete Data",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset Data",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)



        # ==========================Information Frame==============================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1"
                                                            ,"address2","postid","mobile","bookid","booktitle","author","dateborrowed"
                                                            ,"datedue","daysonbook","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address Line 1")
        self.library_table.heading("address2",text="Address Line 2")
        self.library_table.heading("postid",text="Postal Code")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author Name")
        self.library_table.heading("dateborrowed",text="Date Of Issued")
        self.library_table.heading("datedue",text="Due Date")
        self.library_table.heading("daysonbook",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Actual Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("daysonbook",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Cricket7!",database="lib_data")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                               self.member_var.get(),
                                                                                                               self.prn_var.get(),
                                                                                                               self.id_var.get(),
                                                                                                               self.firstname_var.get(),
                                                                                                               self.lastname_var.get(),
                                                                                                               self.address1_var.get(),
                                                                                                               self.address2_var.get(),
                                                                                                               self.postcode_var.get(),
                                                                                                               self.mobile_var.get(),
                                                                                                               self.bookid_var.get(),
                                                                                                               self.booktitle_var.get(),
                                                                                                               self.author_var.get(),
                                                                                                               self.dateborrowed_var.get(),
                                                                                                               self.datedue_var.get(),
                                                                                                               self.daysonbook_var.get(),
                                                                                                               self.latereturnfine_var.get(),
                                                                                                               self.dateoverdue_var.get(),
                                                                                                               self.finalprice_var.get()
                                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member Has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Cricket7!",database="lib_data")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,Title=%s,First_Name=%s,Last_Name=%s,Address1=%s,Address2=%s,Postal_Code=%s,Mobile_Number=%s,Book_ID=%s,Book_Title=%s,Author_Name=%s,Date_of_Issued=%s,Due_Date=%s,Days_On_Book=%s,Late_Return_Fine=%s,Date_Over_Due=%s,Actual_Price=%s where PRN_No=%s",(
                                                                                                               self.member_var.get(),
                                                                                                               self.id_var.get(),
                                                                                                               self.firstname_var.get(),
                                                                                                               self.lastname_var.get(),
                                                                                                               self.address1_var.get(),
                                                                                                               self.address2_var.get(),
                                                                                                               self.postcode_var.get(),
                                                                                                               self.mobile_var.get(),
                                                                                                               self.bookid_var.get(),
                                                                                                               self.booktitle_var.get(),
                                                                                                               self.author_var.get(),
                                                                                                               self.dateborrowed_var.get(),
                                                                                                               self.datedue_var.get(),
                                                                                                               self.daysonbook_var.get(),
                                                                                                               self.latereturnfine_var.get(),
                                                                                                               self.dateoverdue_var.get(),
                                                                                                               self.finalprice_var.get(),
                                                                                                               self.prn_var.get()
                                                                                                            ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Updated")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Cricket7!",database="lib_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17]),

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"First Name:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address Line 1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address Line 2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Postal Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author Name:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"Date of Issued:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"Due Date:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"Days On Book:\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"Late Return Fine:\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"Date Overdue:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"Actual Price:\t\t"+ self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Cricket7!",database="lib_data")
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")



if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()