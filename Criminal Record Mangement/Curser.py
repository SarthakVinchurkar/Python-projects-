
def get_cursor(self, event=""):
    cursor_row = self.criminal_table.focus()
    data = self.criminal_table.item(cursor_row)["values"]

    self.var_case_id.set(data[0])
    self.var_criminal_no.set(data[1])
    self.var_name.set(data[2])
    self.var_nickname.set(data[3])
    self.var_arrest_date.set(data[4])
    self.var_date_of_crime.set(data[5])
    self.var_address.set(data[6])
    self.var_age.set(data[7])
    self.var_occupation.set(data[8])
    self.var_birthmark.set(data[9])
    self.var_crime_type.set(data[10])
    self.var_father_name.set(data[11])
    self.var_gender.set(data[12])
    self.var_wanted.set(data[13])
