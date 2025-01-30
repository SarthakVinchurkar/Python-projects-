from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def initialize(self, window):
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
    combo_search['value'] = ('Select Option', 'Case_Id', 'Criminal_no')
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
    self.criminal_table.heading('1', text='Case_Id')
    self.criminal_table.heading('2', text='Crime_No')
    self.criminal_table.heading('3', text='Criminal Name')
    self.criminal_table.heading('4', text='NickName')
    self.criminal_table.heading('5', text='ArrestDate')
    self.criminal_table.heading('6', text='Date of Crime')
    self.criminal_table.heading('7', text='Address')
    self.criminal_table.heading('8', text='Age')
    self.criminal_table.heading('9', text='Occupation')
    self.criminal_table.heading('10', text='Birth Mark')
    self.criminal_table.heading('11', text='Crime Type')
    self.criminal_table.heading('12', text='Father Name')
    self.criminal_table.heading('13', text='Gender')
    self.criminal_table.heading('14', text='Wanted')

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
