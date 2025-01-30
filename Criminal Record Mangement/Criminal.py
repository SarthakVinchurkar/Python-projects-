import Insert
import Interface
import Curser
import Retrive
import Find
import Delete
import Update


class Criminal:
    def __init__(self, window):
        Interface.initialize(self, window)

    # Add Data
    def add_data(self):
        Insert.add_data(self)

    # Fetch Data
    def fetch_data(self):
        Retrive.fetch_data(self)

    # get Cursor
    def get_cursor(self, event=""):
        Curser.get_cursor(self)

    # Update
    def update_data(self):
        Update.update_data(self)

    # Delete
    def delete_data(self):
        Delete.delete_data(self)

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
        Find.search_data(self)

    # Show All
    def show_all_data(self):
        Retrive.fetch_data(self)
