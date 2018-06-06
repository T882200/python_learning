from tkinter import *
from tkinter import ttk
import sqlite3



class StudentDB:

    #Fields
    db_conn = 0
    theCursor= 0
    curr_student = 0

    def setup_db(self):
        self.db_conn = sqlite3.connect('student.db')

        self.theCursor = self.db_conn.cursor()
        try:
            self.db_conn.execute("CREATE TABLE if not exists Students(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL);")

            self.db_conn.commit()

        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")

        print("Setup DB")

    def stud_submit(self):

        self.db_conn.execute("INSERT INTO Students(FName, LName)" +
        "VALUES ('" +
        self.fn_entry_value.get() +"', '"+
        self.ln_entry_value.get() +"')")

        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")

        self.update_listbox()

        print("Submit Stud")

    def update_listbox(self):

        self.list_box.delete(0, "end")

        try:
            result = self.theCursor.execute("SELECT ID, FName, LName FROM Students")
            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]

                self.list_box.insert(stud_id,
                                 stud_fname + " " +
                                 stud_lname)

        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")

        except:
            print("1: Couldn't Retrieve Data From Database")

        print("Update LB")

    def load_student(self, event=None):

        lb_widget = event.widget
        index = str(lb_widget.curselection()[0] + 1)

        self.curr_student = index

        try:
            result = self.theCursor.execute("SELECT ID, FName, LName FROM Students WHERE ID=" + index)
            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]

                self.fn_entry_value.set(stud_fname)
                self.ln_entry_value.set(stud_lname)

        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")

        except:
            print("2: Couldn't Retrieve Data From Database")

        print("Load Stud")

    def update_student(self):

        try:
            self.db_conn.execute("UPDATE Students SET FName='"+
                                 self.fn_entry_value.get()+
                                 "', LName='" +
                                 self.ln_entry_value.get()+
                                 "' WHERE ID='" +
                                 self.curr_student)

            self.db_conn.commit()

        except sqlite3.OperationalError:
            print("Database couldn't be Updated")

        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")

        self.update_listbox()

        print("Update Stud")

    def __init__(self, root):
        root.title("Student Database")

        root.geometry("250x350")

        #1st row

        fn_label = Label(root, text="First Name")
        fn_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.fn_entry_value = StringVar(root, value="")
        self.fn_entry = ttk.Entry(root,
                                  textvariable=self.fn_entry_value)

        self.fn_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        #2nd row

        ln_label = Label(root, text="Last Name")
        ln_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.ln_entry_value = StringVar(root, value="")
        self.ln_entry = ttk.Entry(root,
                                  textvariable=self.ln_entry_value)

        self.ln_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        #3rd row

        self.submit_button = ttk.Button(root,
                                        text="Submit",
                                        command = lambda: self.stud_submit())
        self.submit_button.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.update_button = ttk.Button(root,
                                        text="Update",
                                        command = lambda: self.update_student())
        self.update_button.grid(row=2, column=1, padx=10, pady=10, sticky=E)

        #4th row

        scrollbar = Scrollbar(root)

        self.list_box = Listbox(root)

        self.list_box.bind('<<ListboxSelect>>', self.load_student)

        self.list_box.insert(1, "Students Here")

        self.list_box.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky=W+E)

        self.setup_db()

        self.update_listbox()

root = Tk()

studDB = StudentDB(root)

root.mainloop()










