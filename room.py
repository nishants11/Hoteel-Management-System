from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:

    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1000x550+230+148")

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        lbl_title=Label(self.root,text="Booking DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1000,height=50)

        img2=Image.open(r"C:\Users\nisha\OneDrive\Desktop\python\Hotel Management dbms\images\logo.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=2,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        labelframeleft=LabelFrame(self.root,bd=2,text="Roombooking DETAILS",font=("times new roman",12,"bold"),relief=RIDGE,padx=2)
        labelframeleft.place(x=5,y=50,width=405,height=450)

        lbl_cusr_contact=Label(labelframeleft,text="Customer Reference No",font=("times new roman",11,"bold"),padx=2,pady=6)
        lbl_cusr_contact.grid(row=0,column=0,sticky=W)
        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=18,font=("times new roman",11,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)

        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("times new roman",7,"bold"),bg="black",fg="gold",width=7)
        btnFetchData.place(x=320,y=3)

        check_in_date=Label(labelframeleft,text="Check_in Date",font=("times new roman",11,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=25,font=("times new roman",11,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        lbl_Check_out=Label(labelframeleft,text="Check_out Date",font=("times new roman",11,"bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=25,font=("times new roman",11,"bold"))
        txt_Check_out.grid(row=2,column=1)

        label_RoomType=Label(labelframeleft,text="Room Type",font=("times new roman",11,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("select distinct RoomType from details")
        ide=my_cursor.fetchall()
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("times new roman",11,"bold"),width=18,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(1)
        combo_RoomType.grid(row=3,column=1)
        btnFetchData=Button(labelframeleft,command=self.Fetch_room,text="Fetch Data",font=("times new roman",7,"bold"),bg="black",fg="gold",width=7)
        btnFetchData.place(x=320,y=103)

        lblRoomAvailable=Label(labelframeleft,text="Available Room",font=("times new roman",11,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=25,font=("times new roman",11,"bold"),state="readonly")
        txtRoomAvailable.grid(row=4,column=1)

        lblMeal=Label(labelframeleft,text="Meal",font=("times new roman",11,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=25,font=("times new roman",11,"bold"))
        txtMeal.grid(row=5,column=1)

        lblNoOfDays=Label(labelframeleft,text="No Of Days",font=("times new roman",11,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=25,font=("times new roman",11,"bold"))
        txtNoOfDays.grid(row=6,column=1)

        lblNoOfDays=Label(labelframeleft,text="Tax Paid",font=("times new roman",11,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=25,font=("times new roman",11,"bold"))
        txtNoOfDays.grid(row=7,column=1)

        lblNoOfDays=Label(labelframeleft,text="Sub Total",font=("times new roman",11,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=25,font=("times new roman",11,"bold"))
        txtNoOfDays.grid(row=8,column=1)

        lblTotal=Label(labelframeleft,text="Total",font=("times new roman",11,"bold"),padx=2,pady=6)
        lblTotal.grid(row=9,column=0,sticky=W)
        txtTotal=ttk.Entry(labelframeleft,textvariable=self.var_total,width=25,font=("times new roman",11,"bold"))
        txtTotal.grid(row=9,column=1)

        btnBill=Button(labelframeleft,command=self.total,text="Bill",font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=370,width=380,height=40)

        btnAdd=Button(btn_frame,command=self.add_data,text="Add",font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,command=self.update,text="Update",font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,command=self.mDelete,text="Delete",font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,command=self.reset,text="Reset",font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        img3=Image.open(r"C:\Users\nisha\OneDrive\Desktop\python\Hotel Management dbms\images\download (3).jfif")
        img3=img3.resize((300,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=2,relief=RIDGE)
        lblimg.place(x=750,y=55,width=300,height=300)

        Table_Frame=LabelFrame(self.root,bd=2,text="VIEW DETAILS & SEARCH SYSTEM",font=("times new roman",12,"bold"),relief=RIDGE,padx=2)
        Table_Frame.place(x=415,y=280,width=585,height=220)

        lblSearchBy=Label(Table_Frame,text="Search By",font=("times new roman",11,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=1)
        self.serch_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("times new roman",11,"bold"),width=14,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(1)
        combo_Search.grid(row=0,column=1,padx=1)
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,width=18,textvariable=self.txt_search,font=("times new roman",11,"bold"))
        txtSearch.grid(row=0,column=2,padx=1)

        btnSearch=Button(Table_Frame,command=self.search,text="Search",font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,command=self.fetch_data,text="Show All",font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=555,height=160)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Ref")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room type")
        self.room_table.heading("roomavailable",text="Room No.")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="NoOfDays")
        self.room_table["show"]="headings"
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(),self.var_roomavailable.get(),self.var_meal.get(),self.var_noofdays.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS","Booking added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("WARNING",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cuersor(self,event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("ERROR","Mobile no. is required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,Room=%s,meal=%s,noOfdays=%s where Contact=%s",(self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(),self.var_roomavailable.get(),self.var_meal.get(),self.var_noofdays.get(),self.var_contact.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("SUCCESS","Booking details updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("SURE?","Delete Booking?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s AND check_in=%s AND check_out=%s AND Room=%s"
            value=(self.var_contact.get(),self.var_checkin.get(),self.var_checkout.get(),self.var_roomavailable.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")


    def Fetch_room(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
            my_cursor=conn.cursor()
            showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
            showDataframe.place(x=435,y=55,width=300,height=180)
            value=(self.var_roomtype.get(),)
            query="select RoomNo from details where RoomType=%s"
            my_cursor.execute(query,value)
            rows=my_cursor.fetchall()
            combo_RoomNo=ttk.Combobox(showDataframe,textvariable=self.var_roomavailable,font=("times new roman",11,"bold"),width=25,state="readonly")
            combo_RoomNo["value"]=rows
            combo_RoomNo.current()
            combo_RoomNo.grid(row=4,column=1)


    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("ERROR","Ref no. is required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
            my_cursor=conn.cursor()
            query=("select Name from customer where Ref=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("ERROR","Ref no. not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=435,y=55,width=300,height=180)
                lblName=Label(showDataframe,text="Name",font=("times new roman",11,"bold"))
                lblName.place(x=0,y=0)
                lbl=Label(showDataframe,text=row,font=("times new roman",11,"bold"))
                lbl.place(x=90,y=0)

                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Ref=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblGender=Label(showDataframe,text="Gender",font=("times new roman",11,"bold"))
                lblGender.place(x=0,y=25)
                lbl2=Label(showDataframe,text=row,font=("times new roman",11,"bold"))
                lbl2.place(x=90,y=25)

                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
                my_cursor=conn.cursor()
                query=("select Email from customer where Ref=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblEmail=Label(showDataframe,text="Email",font=("times new roman",11,"bold"))
                lblEmail.place(x=0,y=50)
                lbl3=Label(showDataframe,text=row,font=("times new roman",11,"bold"))
                lbl3.place(x=90,y=50)

                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Ref=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblNationality=Label(showDataframe,text="Nationality",font=("times new roman",11,"bold"))
                lblNationality.place(x=0,y=75)
                lbl4=Label(showDataframe,text=row,font=("times new roman",11,"bold"))
                lbl4.place(x=90,y=75)

                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
                my_cursor=conn.cursor()
                query=("select Address from customer where Ref=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblAddress=Label(showDataframe,text="Address",font=("times new roman",11,"bold"))
                lblAddress.place(x=0,y=100)
                lbl5=Label(showDataframe,text=row,font=("times new roman",11,"bold"))
                lbl5.place(x=90,y=100)

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%y")
        outDate=datetime.strptime(outDate,"%d/%m/%y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Suite"):
            q1=float(300)
            q2=float(12000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Suite"):
            q1=float(500)
            q2=float(12000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Suite"):
            q1=float(500)
            q2=float(12000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Deluxe"):
            q1=float(500)
            q2=float(8000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Deluxe"):
            q1=float(300)
            q2=float(8000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Deluxe"):
            q1=float(500)
            q2=float(8000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="SuperDeluxe"):
            q1=float(500)
            q2=float(10000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="SuperDeluxe"):
            q1=float(500)
            q2=float(10000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="SuperDeluxe"):
            q1=float(300)
            q2=float(10000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

if __name__=='__main__':
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
