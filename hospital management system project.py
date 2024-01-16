
from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import  mysql.connector



class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management system")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ReferenceNo=StringVar()
        self.Dose=StringVar()
        self.Nooftablets=StringVar()
        self.Lot=StringVar()
        self.issueDate=StringVar()
        self.sideEffect=StringVar()
        self.Furtherinfo=StringVar()
        self.Bloodpressure=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.storage=StringVar()
        self.Medication=StringVar()
        self.patientid=StringVar()
        self.NHSNumber=StringVar()
        self.patientname=StringVar()
        self.dateofbirth=StringVar()
        self.patientaddress=StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("Times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #============================================================== Dataframe ============================================================================

        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,padx=10,relief=RIDGE,
                                                font=("arial",12,"bold"),text="patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,padx=10,relief=RIDGE,
                                                font=("arial",12,"bold"),text="prescription")
        DataFrameRight.place(x=990,y=5,width=460,height=350)

        #============================================================ buttuonframe ==============================================================================
        
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        #=========================================================== Details frame ==============================================================================

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        #=========================================================== DataframeLeft =============================================================================

        lblNameTablet=Label(DataFrameLeft,text="Names of Tablet:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,state="readonly",
                                                        font=("arial",12,"bold"),width=33)
        comNameTablet['value']=("Nice","corona vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,textvariable=self.ReferenceNo,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataFrameLeft,font=("arial",13,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,textvariable=self.Dose,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNooftablets=Label(DataFrameLeft,font=("arial",13,"bold"),text="No of tablets:",padx=2,pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        txtnooftablets=Entry(DataFrameLeft,textvariable=self.Nooftablets,font=("arial",13,"bold"),width=35)
        txtnooftablets.grid(row=3,column=1)

        lblLot=Label(DataFrameLeft,font=('arial',13,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,textvariable=self.Lot,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft,textvariable=self.issueDate,font=("arial",13,"bold"),width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,textvariable=self.ExpDate,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,textvariable=self.DailyDose,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)

        lblsideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="side Effect:",padx=2,pady=6)
        lblsideEffect.grid(row=8,column=0,sticky=W)
        txtsideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect,font=("arial",13,"bold"),width=35)
        txtsideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further info:",padx=2,pady=6)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataFrameLeft,textvariable=self.Furtherinfo,font=("arial",12,"bold"),width=35)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodpressure=Label(DataFrameLeft,font=("arial",12,"bold"),text="Bloodpressure:",padx=2,pady=6)
        lblBloodpressure.grid(row=1,column=2)
        txtBloodpressure=Entry(DataFrameLeft,textvariable=self.Bloodpressure,font=("arial",13,"bold"),width=35)
        txtBloodpressure.grid(row=1,column=3)

        lblstorage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblstorage.grid(row=2,column=2)
        txtstorage=Entry(DataFrameLeft,textvariable=self.storage,font=("arial",13,"bold"),width=35)
        txtstorage.grid(row=2,column=3)

        lblMedication=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedication.grid(row=3,column=2,sticky=W)
        txtMedication=Entry(DataFrameLeft,textvariable=self.Medication,font=("arial",13,"bold"),width=35)
        txtMedication.grid(row=3,column=3)

        lblpatientid=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblpatientid.grid(row=4,column=2,sticky=W)
        txtpatientid=Entry(DataFrameLeft,textvariable=self.patientid,font=("arial",13,"bold"),width=35)
        txtpatientid.grid(row=4,column=3)

        lblNHSNumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNHSNumber.grid(row=5,column=2,sticky=W)
        txtNHSNumber=Entry(DataFrameLeft,textvariable=self.NHSNumber,font=("arial",13,"bold"),width=35)
        txtNHSNumber.grid(row=5,column=3)

        lblpatientname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblpatientname.grid(row=6,column=2,sticky=W)
        txtpatientname=Entry(DataFrameLeft,textvariable=self.patientname,font=("arial",13,"bold"),width=35)
        txtpatientname.grid(row=6,column=3)

        lbldateofbirth=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lbldateofbirth.grid(row=7,column=2,sticky=W)
        txtdateofbirth=Entry(DataFrameLeft,textvariable=self.dateofbirth,font=('arial',12,"bold"),width=35)
        txtdateofbirth.grid(row=7,column=3)

        lblpatientaddress=Label(DataFrameLeft,font=("arial",12,"bold"),text="patient Address:",padx=2,pady=6)
        lblpatientaddress.grid(row=8,column=2,sticky=W)
        txtpatientaddress=Entry(DataFrameLeft,textvariable=self.patientaddress,font=("arial",12,"bold"),width=35)
        txtpatientaddress.grid(row=8,column=3)

        #============================================================== DataFrameRight ========================================================================

        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #================================================================== Buttons ========================================================================

        btnPrescription=Button(Buttonframe,bg="green",fg="white",text="Prescription",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)


        btnPrescriptionData=Button(Buttonframe,text="Prescripton Data",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)
         

        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnclear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnclear.grid(row=0,column=4)


        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

#==================================================================== table =========================================================================================
#================================================================== scrollbar ==========================================================================================

        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablets","ref","dose","nooftablets","lot","issuedate",
                                    "expdate","dailydose","storage","nhsnumber","pname","dob","patientaddress"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM,fill =X)
        scroll_y.pack(side = RIGHT,fill =Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets",text="Name of tablets")
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Paitient Name")
        self.hospital_table.heading("dob",text="Date of birth")
        self.hospital_table.heading("patientaddress",text="patientaddress")
        
        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("patientaddress",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor) 


        self.fetch_data()

#============================================================== Functionality Declaration =====================================================================

    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ReferenceNo.get()=="":
            messagebox.showerror("Error","all fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Saikumar@9618",database="Mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",(
                                                                                                    self.Nameoftablets.get(),
                                                                                                    self.ReferenceNo.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.Nooftablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.issueDate.get(),
                                                                                                    self.sideEffect.get(),
                                                                                                    self.Furtherinfo.get(),
                                                                                                    self.Bloodpressure.get(),
                                                                                                    self.ExpDate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    self.storage.get(),
                                                                                                    self.Medication.get(),
                                                                                                    self.patientid.get(),
                                                                                                    self.NHSNumber.get(),
                                                                                                    self.patientname.get(),
                                                                                                    self.dateofbirth.get(),
                                                                                                    self.patientaddress.get(),

                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Saikumar@9618",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["value"]
        self.Nameoftablets.set(row[0])
        self.ReferenceNo.set(row[1])
        self.Dose.set(row[2])
        self.Nooftablets.set(row[3])
        self.Lot.set(row[4])
        self.issueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.storage.set(row[8])
        self.NHSNumber.set(row[9])
        self.patientname.set(row[10])
        self.dateofbirth.set(row[11])
        








if __name__=="__main__":
   root=Tk()
   ob=Hospital(root)
   root.mainloop()