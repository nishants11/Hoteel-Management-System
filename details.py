from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:

    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1000x550+230+148")

        lbl_title=Label(self.root,text="Room Record",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1000,height=50)

        img2=Image.open(r"C:\Users\nisha\OneDrive\Desktop\python\Hotel Management dbms\images\logo.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=2,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        labelframeleft=LabelFrame(self.root,bd=2,text="Add New Room",font=("times new roman",12,"bold"),relief=RIDGE,padx=2)
        labelframeleft.place(x=5,y=50,width=525,height=310)

        lbl_floor=Label(labelframeleft,text="Floor",font=("times new roman",11,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=18,font=("times new roman",11,"bold"))
        enty_floor.grid(row=0,column=1,sticky=W)

        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("times new roman",11,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        self.var_roomNo=StringVar()
        enty_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=18,font=("times new roman",11,"bold"))
        enty_RoomNo.grid(row=1,column=1,sticky=W)

        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("times new roman",11,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        self.var_roomType=StringVar()
        enty_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_roomType,width=18,font=("times new roman",11,"bold"))
        enty_RoomType.grid(row=2,column=1,sticky=W)

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=170,width=380,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        Table_Frame=LabelFrame(self.root,bd=2,text="Show Rooms",font=("times new roman",12,"bold"),relief=RIDGE,padx=2)
        Table_Frame.place(x=580,y=55,width=335,height=310)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomtype",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room type")

        self.room_table["show"]="headings"
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomType.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),self.var_roomNo.get(),self.var_roomType.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS","Room added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("WARNING",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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
        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_roomType.set(row[2])

    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("ERROR","Floor is required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(self.var_floor.get(),self.var_roomType.get(),self.var_roomNo.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("SUCCESS","Room details updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("SURE?","Delete Room?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="sys")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_roomType.set("")








if __name__=='__main__':
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
