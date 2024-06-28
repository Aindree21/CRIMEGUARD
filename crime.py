from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#import mysql.connector

class Criminal:
    def __init__ (self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        lbl_title=Label(self.root, text='CRIMEGUARD REGISTER',font=('times new roman',40, 'bold'), bg='black', fg='gold')
        lbl_title.place(x=0, y=0,width=1530,height=70)

        img_logo= Image.open('Image\logo.jpeg')
        img_logo= img_logo.resize((70,70), Image.ANTIALIAS)
        self.photo_logo=ImageTk. PhotoImage(img_logo)
        self.logo=Label(self.root, image=self.photo_logo)
        self.logo.place(x=150, y=5,width=60,height=68)

        #variable
        self.var_case_id=StringVar()
        self.var_name=StringVar()
        self.var_arrest_date=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_birthmark= StringVar()
        self.var_father_name=StringVar()
        self.var_crime_type=StringVar()
        self.var_mobile=StringVar()
        self.var_gender=StringVar()

        




        # Img Frame
        img_frame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=70,width=1530,height=138)

        img1=Image.open('Image\cyber-training.jpg')
        img1=img1.resize((1540,360), Image.ANTIALIAS)
        self.photol=ImageTk.PhotoImage(img1)
        self.img_1=Label(img_frame, image=self.photol)
        self.img_1.place(x=0,y=0,width=1530,height=160)

        # Main Frame
        Main_frame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=200, width=1500, height=560)
        
        #upper frame
        upper_frame=LabelFrame(Main_frame, bd=2, relief=RIDGE, text='INFORMATION',font=('times new roman',11, 'bold'),  fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1480, height=270)

        # Labels Entry
        # case id
        caseid=Label(upper_frame, text='Case ID: ', font=('arial',11, 'bold'),bg='white')
        caseid.grid(row=0,column=0, padx=2,sticky=W)
        caseentry=ttk. Entry(upper_frame,textvariable= self.var_case_id,width=22, font=('arial', 11, "bold"))
        caseentry.grid(row=0, column=1, padx=2, sticky=W)
       # Criminal Name
        lb1_Name = Label(upper_frame, font=("arial", 12, "bold"), text="Criminal Name : ",bg="white")
        lb1_Name.grid (row=1, column=0, sticky=W, padx=2, pady=7)
        txt_Name=ttk. Entry(upper_frame, textvariable= self.var_name,width=22, font=("arial", 11, "bold"))
        txt_Name.grid(row=1, column=1, sticky=W, padx=2, pady=7)
        # address
        lb1_address = Label(upper_frame, font=("arial", 12, "bold"), text="Address : ",bg="white")
        lb1_address.grid (row=2, column=0, sticky=W, padx=2, pady=7)
        txt_address=ttk. Entry(upper_frame,  textvariable= self.var_address,width=22, font=("arial", 11, "bold"))
        txt_address.grid(row=2, column=1, sticky=W, padx=2, pady=7)

        # Crime Type
        lb1_crimeType=Label (upper_frame, font=("arial", 12, "bold"), text="Crime Type : ",bg="white")
        lb1_crimeType.grid(row=0, column=4, sticky=W, padx=2, pady=7)
        txt_crimeType=ttk. Entry(upper_frame, textvariable= self.var_crime_type, width=22, font=("arial", 11, "bold"))
        txt_crimeType.grid (row=0, column=5, padx=2, pady=7)
        # # Father Name
        lbl_fatherName=Label(upper_frame, font=("arial", 12, "bold"), text="Father Name:", bg="white")
        lbl_fatherName.grid (row=5,column=0, sticky=W, padx=2, pady=7)
        txt_fatherName=ttk. Entry(upper_frame,textvariable= self.var_case_id, width=22, font=("arial", 11, "bold"))
        txt_fatherName.grid(row=5, column=1, padx=2, pady=7)
        #Mobile
        mobile=Label(upper_frame, text='Mobile_No ', font=('arial',11, 'bold'),bg='white')
        mobile.grid(row=4,column=0, padx=2,sticky=W)
        mobileentry=ttk. Entry(upper_frame,textvariable= self.var_mobile, width=22, font=('arial', 11, "bold"))
        mobileentry.grid(row=4, column=1, padx=2, sticky=W)
        # gender
        lbl_gender=Label(upper_frame, font=("arial", 12, "bold"), text="Gender:", bg="white")
        lbl_gender.grid (row=4,column=4, sticky=W, padx=2, pady=7)
        txt_gender=ttk. Entry(upper_frame, textvariable= self.var_gender,width=22, font=("arial", 11, "bold"))
        txt_gender.grid(row=4, column=5, padx=2, pady=7)
        # birth mark
        lbl_birthmark=Label(upper_frame, font=("arial", 12, "bold"), text="Birth mark:", bg="white")
        lbl_birthmark.grid (row=1,column=4, sticky=W, padx=2, pady=7)
        txt_birthmark=ttk. Entry(upper_frame, textvariable= self.var_birthmark,width=22, font=("arial", 11, "bold"))
        txt_birthmark.grid(row=1, column=5, padx=2, pady=7)
        # AGE
        lbl_age=Label(upper_frame, font=("arial", 12, "bold"), text="Criminal's Age:", bg="white")
        lbl_age.grid (row=2,column=4, sticky=W, padx=2, pady=7)
        txt_age=ttk. Entry(upper_frame,textvariable= self.var_age, width=22, font=("arial", 11, "bold"))
        txt_age.grid(row=2, column=5, padx=2, pady=7)
        #image
        f=Frame(upper_frame, bd=3,bg="black",width=200,height=200,relief=GROOVE)
        f.place (x=900, y=0)
        img=PhotoImage(file="Image\download.png")
        lbl=Label(upper_frame,bg="black",image=img)
        lbl.place(x=900,y=0, width="200",height="200")

        #btn_upload=Button(upper_frame, text='upload', font=("arial", 13,"bold"), width=14, bg='red', fg='white')
        #btn_upload.grid(row=15,column=15,sticky=W,padx=5)

        # down frame
        down_frame=LabelFrame(Main_frame, bd=2, relief=RIDGE, text='INFORMATION TABLE',font=('times new roman',11, 'bold'),  fg='red', bg='white')
        down_frame.place(x=10, y=280, width=1480, height=270)
        # search frame
        search_frame=LabelFrame(down_frame, bd=2, relief=RIDGE, text='search',font=('times new roman',11, 'bold'),  fg='red', bg='white')
        search_frame.place(x=0, y=0, width=1480, height=60)

        search_by=Label(search_frame, font=("arial", 11, "bold"), text="Search:", bg="red", fg="white")
        search_by.grid (row=0,column=0, sticky=W, padx=2, pady=5)
        combo_search_box=ttk.Combobox(search_frame,font=("arial", 11, "bold"),width=18 , state="readonly")
        combo_search_box['value']=('Select Option','Case_id','Criminal Name')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1, sticky=W,padx=5)

        search_txt=ttk.Entry(search_frame,width=18, font=("arial", 11, "bold")) 
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        # search
        btn_search=Button(search_frame,text='Search', font=("arial", 13, "bold"), width=14, bg='red', fg='white')
        btn_search.grid(row=0,column=3,sticky=W,padx=5)
        #all
        btn_all=Button(search_frame, text='All record', font=("arial", 13,"bold"), width=14, bg='red', fg='white')
        btn_all.grid(row=0,column=4,sticky=W,padx=5)

        table_frame=Frame(down_frame,bd=2, relief=RIDGE)

        table_frame.place(x=0,y=60,width=1470,height=170)

        
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=TOP, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)
        
        self.criminal_table.heading('1', text='CaseId')
        self.criminal_table.heading("2",text="Criminal Name")
        self.criminal_table.heading("3", text="Address")

        self.criminal_table.heading("4", text="Age")



        self.criminal_table.heading("5", text="Birth Mark")

        self.criminal_table.heading("6", text="Crime Type") 
        self.criminal_table.heading("7", text="Father Name")
        self.criminal_table.heading("8", text="Gender")

        self.criminal_table.pack(fill=BOTH, expand=1)
        self.criminal_table['show']='headings'






        #button
        button_frame=Frame(upper_frame,bd=2, relief=RIDGE, bg="white")

        button_frame.place(x=5,y=200, width=620,height=45)
        #add button
        btn_add=Button(button_frame, text='Record Save', font=("arial", 13, "bold"),width=14,  bg='red', fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)
        #update
        btn_update=Button(button_frame,text='Update', font=("arial", 13, "bold"),width=14, bg='red', fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)
        #clear
        btn_clear=Button(button_frame,text='Upload', font=("arial", 13, "bold"), width=14, bg='red', fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)
        #delete
        btn_delete=Button(button_frame, text='Delete', font=("arial", 13,"bold"), width=14, bg='red', fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

       
        

if  __name__== "__main__":
    root=Tk()
    obj= Criminal(root)
    root.mainloop()