from tkinter import *
import mysql.connector


def fetch_data(self):
    conn = mysql.connector.connect(host='localhost', username='root',
                                   password='$mit2311', database='management')
    my_curs = conn.cursor()
    my_curs.execute("select * from criminals")
    data = my_curs.fetchall()
    if len(data) != 0:
        self.criminal_table.delete(*self.criminal_table.get_children())
        for item in data:
            self.criminal_table.insert("", END, value=item)
        conn.commit()
    conn.close()
