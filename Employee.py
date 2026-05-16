from tkinter import*
import mysql
import mysql.connector
from tkinter import messagebox,ttk
import time
import os
import tempfile


class EmployeeSystem():
    def __init__(self,root):
        self.root=root
        self.root.title("Employee PayRoll Management System | Developed By Velmurugan")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title1=Label(self.root,text="Employee PayRoll Management System",font=("times new roman",30,"bold"),bg="#262626",fg="white").place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root,text="All employee's",command=self.employee_frame,font=("times new roman",15),bg="gray",fg="white").place(x=1100,y=10,height=30,width=130)
        #===============frame1==========================
        #=======variables===============================
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_hr_location=StringVar()
        self.var_experience=StringVar()
        self.var_proof_id=StringVar()#adhar card
        self.var_status=StringVar()
        self.var_contact=StringVar()
    
        
        
        
        
        
        
        
        
        
        
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,height=620,width=750)
        title2=Label(Frame1,text="Employee Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        #===Employee Code===
        lbl_code=Label(Frame1,text="Employee Code",font=("times new roman",20),bg="white",fg="black").place(x=10,y=70)
        self.txt_code=Entry(Frame1,text=("times new roman",15),textvariable=self.var_emp_code,bg="lightyellow",fg="black")
        self.txt_code.place(x=210,y=85,width=150)
        btn_search=Button(Frame1,text="Search",command=self.search,font=("times new roman",15),bg="lightgreen",fg="black").place(x=370,y=75,height=30)
        #====row1===
        #===designation===
        lbl_designation=Label(Frame1,text="Designation",font=("times new roman",20),bg="white",fg="black").place(x=10,y=120)
        txt_designation=Entry(Frame1,font=("times new roman",15),textvariable=self.var_designation,bg="lightyellow",fg="black").place(x=170,y=125,width=200)
        #====dob=====
        lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman",20),bg="white",fg="black").place(x=390,y=125)
        txt_dob=Entry(Frame1,font=("times new roman",15),textvariable=self.var_dob,bg="lightyellow",fg="black").place(x=520,y=130,width=200)
        
        #====row2===
        #===name===
        lbl_name=Label(Frame1,text="Name",font=("times new roman",20),bg="white",fg="black").place(x=10,y=170)
        txt_name=Entry(Frame1,font=("times new roman",15),textvariable=self.var_name,bg="lightyellow",fg="black").place(x=170,y=175,width=200)
        #====doj=====
        lbl_doj=Label(Frame1,text="D.O.J",font=("times new roman",20),bg="white",fg="black").place(x=390,y=175)
        txt_doj=Entry(Frame1,font=("times new roman",15),textvariable=self.var_doj,bg="lightyellow",fg="black").place(x=520,y=175,width=200)
        
        #====row3===
        #===age===
        lbl_age=Label(Frame1,text="Age",font=("times new roman",20),bg="white",fg="black").place(x=10,y=220)
        txt_age=Entry(Frame1,font=("times new roman",15),textvariable=self.var_age,bg="lightyellow",fg="black").place(x=170,y=220,width=200)
        #====experiance=====
        lbl_experience=Label(Frame1,text="Experience",font=("times new roman",20),bg="white",fg="black").place(x=390,y=220)
        txt_experience=Entry(Frame1,font=("times new roman",15),textvariable=self.var_experience,bg="lightyellow",fg="black").place(x=520,y=220,width=200)
        
        #====row4====== 
        #===gender=====
        lbl_gender=Label(Frame1,text="Gender",font=("times new roman",20),bg="white",fg="black").place(x=10,y=270)
        txt_gender=Entry(Frame1,font=("times new roman",15),textvariable=self.var_gender,bg="lightyellow",fg="black").place(x=170,y=270,width=200)
        #====proof id=====
        lbl_proof_id=Label(Frame1,text="Proof ID",font=("times new roman",20),bg="white",fg="black").place(x=390,y=270)
        txt_proof_id=Entry(Frame1,font=("times new roman",15),textvariable=self.var_proof_id,bg="lightyellow",fg="black").place(x=520,y=270,width=200)
        
        #====row5===
        #===email===
        lbl_email=Label(Frame1,text="Email",font=("times new roman",20),bg="white",fg="black").place(x=10,y=320)
        txt_email=Entry(Frame1,font=("times new roman",15),textvariable=self.var_email,bg="lightyellow",fg="black").place(x=170,y=320,width=200)
        #====proof id=====
        lbl_contact=Label(Frame1,text="Contact",font=("times new roman",20),bg="white",fg="black").place(x=390,y=320)
        txt_contact=Entry(Frame1,font=("times new roman",15),textvariable=self.var_contact,bg="lightyellow",fg="black").place(x=520,y=320,width=200)
        
        #====row6======
        #=====hired location
        lbl_hr_location=Label(Frame1,text="Hr_Location",font=("times new roman",20),bg="white",fg="black").place(x=10,y=370)
        txt_hr_location=Entry(Frame1,font=("times new roman",15),textvariable=self.var_hr_location,bg="lightyellow",fg="black").place(x=170,y=370,width=200)
        #====status=====
        lbl_status=Label(Frame1,text="Status",font=("times new roman",20),bg="white",fg="black").place(x=390,y=370)
        txt_status=Entry(Frame1,font=("times new roman",15),textvariable=self.var_status,bg="lightyellow",fg="black").place(x=520,y=370,width=200)
        
        #====row7====
        #=====address===
        lbl_address=Label(Frame1,text="Address",font=("times new roman",20),bg="white",fg="black").place(x=10,y=420)
        self.txt_address=Text(Frame1,font=("times new roman",15),bg="lightyellow",fg="black")
        self.txt_address.place(x=170,y=420,height=150,width=550)
            
        #===============frame2==========================
        
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_b_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,height=300,width=580)
        
        title3=Label(Frame2,text="Employee Salary Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        #====row1=====
        #====month====
        lbl_month=Label(Frame2,text="Month",font=("times new roman",20),bg="white",fg="black").place(x=10,y=70)
        txt_month=Entry(Frame2,font=("times new roman",15),textvariable=self.var_month,bg="lightyellow",fg="black").place(x=90,y=75,width=100)
        
        #====year====
        lbl_year=Label(Frame2,text="year",font=("times new roman",20),bg="white",fg="black").place(x=200,y=70)
        txt_year=Entry(Frame2,font=("times new roman",15),textvariable=self.var_year,bg="lightyellow",fg="black").place(x=260,y=75,width=100)
        
        #====salary==
        lbl_b_salary=Label(Frame2,text="B_Salary",font=("times new roman",20),bg="white",fg="black").place(x=360,y=70)
        txt_b_salary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_b_salary,bg="lightyellow",fg="black").place(x=470,y=75,width=100)
        
        #===row2===
        #====total days===
        lbl_t_days=Label(Frame2,text="Total Days",font=("times new roman",20),bg="white",fg="black").place(x=10,y=110)
        txt_t_days=Entry(Frame2,font=("times new roman",15),textvariable=self.var_t_days,bg="lightyellow",fg="black").place(x=140,y=115,width=100)
        
        #====absent===
        lbl_absent=Label(Frame2,text="Absent",font=("times new roman",20),bg="white",fg="black").place(x=270,y=110)
        txt_absent=Entry(Frame2,font=("times new roman",15),textvariable=self.var_absent,bg="lightyellow",fg="black").place(x=390,y=115,width=100)
        
        #===row3===
        #====medical===
        lbl_medical=Label(Frame2,text="Medical",font=("times new roman",20),bg="white",fg="black").place(x=10,y=140)
        txt_medical=Entry(Frame2,font=("times new roman",15),textvariable=self.var_medical,bg="lightyellow",fg="black").place(x=140,y=145,width=100)
        
        #====pf===
        lbl_pf=Label(Frame2,text="PF",font=("times new roman",20),bg="white",fg="black").place(x=270,y=140)
        txt_pf=Entry(Frame2,font=("times new roman",15),textvariable=self.var_pf,bg="lightyellow",fg="black").place(x=390,y=145,width=100)
        
        #===row4===
        #====convence===
        lbl_convence=Label(Frame2,text="Convence",font=("times new roman",20),bg="white",fg="black").place(x=10,y=170)
        txt_convence=Entry(Frame2,font=("times new roman",15),textvariable=self.var_convence,bg="lightyellow",fg="black").place(x=140,y=175,width=100)
        
        #====pf===
        lbl_net_salary=Label(Frame2,text="Net Salary",font=("times new roman",20),bg="white",fg="black").place(x=270,y=170)
        txt_net_salary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_net_salary,bg="lightyellow",fg="black").place(x=390,y=175,width=100)
        
        #===calculate==
        btn_calculate=Button(Frame2,text="Calculate",command=self.calculate,font=("times new roman",15),bg="orange",fg="black").place(x=100,y=220,height=30,width=120)
        #====save====
        self.btn_save=Button(Frame2,text="Save",command=self.add,font=("times new roman",15),bg="green",fg="black")
        self.btn_save.place(x=230,y=220,height=30,width=120)
        #====clear===
        btn_clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",15),bg="gray",fg="white").place(x=360,y=220,height=30,width=120)        
        #=====delete 
        self.btn_update=Button(Frame2,text="Update",command=self.update,state=DISABLED,font=("times new roman",15),bg="pink",fg="black")
        self.btn_update.place(x=160,y=260,height=30,width=120)
        #======update==
        self.btn_delete=Button(Frame2,text="Delete",command=self.delete,state=DISABLED,font=("times new roman",15),bg="red",fg="black")
        self.btn_delete.place(x=310,y=260,height=30,width=120)
        
        
        
        #===============frame3==========================
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,height=310,width=580)
        #====calculator frame====
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
            
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
        def clear_cal():
            self.var_txt.set(" ")
            self.var_operator=" "
            
            
        cal_frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        cal_frame.place(x=2,y=2,width=248,height=300)
        
        txt_result=Entry(cal_frame,bg="lightyellow",textvariable=self.var_txt,font=("times new roman",20,"bold"),justify=RIGHT).place(x=0,y=0,relwidth=1,height=52)
        
        #=====button====
        #======row1===
        btn_7=Button(cal_frame,text="7",command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=0,y=52,height=60,width=60)
        btn_8=Button(cal_frame,text="8",command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=61,y=52,height=60,width=60)
        btn_9=Button(cal_frame,text="9",command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=122,y=52,height=60,width=60)
        btn_div=Button(cal_frame,text="/",command=lambda:btn_click("/"),font=("times new roman",15,"bold")).place(x=183,y=52,height=60,width=60)
        
        #======row2===
        btn_4=Button(cal_frame,text="4",command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=0,y=112,height=60,width=60)
        btn_5=Button(cal_frame,text="5",command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=61,y=112,height=60,width=60)
        btn_6=Button(cal_frame,text="6",command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=122,y=112,height=60,width=60)
        btn_mul=Button(cal_frame,text="*",command=lambda:btn_click("*"),font=("times new roman",15,"bold")).place(x=183,y=112,height=60,width=60)
        
        #======row3===
        btn_1=Button(cal_frame,text="1",command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=0,y=172,height=60,width=60)
        btn_2=Button(cal_frame,text="2",command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=61,y=172,height=60,width=60)
        btn_3=Button(cal_frame,text="3",command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=122,y=172,height=60,width=60)
        btn_min=Button(cal_frame,text="-",command=lambda:btn_click("-"),font=("times new roman",15,"bold")).place(x=183,y=172,height=60,width=60)
        
        #======row4===
        btn_0=Button(cal_frame,text="0",command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=0,y=232,height=60,width=60)
        btn_clear=Button(cal_frame,text="C",command=clear_cal,font=("times new roman",15,"bold")).place(x=61,y=232,height=60,width=60)
        btn_sum=Button(cal_frame,text="+",command=lambda:btn_click("+"),font=("times new roman",15,"bold")).place(x=122,y=232,height=60,width=60)
        btn_equal=Button(cal_frame,text="=",command=result,font=("times new roman",15,"bold")).place(x=183,y=232,height=60,width=60)
        
        #========salary frame===
        sal_frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_frame.place(x=251,y=2,width=320,height=300)
        #====title
        title_sal=Label(sal_frame,text="Salary Reciept",font=("times new roman",20),bg="lightgray",fg="black",padx=10,anchor="w").place(x=0,y=0,relwidth=1)
        
        sal_frame2=Frame(sal_frame,bg="white",bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=30,relwidth=1,height=230)
        self.sample=f'''\tCompany Name XYZ\n\tAddress: xyz,floor 4

----------------------------------------
 Employee ID\t\t:  
 Salary Of\t\t:  Mon-YYYY
 Genarated On\t\t: DD-MM-YYYY
---------------------------------------
 total Days\t\t:  DD
 total Presant\t\t:  DD
 total Absent\t\t:  DD
 Convence\t\t:  Rs.----
 Medical\t\t:  Rs.----
 Pf\t\t:  Rs.----
 Cross Payment\t\t:  Rs.-------
 Net Salary\t\t:  Rs.--------
-------------------------------------
this is computer genarated slip,not
required any signature
'''
        
        #===scroll bar
        scroll_y=Scrollbar(sal_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
        
        self.txt_salary_reciept=Text(sal_frame2,font=("times new roman",15),bg="lightyellow",yscrollcommand=scroll_y)
        self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_reciept.yview)
        self.txt_salary_reciept.insert(END,self.sample)
        
        #print button
        
        self.btn_print=Button(sal_frame,text="Print",state=DISABLED,command=self.print,font=("times new roman",15),bg="lightblue",fg="black")
        self.btn_print.place(x=200,y=265,height=30,width=100)
        
        self.check_connection()
#================================all functions=========================
    def search(self):
        try:
            mydb=mysql.connector.connect(
                host="localhost",
                port="3306",
                user="root",
                password="root",
                database="ems"
            )
            cur=mydb.cursor()
            query="SELECT * FROM emp_salary WHERE e_id=%s"
            cur.execute(query,(self.var_emp_code.get(),))
            row=cur.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","invalid employee id,please try another employee id",parent=self.root)
            else:
                print(row)
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hr_location.set(row[6])
                self.var_dob.set(row[7])
                self.var_doj.set(row[8])
                self.var_experience.set(row[9])
                self.var_proof_id.set(row[10])
                self.var_status.set(row[11])
                self.var_contact.set(row[12])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,row[13])
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_b_salary.set(row[16])
                self.var_t_days.set(row[17])
                self.var_absent.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_net_salary.set(row[22])
                file=open('salary_reciept/'+str(row[23]),"r")
                self.txt_salary_reciept.delete('1.0',END)
                for i in file:
                    self.txt_salary_reciept.insert(END,i)
                file.close()
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_code.config(state='readonly')
                self.btn_print.config(state=NORMAL)
        except Exception as ex:
                messagebox.showerror("Error",f"error due to :{str(ex)}")
    #clear function
    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)
        

        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_experience.set('')
        self.var_proof_id.set('')
        self.var_status.set('')
        self.var_contact.set('')
        self.txt_address.delete('1.0',END)
        
        self.var_month.set('')
        self.var_year.set('')
        self.var_b_salary.set('')
        self.var_t_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set('')
        self.txt_salary_reciept.delete('1.0',END)
        self.txt_salary_reciept.insert(END,self.sample)        
            
    #======delete function=======
    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","employee if must be required")
        else:
            try:
                mydb=mysql.connector.connect(
                    host="localhost",
                    port="3306",
                    user="root",
                    password="root",
                    database="ems"
                )
                cur=mydb.cursor()
                query="SELECT * FROM emp_salary WHERE e_id=%s"
                cur.execute(query,(self.var_emp_code.get(),))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","invalid employee id,please try another employee id",parent=self.root) 
                else:
                    op=messagebox.askyesno("confirm","do you really want to delete?")
                    print(op)
                    if op==True:
                        query="DELETE FROM emp_salary WHERE e_id=%s"
                        cur.execute(query,(self.var_emp_code.get(),))
                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo("Success","Employee Details deleted successfully",parent=self.root)
                        self.clear() 
            except Exception as ex:
                messagebox.showerror("Error",f"error due to :{str(ex)}")            
                        
    #=======update function====
    def update(self):
        if self.var_emp_code.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","employee details  requird")
        else:
        
            try:
                mydb=mysql.connector.connect(
                    host="localhost",
                    port="3306",
                    user="root",
                    password="root",
                    database="ems"
                )
                cur=mydb.cursor()
                query="SELECT * FROM emp_salary WHERE e_id=%s"
                cur.execute(query,(self.var_emp_code.get(),))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","this employee id is invalid,please try valid employee id",parent=self.root)
                else:
                    cur.execute("""UPDATE emp_salary SET designation=%s,name=%s,age=%s,gender=%s,email=%s,hr_location=%s,doj=%s,dob=%s,experience=%s,proof_id=%s,contact=%s,status=%s,address=%s,month=%s,year=%s,b_salary=%s,t_days=%s,absent=%s,medical=%s,pf=%s,convence=%s,net_salary=%s,salary_reciept=%s WHERE e_id=%s""",
                            (
                                     
                                
                                self.var_designation.get(),
                                self.var_name.get(),
                                self.var_age.get(),
                                self.var_gender.get(),
                                self.var_email.get(),
                                self.var_hr_location.get(),
                                self.txt_address.get('1.0',END),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_experience.get(),
                                self.var_proof_id.get(),
                                self.var_status.get(),
                                self.var_contact.get(),
                                self.var_month.get(),
                                self.var_year.get(),
                                self.var_b_salary.get(),
                                self.var_t_days.get(),
                                self.var_absent.get(),
                                self.var_medical.get(),
                                self.var_pf.get(),
                                self.var_convence.get(),
                                self.var_net_salary.get(),
                                self.var_emp_code.get()+".txt",
                                self.var_emp_code.get()
                                #101.txt
                                        
                            )
                            )
                mydb.commit()
                mydb.close()
                file=open('salary_reciept/'+str(self.var_emp_code.get())+".txt","w")
                file.write(self.txt_salary_reciept.get('1.0',END))
                file.close()
                messagebox.showinfo("Success","Record updated successfully")
               
                                    
                 
            except Exception as ex:
                messagebox.showerror("Error",f"error due to :{str(ex)}")
                       
        
        
        
    def add(self):
        if self.var_emp_code.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","employee details  requird")
        else:
        
            try:
                mydb=mysql.connector.connect(
                    host="localhost",
                    port="3306",
                    user="root",
                    password="root",
                    database="ems"
                )
                cur=mydb.cursor()
                query="SELECT * FROM emp_salary WHERE e_id=%s"
                cur.execute(query,(self.var_emp_code.get(),))
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","this employee id has alredy recorded,please try another Id",parent=self.root)
                else:
                    cur.execute("INSERT INTO emp_salary VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (
                                     
                                self.var_emp_code.get(),
                                self.var_designation.get(),
                                self.var_name.get(),
                                self.var_age.get(),
                                self.var_gender.get(),
                                self.var_email.get(),
                                self.var_hr_location.get(),
                                self.txt_address.get('1.0',END),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_experience.get(),
                                self.var_proof_id.get(),
                                self.var_status.get(),
                                self.var_contact.get(),
                                self.var_month.get(),
                                self.var_year.get(),
                                self.var_b_salary.get(),
                                self.var_t_days.get(),
                                self.var_absent.get(),
                                self.var_medical.get(),
                                self.var_pf.get(),
                                self.var_convence.get(),
                                self.var_net_salary.get(),
                                self.var_emp_code.get()+".txt"
                                #101.txt
                                        
                            )
                            )
                mydb.commit()
                mydb.close()
                file=open('salary_reciept/'+str(self.var_emp_code.get())+".txt","w")
                file.write(self.txt_salary_reciept.get('1.0',END))
                file.close()
                self.btn_print.config(state=NORMAL)
                messagebox.showinfo("Success","Record added successfully")
               
                                    
                 
            except Exception as ex:
                messagebox.showerror("Error",f"error due to :{str(ex)}")
        
    

            
    def calculate(self):
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_b_salary.get()=='' or self.var_t_days.get()=='' or self.var_absent.get()=='' or self.var_medical.get()=='' or self.var_pf.get()=='' or self.var_convence.get()=='' or self.var_net_salary.get()=='':
            messagebox.showerror("Error","all fields are required ")
        else:
            per_day=int(self.var_b_salary.get())/int(self.var_t_days.get())
            work_day=int(self.var_t_days.get())-int(self.var_absent.get())
            sal=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal-deduct+addition
            self.var_net_salary.set(str(round(net_sal,2)))
            #----------update the recipet---
            new_sample=f'''\tCompany Name, XYZ\n\tAddress: xyz,floor 4

----------------------------------------
 Employee ID\t\t:  {self.var_emp_code.get()}
 Salary Of\t\t:  {self.var_month.get()}-{self.var_year.get()}
 Genarated On\t\t: {str(time.strftime("%d-%m-%Y"))}
---------------------------------------
 total Days\t\t:  {self.var_t_days.get()}
 total Presant\t\t:  {str(int(self.var_t_days.get())-int(self.var_absent.get()))}
 total Absent\t\t:  {self.var_absent.get()}
 Convence\t\t:  Rs.{self.var_convence.get()}
 Medical\t\t:  Rs.{self.var_medical.get()}
 Pf\t\t:  Rs.{self.var_pf.get()}
 Cross Payment\t\t:  Rs.{self.var_b_salary.get()}
 Net Salary\t\t:  Rs.{self.var_net_salary.get()}
-------------------------------------
this is computer genarated slip,not
required any signature
'''
            self.txt_salary_reciept.delete('1.0',END)
            self.txt_salary_reciept.insert(END,new_sample)
        
        
        
        
    def check_connection(self):
        try:
            mydb=mysql.connector.connect(host="localhost",port="3306",user="root",password="root",database="ems")
            cur=mydb.cursor()
            cur.execute("select*from emp_salary")
            rows=cur.fetchall()
            print(rows)
            
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')
            
            
    def show(self):
        try:
            mydb=mysql.connector.connect(host="localhost",port="3306",user="root",password="root",database="ems")
            cur=mydb.cursor()
            cur.execute("select*from emp_salary")
            rows=cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            mydb.close()
            
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')
        
    def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee PayRoll Management System | Developed By Velmurugan")
        self.root2.geometry("1000x500+120+80")
        self.root2.config(bg="white")
        title1=Label(self.root2,text="All Employee Details",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).pack(side=TOP,fill=X)
        self.root2.focus_force()
        scrooly=Scrollbar(self.root2,orient=VERTICAL)
        scroolx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrooly.pack(side=RIGHT,fill=Y)
        scroolx.pack(side=BOTTOM,fill=X)
        
        
        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id','designation','name','age','gender','email','hr_location','doj','dob','experience','proof_id','contact','status','address','month','year','b_salary','t_days','absent','medical','pf','convence','net_salary','salary_reciept'),yscrollcommand=scrooly.set,xscrollcommand=scroolx.set)
        self.employee_tree.heading('e_id',text='EID')
        self.employee_tree.heading('designation',text='designation')
        self.employee_tree.heading('name',text='name')
        self.employee_tree.heading('age',text='age')
        self.employee_tree.heading('gender',text='gender')
        self.employee_tree.heading('email',text='email')
        self.employee_tree.heading('hr_location',text='hr_location')
        self.employee_tree.heading('doj',text='doj')
        self.employee_tree.heading('dob',text='dob')
        self.employee_tree.heading('experience',text='experience')
        self.employee_tree.heading('proof_id',text='proof_id')
        self.employee_tree.heading('contact',text='contact')
        self.employee_tree.heading('status',text='status')
        self.employee_tree.heading('address',text='address')
        self.employee_tree.heading('month',text='month')
        self.employee_tree.heading('year',text='year')
        self.employee_tree.heading('b_salary',text='b_salary')
        self.employee_tree.heading('t_days',text='t_days')
        self.employee_tree.heading('absent',text='absent')
        self.employee_tree.heading('medical',text='medical')
        self.employee_tree.heading('pf',text='pf')
        self.employee_tree.heading('convence',text='convence')
        self.employee_tree.heading('net_salary',text='net_salary')
        self.employee_tree.heading('salary_reciept',text='salary_reciept')
        
        self.employee_tree['show']='headings'
        self.employee_tree.column('e_id',width=10)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=500)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('b_salary',width=100)
        self.employee_tree.column('t_days',width=100)
        self.employee_tree.column('absent',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_reciept',width=100)
        scroolx.config(command=self.employee_tree.xview)
        scrooly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        
        self.show()
        
        self.root2.mainloop()   
    def print(self):
        file_=tempfile.mktemp('.txt')
        open(file_,'w').write(self.txt_salary_reciept.get('1.0',END))    
        os.startfile(file_,"print")
        
root=Tk()
obj=EmployeeSystem(root)
root.mainloop()




