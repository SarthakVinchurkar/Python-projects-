import mysql.connector
from tkinter import messagebox as msg


def add_data(self):
    if self.var_case_id.get() == "" or self.var_criminal_no.get() == "":
        msg.showerror("Error", "All Fields are Required")

    else:
        try:
            conn = mysql.connector.connect(host='localhost', username='root',
                                           password='$mit2311', database='management')
            my_curs = conn.cursor()
            my_curs.execute("insert into criminals values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (
                                self.var_case_id.get(),
                                self.var_criminal_no.get(),
                                self.var_name.get(),
                                self.var_nickname.get(),
                                self.var_arrest_date.get(),
                                self.var_date_of_crime.get(),
                                self.var_address.get(),
                                self.var_age.get(),
                                self.var_occupation.get(),
                                self.var_birthmark.get(),
                                self.var_crime_type.get(),
                                self.var_father_name.get(),
                                self.var_gender.get(),
                                self.var_wanted.get()
                            ))

            conn.commit()
            conn.close()
            self.fetch_data()
            self.clear_data()
            msg.showinfo("Success", "Criminal record has been added")

        except Exception as es:
            msg.showerror("Error", f"Due to {es}")
