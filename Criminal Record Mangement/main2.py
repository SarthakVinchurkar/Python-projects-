from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox as msg
import time
from getpass import getpass


class Criminal:
    def __init__(self, window):
        self.root = window
        self.root.geometry("1920x1080+0+0")
        self.root.title("Criminal Management System")

        # Variable
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthmark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()

        # Label Title
        lbl_title = Label(self.root, text="CRIMINAL MANAGEMENT SYSTEM",
                          font=('times new roman', 55, 'bold'), bg='black', fg='gold')
        lbl_title.place(x=0, y=0, width=1920, height=90)

        # Logo Image
        img_logo = Image.open('Images/Logo.png')
        img_logo = img_logo.resize((100, 86), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        lbl_logo = Label(lbl_title, image=self.photo_logo)
        lbl_logo.place(x=100, y=1, width=100, height=86)
        lbl_logo = Label(lbl_title, image=self.photo_logo)
        lbl_logo.place(x=1720, y=1, width=100, height=86)

        # Image Frame
        frm_img = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        frm_img.place(x=0, y=90, width=1920, height=260)

        # Image1
        img = Image.open('Images/police1.jpg')
        img = img.resize((640, 260), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img)

        lbl_img = Label(frm_img, image=self.photo1)
        lbl_img.place(x=0, y=0, width=640, height=260)

        # Image2
        img = Image.open('Images/Police2.jpg')
        img = img.resize((640, 260), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img)

        lbl_img = Label(frm_img, image=self.photo2)
        lbl_img.place(x=640, y=0, width=640, height=260)

        # Image3
        img = Image.open('Images/police4.jpg')
        img = img.resize((640, 260), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img)

        lbl_img = Label(frm_img, image=self.photo3)
        lbl_img.place(x=1280, y=0, width=640, height=260)

        # Main Frame
        frm_main = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        frm_main.place(x=10, y=350, width=1900, height=690)

        # Upper Frame
        frm_upr = LabelFrame(frm_main, bd=2, relief=RIDGE, text="Criminal Information",
                             font=('times new roman', 25, 'bold'), bg='white', fg='red')
        frm_upr.place(x=10, y=10, width=1880, height=335)

        # Label Entry
        xp = 4
        # Case ID
        caseId = Label(frm_upr, text="Case ID:", font=('arial', 20, 'bold'), bg='white')
        caseId.grid(row=0, column=0, padx=2, sticky=W, pady=xp)

        caseEntry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_case_id)
        caseEntry.grid(row=0, column=1, padx=2, sticky=W, pady=xp)

        # Criminal Name
        name = Label(frm_upr, text="Criminal Name:", font=('arial', 20, 'bold'), bg='white')
        name.grid(row=1, column=0, padx=2, sticky=W, pady=xp)

        nameEntry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_name)
        nameEntry.grid(row=1, column=1, padx=2, sticky=W, pady=xp)

        # Arrest Date
        date1 = Label(frm_upr, text="Arrest Date:", font=('arial', 20, 'bold'), bg='white')
        date1.grid(row=2, column=0, padx=2, sticky=W, pady=xp)

        date1Entry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_arrest_date)
        date1Entry.grid(row=2, column=1, padx=2, sticky=W, pady=xp)

        # Address
        add = Label(frm_upr, text="Address:", font=('arial', 20, 'bold'), bg='white')
        add.grid(row=3, column=0, padx=2, sticky=W, pady=xp)

        addEntry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_address)
        addEntry.grid(row=3, column=1, padx=2, sticky=W, pady=xp)

        # Occupation
        occ = Label(frm_upr, text="Occupation:", font=('arial', 20, 'bold'), bg='white')
        occ.grid(row=4, column=0, padx=2, sticky=W, pady=xp)

        occEntry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_occupation)
        occEntry.grid(row=4, column=1, padx=2, sticky=W, pady=xp)

        # Criminal Number
        cnum = Label(frm_upr, text="Criminal NO:", font=('arial', 20, 'bold'), bg='white')
        cnum.grid(row=0, column=2, padx=5, sticky=W, pady=xp)

        cnumEntry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_criminal_no)
        cnumEntry.grid(row=0, column=3, padx=2, sticky=W, pady=xp)

        # NickName
        Nname = Label(frm_upr, text="NickName:", font=('arial', 20, 'bold'), bg='white')
        Nname.grid(row=1, column=2, padx=5, sticky=W, pady=xp)

        NnameEntry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_nickname)
        NnameEntry.grid(row=1, column=3, padx=2, sticky=W, pady=xp)

        # Date of Crime as date2
        date2 = Label(frm_upr, text="Date of Crime:", font=('arial', 20, 'bold'), bg='white')
        date2.grid(row=2, column=2, padx=5, sticky=W, pady=xp)

        date2Entry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_date_of_crime)
        date2Entry.grid(row=2, column=3, padx=2, sticky=W, pady=xp)

        # Age
        age = Label(frm_upr, text="Age:", font=('arial', 20, 'bold'), bg='white')
        age.grid(row=3, column=2, padx=5, sticky=W, pady=xp)

        ageEntry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_age)
        ageEntry.grid(row=3, column=3, padx=2, sticky=W, pady=xp)

        # Birth mark
        mark = Label(frm_upr, text="Birth Mark:", font=('arial', 20, 'bold'), bg='white')
        mark.grid(row=4, column=2, padx=5, sticky=W, pady=xp)

        markEntry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_birthmark)
        markEntry.grid(row=4, column=3, padx=2, sticky=W, pady=xp)

        # Crime Type
        typo = Label(frm_upr, text="Crime Type:", font=('arial', 20, 'bold'), bg='white')
        typo.grid(row=0, column=4, padx=5, sticky=W, pady=xp)

        typoEntry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_crime_type)
        typoEntry.grid(row=0, column=5, padx=2, sticky=W, pady=xp)

        # Father Name
        father_name = Label(frm_upr, text="Father Name:", font=('arial', 20, 'bold'), bg='white')
        father_name.grid(row=1, column=4, padx=5, sticky=W, pady=xp)

        father_name_entry = ttk.Entry(frm_upr, width=20, font=('arial', 20, 'bold'), textvar=self.var_father_name)
        father_name_entry.grid(row=1, column=5, padx=2, sticky=W, pady=xp)

        # Gender
        gender = Label(frm_upr, text="Gender:", font=('arial', 20, 'bold'), bg='white')
        gender.grid(row=2, column=4, padx=5, sticky=W, pady=xp)

        # # Radio Button
        frm_radio_gender = Frame(frm_upr, bd=2, relief=RIDGE, bg='white')
        frm_radio_gender.place(x=1240, y=95, width=210, height=40)

        male = Radiobutton(frm_radio_gender, text='Male', value='male',
                           font=('arial', 16, 'bold'), bg='white', variable=self.var_gender)
        male.grid(row=0, column=0, padx=7, sticky=W)

        female = Radiobutton(frm_radio_gender, text='Female', value='female',
                             font=('arial', 15, 'bold'), bg='white', variable=self.var_gender)
        female.grid(row=0, column=1, padx=7, sticky=W)

        # Most Wanted
        wanted = Label(frm_upr, text="Most Wanted:", font=('arial', 20, 'bold'), bg='white')
        wanted.grid(row=3, column=4, padx=5, sticky=W, pady=xp)

        # # Radio Button
        frm_radio_wanted = Frame(frm_upr, bd=2, relief=RIDGE, bg='white')
        frm_radio_wanted.place(x=1240, y=145, width=170, height=40)

        yes = Radiobutton(frm_radio_wanted, text='Yes', value='yes',
                          font=('arial', 16, 'bold'), bg='white', variable=self.var_wanted)
        yes.grid(row=0, column=0, padx=7, sticky=W)

        no = Radiobutton(frm_radio_wanted, text='No', value='no',
                         font=('arial', 15, 'bold'), bg='white', variable=self.var_wanted)
        no.grid(row=0, column=1, padx=7, sticky=W)

        # Button
        frm_btn = Frame(frm_upr, bd=2, relief=RIDGE, bg='white')
        frm_btn.place(x=5, y=235, width=1048, height=50)

        # # Add Button

        btn_save = Button(frm_btn, text='Save Record', font=('arial', 16, 'bold'),
                          bg='blue', fg='white', width=19, command=self.add_data)
        btn_save.grid(row=0, column=0, padx=2, pady=2)

        btn_update = Button(frm_btn, text='Update', font=('arial', 16, 'bold'),
                            bg='blue', fg='white', width=19, command=self.update_data)
        btn_update.grid(row=0, column=1, padx=2, pady=2)

        btn_delete = Button(frm_btn, text='Delete', font=('arial', 16, 'bold'),
                            bg='blue', fg='white', width=19, command=self.delete_data)
        btn_delete.grid(row=0, column=2, padx=2, pady=2)

        btn_clear = Button(frm_btn, text='Clear', font=('arial', 16, 'bold'),
                           bg='blue', fg='white', width=19, command=self.clear_data)
        btn_clear.grid(row=0, column=3, padx=2, pady=2)

        # Side Photo
        img = Image.open('Images/Police3.jpg')
        img = img.resize((310, 285), Image.ANTIALIAS)
        self.photo4 = ImageTk.PhotoImage(img)

        lbl_img = Label(frm_upr, image=self.photo4)
        lbl_img.place(x=1558, y=0, width=310, height=285)

        # ---------------------------------------------------------------------------------------------------

        # Lower Frame
        frm_low = LabelFrame(frm_main, bd=2, relief=RIDGE, text="Criminal Information Table",
                             font=('times new roman', 20, 'bold'), bg='white', fg='red')
        frm_low.place(x=10, y=345, width=1880, height=335)

        # Search Frame
        frm_search = LabelFrame(frm_low, bd=2, relief=RIDGE, text="Search Criminal Information",
                                font=('times new roman', 20, 'bold'), bg='white', fg='red')
        frm_search.place(x=0, y=0, width=1875, height=70)

        lbl_search = Label(frm_search, text="Search By:", font=('arial', 17, 'bold'),
                           bg='red', fg='white')
        lbl_search.grid(row=0, column=0, padx=5, sticky=W)

        self.str_com_search = StringVar()
        self.str_search = StringVar()
        combo_search = ttk.Combobox(frm_search, font=('arial', 17, 'bold'),
                                    width=18, state='readonly', textvar=self.str_com_search)
        combo_search['value'] = ('Select Option', 'Crime_id', 'Criminal_no')
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=5, sticky=W)

        search_entry = ttk.Entry(frm_search, width=18, font=('arial', 17, 'bold'), textvar=self.str_search)
        search_entry.grid(row=0, column=2, padx=5, sticky=W)

        btn_search = Button(frm_search, text='Search', font=('arial', 13, 'bold'),
                            bg='blue', fg='white', width=18, command=self.search_data)
        btn_search.grid(row=0, column=3, padx=5, sticky=W)

        btn_all = Button(frm_search, text='Show All', font=('arial', 13, 'bold'),
                         bg='blue', fg='white', width=18, command=self.show_all_data)
        btn_all.grid(row=0, column=4, padx=5, sticky=W)

        lbl_tlt = Label(frm_search, text="SECRET INTELLIGENCE SERVICE MI6",
                        font=('times new roman', 19, 'bold'), bg='black', fg='crimson')
        lbl_tlt.place(x=1150, y=0, width=700, height=35)

        # Table Frame
        frm_table = Frame(frm_low, bd=2, relief=RIDGE)
        frm_table.place(x=0, y=70, width=1875, height=230)

        # # ScrollBar With Table
        scroll_x = ttk.Scrollbar(frm_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(frm_table, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(frm_table, column=('1', '2', '3', '4', '5', '6', '7',
                                                              '8', '9', '10', '11', '12', '13', '14'),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        # Add Heading to Table
        self.criminal_table.heading('12', text='Case_Id')
        self.criminal_table.heading('1', text='Crime_No')
        self.criminal_table.heading('2', text='Criminal Name')
        self.criminal_table.heading('3', text='NickName')
        self.criminal_table.heading('4', text='ArrestDate')
        self.criminal_table.heading('13', text='Date of Crime')
        self.criminal_table.heading('5', text='Address')
        self.criminal_table.heading('6', text='Age')
        self.criminal_table.heading('7', text='Occupation')
        self.criminal_table.heading('11', text='Birth Mark')
        self.criminal_table.heading('14', text='Crime Type')
        self.criminal_table.heading('8', text='Father Name')
        self.criminal_table.heading('9', text='Gender')
        self.criminal_table.heading('10', text='Wanted')

        xp = 132
        self.criminal_table.column('1', width=xp)
        self.criminal_table.column('2', width=xp)
        self.criminal_table.column('3', width=xp)
        self.criminal_table.column('4', width=xp)
        self.criminal_table.column('5', width=xp)
        self.criminal_table.column('6', width=xp)
        self.criminal_table.column('7', width=xp)
        self.criminal_table.column('8', width=xp)
        self.criminal_table.column('9', width=xp)
        self.criminal_table.column('10', width=xp)
        self.criminal_table.column('11', width=xp)
        self.criminal_table.column('12', width=xp)
        self.criminal_table.column('13', width=xp)
        self.criminal_table.column('14', width=xp)

        self.criminal_table['show'] = 'headings'

        self.criminal_table.pack(fill=BOTH, expand=1)
        self.criminal_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    # Add Data
    def add_data(self):
        if self.var_case_id == "" or self.var_criminal_no == "":
            msg.showerror("Error", "All Fields are Required")

        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root',
                                               password='$mit2311', database='management2')
                my_curs = conn.cursor()
                if self.var_criminal_no == "":
                    my_curs.execute("insert into crime values(%s, %s, %s)",
                                    (
                                        self.var_case_id.get(),
                                        self.var_date_of_crime.get(),
                                        self.var_crime_type.get(),
                                    ))

                elif self.var_case_id == "":
                    my_curs.execute("insert into criminals values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                    (
                                        self.var_criminal_no.get(),
                                        self.var_name.get(),
                                        self.var_nickname.get(),
                                        self.var_arrest_date.get(),
                                        self.var_address.get(),
                                        self.var_age.get(),
                                        self.var_occupation.get(),
                                        self.var_father_name.get(),
                                        self.var_gender.get(),
                                        self.var_wanted.get(),
                                        self.var_birthmark.get()
                                    ))

                else:
                    try:
                        my_curs.execute("insert into criminals values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                        (
                                            self.var_criminal_no.get(),
                                            self.var_name.get(),
                                            self.var_nickname.get(),
                                            self.var_arrest_date.get(),
                                            self.var_address.get(),
                                            self.var_age.get(),
                                            self.var_occupation.get(),
                                            self.var_father_name.get(),
                                            self.var_gender.get(),
                                            self.var_wanted.get(),
                                            self.var_birthmark.get()
                                        ))

                        my_curs.execute("insert into crime values(%s, %s, %s)",
                                        (
                                            self.var_case_id.get(),
                                            self.var_date_of_crime.get(),
                                            self.var_crime_type.get()
                                        ))
                    finally:
                        my_curs.execute("insert into crime values(%s, %s)",
                                        (
                                            self.var_case_id.get(),
                                            self.var_criminal_no.get()
                                        ))

                conn.commit()
                conn.close()
                self.fetch_data()
                self.clear_data()
                msg.showinfo("Success", "Criminal record has been added")

            except Exception as es:
                msg.showerror("Error", f"Due to {es}")

    # Fetch Data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root',
                                       password='$mit2311', database='management2')
        my_curs = conn.cursor()
        my_curs.execute("select * from criminals c1 join map m on c1.Criminal_no=m.Criminal_no "
                        "join crime c2 on c2.Crime_id=m.Crime_id where 1")
        data = my_curs.fetchall()
        if len(data) != 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for item in data:
                self.criminal_table.insert("", END, value=item)
            conn.commit()
        conn.close()

    # get Cursor
    def get_cursor(self, event=""):
        cursor_row = self.criminal_table.focus()
        data = self.criminal_table.item(cursor_row)["values"]

        self.var_case_id.set(data[11])
        self.var_criminal_no.set(data[0])
        self.var_name.set(data[1])
        self.var_nickname.set(data[2])
        self.var_arrest_date.set(data[3])
        self.var_date_of_crime.set(data[12])
        self.var_address.set(data[4])
        self.var_age.set(data[5])
        self.var_occupation.set(data[6])
        self.var_birthmark.set(data[10])
        self.var_crime_type.set(data[13])
        self.var_father_name.set(data[7])
        self.var_gender.set(data[8])
        self.var_wanted.set(data[9])

    # Update
    def update_data(self):
        if self.var_case_id == "":
            msg.showerror("Error", "All Fields are Required")

        else:
            try:
                is_update = msg.askyesno("Update", "Are you sure update criminal record")
                if is_update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root',
                                                   password='$mit2311', database='management2')
                    my_curs = conn.cursor()
                    query = "update criminals set Criminal_no=%s,Criminal_name=%s,Nick_name=%s," \
                            "Arrest_date=%s,Address=%s,Age=%s,Occupation=%s," \
                            "BirthMark=%s,Father_name=%s,Gender=%s,Wanted=%s where 1"
                    my_curs.execute(query,
                                    (
                                        self.var_criminal_no.get(),
                                        self.var_name.get(),
                                        self.var_nickname.get(),
                                        self.var_arrest_date.get(),
                                        self.var_address.get(),
                                        self.var_age.get(),
                                        self.var_occupation.get(),
                                        self.var_birthmark.get(),
                                        self.var_father_name.get(),
                                        self.var_gender.get(),
                                        self.var_wanted.get()
                                    ))

                    query = "update crime set Criminal_no=%s,CrimeType=%s,Date_of_crime=%s," \
                            "Crime_id=%s where 1"
                    my_curs.execute(query,
                                    (
                                        self.var_criminal_no.get(),
                                        self.var_crime_type.get(),
                                        self.var_date_of_crime.get(),
                                        self.var_case_id.get()
                                    ))

                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    self.clear_data()
                    msg.showinfo("Success", "Criminal record has been Successfully Updated")

            except Exception as es:
                msg.showerror("Error", f"Due to {es}")

    # Delete
    def delete_data(self):
        if self.var_case_id == "":
            msg.showerror("Error", "All Fields are Required")

        else:
            try:
                is_delete = msg.askyesno("Update", "Are you sure delete criminal record")
                if is_delete > 0:
                    conn = mysql.connector.connect(host='localhost', username='root',
                                                   password='$mit2311', database='management2')
                    my_curs = conn.cursor()
                    query = "delete from crime where Criminal_no=%s"
                    my_curs.execute(query, (self.var_criminal_no.get(),))
                    query = "delete from criminals where Criminal_no=%s"
                    my_curs.execute(query, (self.var_criminal_no.get(),))

                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    self.clear_data()
                    msg.showinfo("Success", "Criminal record has been Successfully Deleted")

            except Exception as es:
                msg.showerror("Error", f"Due to {es}")

    # Clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    # Search
    def search_data(self):
        if self.str_com_search.get() == "":
            msg.showerror("Error", "All Fields are Required")

        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root',
                                               password='$mit2311', database='management2')
                my_curs = conn.cursor()
                my_curs.execute('select * from criminals c1 join crime c2 on c1.Criminal_no=c2.Criminal_no where ' + str(self.str_com_search.get()) +
                                " LIKE'%" + str(self.str_search.get()) + "%'")

                rows = my_curs.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for item in rows:
                        self.criminal_table.insert("", END, values=item)
                conn.commit()
                conn.close()

                if len(rows) == 0:
                    msg.showinfo("Not Fount", "Criminal with given data not found\ntry again")
                    self.fetch_data()

            except Exception as es:
                msg.showerror("Error", f"Due to {es}")

    # Show All
    def show_all_data(self):
        self.fetch_data()


credential = False


def login(usr_name, pas, rootx):
    username = usr_name.get()
    password = pas.get()

    if(username == "") and (password == ""):
        global credential
        credential = True
        rootx.quit()

    else:
        msg.showinfo("Invalid", "Invalid Credential!\nTry Again")

    usr_name.set("")
    pas.set("")


def Auth(rootx):
    rootx.geometry("1080x540")
    rootx.title("Authenticating")

    usr_name = StringVar()
    pas = StringVar()

    # Upper Frame
    frm_upr = LabelFrame(rootx, bd=2, relief=RIDGE, text="Authentication",
                         font=('times new roman', 50, 'bold'), bg='grey', fg='black')
    frm_upr.place(x=10, y=10, width=1060, height=520)

    # Image
    img = Image.open('Images/back1.jpg')
    img = img.resize((1045, 500), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(img)

    lbl_img = Label(frm_upr, image=photo1)
    lbl_img.place(x=5, y=190, width=1045, height=245)

    # Label Entry
    xp = 15
    y = 40

    # Username
    username = Label(frm_upr, text="Username :", font=('arial', y, 'bold'), bg='grey')
    username.grid(row=0, column=0, padx=50, pady=xp)

    usernameEntry = ttk.Entry(frm_upr, width=20, font=('arial', y, 'bold'), textvar=usr_name)
    usernameEntry.grid(row=0, column=1, padx=0, pady=xp)

    # password
    password = Label(frm_upr, text="Password :", font=('arial', y, 'bold'), bg='grey')
    password.grid(row=1, column=0, padx=2, pady=xp)

    passwordEntry = ttk.Entry(frm_upr, width=20, font=('arial', y, 'bold'), textvar=pas)
    passwordEntry.grid(row=1, column=1, padx=0, pady=xp)

    btn_login = Button(frm_upr, text='Login', font=('arial', 25, 'bold'),
                       bg='red', fg='white', width=20, command=lambda: login(usr_name, pas, rootx))
    btn_login.grid(row=2, column=1, padx=2, pady=15)

    rootx.mainloop()


if __name__ == '__main__':

    root = Tk()
    Auth(root)

    if credential:
        obj = Criminal(root)
        root.mainloop()
