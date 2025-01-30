from tkinter import *
import mysql.connector
from tkinter import messagebox as msg


def search_data(self):
    if self.str_com_search.get() == "":
        msg.showerror("Error", "All Fields are Required")

    else:
        try:
            conn = mysql.connector.connect(host='localhost', username='root',
                                           password='$mit2311', database='management')
            my_curs = conn.cursor()
            my_curs.execute('select * from criminals where ' + str(self.str_com_search.get()) +
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
