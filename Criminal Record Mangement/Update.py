import mysql.connector
from tkinter import messagebox as msg


def update_data(self):
    if self.var_case_id == "":
        msg.showerror("Error", "All Fields are Required")

    else:
        try:
            is_update = msg.askyesno("Update", "Are you sure update criminal record")
            if is_update > 0:
                conn = mysql.connector.connect(host='localhost', username='root',
                                               password='$mit2311', database='management')
                my_curs = conn.cursor()
                query = "update criminals set Criminal_no=%s,Criminal_name=%s,Nick_name=%s," \
                        "Arrest_date=%s,Date_of_crime=%s,Address=%s,Age=%s,Occupation=%s," \
                        "BirthMark=%s,CrimeType=%s,Father_name=%s,Gender=%s,Wanted=%s where " \
                        "Case_Id=%s AND Criminal_no=%s"
                my_curs.execute(query,
                                (
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
                                    self.var_wanted.get(),
                                    self.var_case_id.get(),
                                    self.var_criminal_no.get()
                                ))

                conn.commit()
                conn.close()
                self.fetch_data()
                self.clear_data()
                msg.showinfo("Success", "Criminal record has been Successfully Updated")

        except Exception as es:
            msg.showerror("Error", f"Due to {es}")
