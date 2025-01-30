import mysql.connector
from tkinter import messagebox as msg


def delete_data(self):
    if self.var_case_id == "":
        msg.showerror("Error", "All Fields are Required")

    else:
        try:
            is_delete = msg.askyesno("Update", "Are you sure delete criminal record")
            if is_delete > 0:
                conn = mysql.connector.connect(host='localhost', username='root',
                                               password='$mit2311', database='management')
                my_curs = conn.cursor()
                query = "delete from criminals where Case_Id=%s AND Criminal_no=%s"
                my_curs.execute(query, (self.var_case_id.get(), self.var_criminal_no.get()))

                conn.commit()
                conn.close()
                self.fetch_data()
                self.clear_data()
                msg.showinfo("Success", "Criminal record has been Successfully Deleted")

        except Exception as es:
            msg.showerror("Error", f"Due to {es}")