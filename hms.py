import tkinter.ttk
import tkinter
import tkinter.messagebox
import sqlite3


class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("dbFile.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute(
            "CREATE TABLE IF NOT EXISTS doctor_info (id PRIMARYKEY text, fname text, lname text, gender text, speciality text, phone text, email text )")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    # doctor info
    def Insertd(self, id, fname, lname, gender, speciality, phone, email):
        self.dbCursor.execute("INSERT INTO doctor_info VALUES (?, ?, ?, ?, ?, ?,?)", (
            id, fname, lname, gender, speciality, phone, email))
        self.dbConnection.commit()

    def Updated(self, id, fname, lname, gender, speciality, phone, email):
        self.dbCursor.execute(
            "UPDATE doctor_info SET fname = ?, lname = ?,gender = ?, speciality = ?, phone = ?, email = ?",
            (fname, lname, gender, speciality, phone, email))
        self.dbConnection.commit()

    def Deleted(self, id):
        self.dbCursor.execute("DELETE FROM doctor_info WHERE id = ?", (id,))
        self.dbConnection.commit()

    def Displayd(self):
        self.dbCursor.execute("SELECT * FROM doctor_info")
        records = self.dbCursor.fetchall()
        return records

    # patient info

    def Insertp(self, id, fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, history, doctor):
        self.dbCursor.execute("INSERT INTO patient_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            id, fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, history, doctor))
        self.dbConnection.commit()

    def Updatep(self, fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, history, doctor,id):
        self.dbCursor.execute(
            "UPDATE patient_info SET fName = ?, lName = ?, dob = ?, mob = ?, yob = ?, gender = ?, address = ?, phone = ?, email = ?, bloodGroup = ?, history = ?, doctor = ? WHERE id = ?",
            (fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, history, doctor, id))
        self.dbConnection.commit()

    def Searchp(self, id):
        self.dbCursor.execute("SELECT * FROM patient_info WHERE id = ?", (id,))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Deletep(self, id):
        self.dbCursor.execute("DELETE FROM patient_info WHERE id = ?", (id,))
        self.dbConnection.commit()

    def Displayp(self):
        self.dbCursor.execute("SELECT * FROM patient_info")
        records = self.dbCursor.fetchall()
        return records


class Values:
    def Validate(self, id, fname, lname, speciality, phone, email):
        if not (id.isdigit() and (len(id) == 3)):
            return "id"
        elif not (fname.isalpha()):
            return "fName"
        elif not (lname.isalpha()):
            return "lName"
        elif not (speciality.isalpha()):
            return "speciality"
        elif not (phone.isdigit() and (len(phone) == 10)):
            return "phone"
        elif not (email.count("@") == 1 and email.count(".") > 0):
            return "email"
        else:
            return "SUCCESS"


class Valuesp:
    def Validatep(self, id, fName, lName, phone, email, history, doctor):
        if not (id.isdigit() and (len(id) == 3)):
            return "id"
        elif not (fName.isalpha()):
            return "fName"
        elif not (lName.isalpha()):
            return "lName"
        elif not (phone.isdigit() and (len(phone) == 10)):
            return "phone"
        elif not (email.count("@") == 1 and email.count(".") > 0):
            return "email"
        elif not (history.isalpha()):
            return "history"
        elif not (doctor.isalpha()):
            return "doctor"
        else:
            return "SUCCESS"


class InsertWindowp:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.wm_title("Insert data")

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.history = tkinter.StringVar()
        self.doctor = tkinter.StringVar()

        self.genderList = ["Male", "Female", "Transgender", "Other"]
        self.dateList = list(range(1, 32))
        self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"]
        self.yearList = list(range(1900, 2020))
        self.bloodGroupList = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

        # Labels
        tkinter.Label(self.window, text="Patient ID", width=25).grid(pady=5, column=1, row=1)
        tkinter.Label(self.window, text="First Name", width=25).grid(pady=5, column=1, row=2)
        tkinter.Label(self.window, text="Last Name", width=25).grid(pady=5, column=1, row=3)
        tkinter.Label(self.window, text="D.O.B", width=25).grid(pady=5, column=1, row=4)
        tkinter.Label(self.window, text="M.O.B", width=25).grid(pady=5, column=1, row=5)
        tkinter.Label(self.window, text="Y.O.B", width=25).grid(pady=5, column=1, row=6)
        tkinter.Label(self.window, text="Gender", width=25).grid(pady=5, column=1, row=7)
        tkinter.Label(self.window, text="Home Address", width=25).grid(pady=5, column=1, row=8)
        tkinter.Label(self.window, text="Phone Number", width=25).grid(pady=5, column=1, row=9)
        tkinter.Label(self.window, text="Email ID", width=25).grid(pady=5, column=1, row=10)
        tkinter.Label(self.window, text="Blood Group", width=25).grid(pady=5, column=1, row=11)
        tkinter.Label(self.window, text="Patient History", width=25).grid(pady=5, column=1, row=12)
        tkinter.Label(self.window, text="Doctor", width=25).grid(pady=5, column=1, row=13)

        # Fields
        # Entry widgets
        self.idEntry = tkinter.Entry(self.window, width=25, textvariable=self.id)
        self.fNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.fName)
        self.lNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lName)
        self.addressEntry = tkinter.Entry(self.window, width=25, textvariable=self.address)
        self.phoneEntry = tkinter.Entry(self.window, width=25, textvariable=self.phone)
        self.emailEntry = tkinter.Entry(self.window, width=25, textvariable=self.email)
        self.historyEntry = tkinter.Entry(self.window, width=25, textvariable=self.history)
        self.doctorEntry = tkinter.Entry(self.window, width=25, textvariable=self.doctor)

        self.idEntry.grid(pady=5, column=3, row=1)
        self.fNameEntry.grid(pady=5, column=3, row=2)
        self.lNameEntry.grid(pady=5, column=3, row=3)
        self.addressEntry.grid(pady=5, column=3, row=8)
        self.phoneEntry.grid(pady=5, column=3, row=9)
        self.emailEntry.grid(pady=5, column=3, row=10)
        self.historyEntry.grid(pady=5, column=3, row=12)
        self.doctorEntry.grid(pady=5, column=3, row=13)

        # Combobox widgets
        self.dobBox = tkinter.ttk.Combobox(self.window, values=self.dateList, width=20)
        self.mobBox = tkinter.ttk.Combobox(self.window, values=self.monthList, width=20)
        self.yobBox = tkinter.ttk.Combobox(self.window, values=self.yearList, width=20)
        self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderList, width=20)
        self.bloodGroupBox = tkinter.ttk.Combobox(self.window, values=self.bloodGroupList, width=20)

        self.dobBox.grid(pady=5, column=3, row=4)
        self.mobBox.grid(pady=5, column=3, row=5)
        self.yobBox.grid(pady=5, column=3, row=6)
        self.genderBox.grid(pady=5, column=3, row=7)
        self.bloodGroupBox.grid(pady=5, column=3, row=11)

        # Button widgets
        tkinter.Button(self.window, width=20, text="Insert", command=self.Insert).grid(pady=15, padx=5, column=1,
                                                                                       row=14)
        tkinter.Button(self.window, width=20, text="Reset", command=self.Reset).grid(pady=15, padx=5, column=2, row=14)
        tkinter.Button(self.window, width=20, text="Close", command=self.window.destroy).grid(pady=15, padx=5, column=3,
                                                                                              row=14)

        self.window.mainloop()

    def Insert(self):
        self.values = Valuesp()
        self.database = Database()
        self.test = self.values.Validatep(self.idEntry.get(), self.fNameEntry.get(), self.lNameEntry.get(),
                                          self.phoneEntry.get(), self.emailEntry.get(), self.historyEntry.get(),
                                          self.doctorEntry.get())
        if (self.test == "SUCCESS"):
            self.database.Insertp(self.idEntry.get(), self.fNameEntry.get(), self.lNameEntry.get(), self.dobBox.get(),
                                  self.mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(),
                                  self.phoneEntry.get(), self.emailEntry.get(), self.bloodGroupBox.get(),
                                  self.historyEntry.get(), self.doctorEntry.get())
            tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
        else:
            self.valueErrorMessage = "Invalid input in field " + self.test
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)

    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.fNameEntry.delete(0, tkinter.END)
        self.lNameEntry.delete(0, tkinter.END)
        self.dobBox.set("")
        self.mobBox.set("")
        self.yobBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.phoneEntry.delete(0, tkinter.END)
        self.emailEntry.delete(0, tkinter.END)
        self.bloodGroupBox.set("")
        self.historyEntry.delete(0, tkinter.END)
        self.doctorEntry.delete(0, tkinter.END)


class InsertWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.wm_title("Registration Section")

        self.id = tkinter.StringVar()
        self.fname = tkinter.StringVar()
        self.lname = tkinter.StringVar()
        self.gender = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.speciality = tkinter.StringVar()
        self.email = tkinter.StringVar()

        self.genderList = ["Male", "Female", "Transgender", "Other"]

        # Labels
        tkinter.Label(self.window, text="id (3 digit)", width=25).grid(pady=5, column=2, row=1)
        tkinter.Label(self.window, text="First Name", width=25).grid(pady=5, column=2, row=2)
        tkinter.Label(self.window, text="Last Name", width=25).grid(pady=5, column=2, row=3)
        tkinter.Label(self.window, text="Gender", width=25).grid(pady=5, column=2, row=4)
        tkinter.Label(self.window, text="Speciality", width=25).grid(pady=5, column=2, row=5)
        tkinter.Label(self.window, text="Phone", width=25).grid(pady=5, column=2, row=6)
        tkinter.Label(self.window, text="email", width=25).grid(pady=5, column=2, row=7)

        self.idEntry = tkinter.Entry(self.window, width=25, textvariable=self.id)
        self.fnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.fname)
        self.lnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lname)
        self.genderEntry = tkinter.Entry(self.window, width=25, textvariable=self.gender)
        self.specialityEntry = tkinter.Entry(self.window, width=25, textvariable=self.speciality)
        self.phoneEntry = tkinter.Entry(self.window, width=25, textvariable=self.phone)
        self.emailEntry = tkinter.Entry(self.window, width=25, textvariable=self.email)

        self.idEntry.grid(pady=5, column=4, row=1)
        self.fnameEntry.grid(pady=5, column=4, row=2)
        self.lnameEntry.grid(pady=5, column=4, row=3)
        self.specialityEntry.grid(pady=5, column=4, row=5)
        self.phoneEntry.grid(pady=5, column=4, row=6)
        self.emailEntry.grid(pady=5, column=4, row=7)

        self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderList, width=20)

        self.genderBox.grid(pady=5, column=4, row=4)

        tkinter.Button(self.window, width=20, text="Insert", command=self.Insert).grid(pady=15, padx=5, column=1,
                                                                                       row=14)
        tkinter.Button(self.window, width=20, text="Reset", command=self.Reset).grid(pady=15, padx=5, column=3, row=14)
        tkinter.Button(self.window, width=20, text="Close", command=self.window.destroy).grid(pady=15, padx=5, column=5,
                                                                                              row=14)

        self.window.mainloop()

    def Insert(self):
        self.values = Values()
        self.database = Database()
        self.test = self.values.Validate(self.idEntry.get(), self.fnameEntry.get(), self.lnameEntry.get(),
                                         self.specialityEntry.get(), self.phoneEntry.get(), self.emailEntry.get())
        if (self.test == "SUCCESS"):
            self.database.Insertd(self.idEntry.get(), self.fnameEntry.get(), self.lnameEntry.get(),
                                  self.genderBox.get(), self.specialityEntry.get(), self.phoneEntry.get(),
                                  self.emailEntry.get())
            tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
        else:
            self.valueErrorMessage = "Invalid input in field " + self.test
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)

    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.fnameEntry.delete(0, tkinter.END)
        self.lnameEntry.delete(0, tkinter.END)
        self.genderBox.set("")
        self.specialityEntry.delete(0, tkinter.END)
        self.phoneEntry.delete(0, tkinter.END)
        self.emailEntry.delete(0, tkinter.END)


class UpdateWindow:
    def __init__(self, id):
        self.window = tkinter.Tk()
        self.window.wm_title("Update data")


        self.id = id

        self.fname = tkinter.StringVar()
        self.lname = tkinter.StringVar()
        self.speciality = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.email = tkinter.StringVar()

        self.genderList = ["Male", "Female", "Transgender"]


        tkinter.Label(self.window, text="Doctor ID", width=25).grid(pady=5, column=1, row=1)
        tkinter.Label(self.window, text=id, width=25).grid(pady=5, column=3, row=1)
        tkinter.Label(self.window, text="First Name", width=25).grid(pady=5, column=1, row=2)
        tkinter.Label(self.window, text="Last Name", width=25).grid(pady=5, column=1, row=3)
        tkinter.Label(self.window, text="Gender", width=25).grid(pady=5, column=1, row=4)
        tkinter.Label(self.window, text="Speciality", width=25).grid(pady=5, column=1, row=5)
        tkinter.Label(self.window, text="Phone Number", width=25).grid(pady=5, column=1, row=6)
        tkinter.Label(self.window, text="Email ID", width=25).grid(pady=5, column=1, row=7)



        self.fnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.fname)
        self.lnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lname)
        self.specialityEntry = tkinter.Entry(self.window, width=25, textvariable=self.speciality)
        self.phoneEntry = tkinter.Entry(self.window, width=25, textvariable=self.phone)
        self.emailEntry = tkinter.Entry(self.window, width=25, textvariable=self.email)

        self.fnameEntry.grid(pady=5, column=3, row=2)
        self.lnameEntry.grid(pady=5, column=3, row=3)
        self.specialityEntry.grid(pady=5, column=3, row=5)
        self.phoneEntry.grid(pady=5, column=3, row=6)
        self.emailEntry.grid(pady=5, column=3, row=7)



        self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderList, width=20)

        self.genderBox.grid(pady=5, column=3, row=4)

        # Button widgets
        tkinter.Button(self.window, width=20, text="Update", command=self.Update).grid(pady=15, padx=5, column=1,
                                                                                       row=14)
        tkinter.Button(self.window, width=20, text="Reset", command=self.Reset).grid(pady=15, padx=5, column=2, row=14)
        tkinter.Button(self.window, width=20, text="Close", command=self.window.destroy).grid(pady=15, padx=5, column=3,
                                                                                              row=14)

        self.window.mainloop()

    def Update(self):
        self.database = Database()
        self.database.Updated(self.id, self.fnameEntry.get(), self.lnameEntry.get(), self.genderBox.get(),
                              self.specialityEntry.get(), self.phoneEntry.get(),
                              self.emailEntry.get())
        tkinter.messagebox.showinfo("Updated data", "Successfully updated the above data in the database")

    def Reset(self):
        self.fnameEntry.delete(0, tkinter.END)
        self.lnameEntry.delete(0, tkinter.END)
        self.genderBox.set("")
        self.specialityEntry.delete(0, tkinter.END)
        self.phoneEntry.delete(0, tkinter.END)
        self.emailEntry.delete(0, tkinter.END)


class UpdateWindowp:
    def __init__(self, id):
        self.window = tkinter.Tk()
        self.window.wm_title("Update data")

        # Initializing all the variables
        self.id = id

        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.history = tkinter.StringVar()
        self.doctor = tkinter.StringVar()

        self.genderList = ["Male", "Female", "Transgender", "Other"]
        self.dateList = list(range(1, 32))
        self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"]
        self.yearList = list(range(1900, 2020))
        self.bloodGroupList = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

        # Labels
        tkinter.Label(self.window, text="Patient ID", width=25).grid(pady=5, column=1, row=1)
        tkinter.Label(self.window, text=id, width=25).grid(pady=5, column=3, row=1)
        tkinter.Label(self.window, text="First Name", width=25).grid(pady=5, column=1, row=2)
        tkinter.Label(self.window, text="Last Name", width=25).grid(pady=5, column=1, row=3)
        tkinter.Label(self.window, text="D.O.B", width=25).grid(pady=5, column=1, row=4)
        tkinter.Label(self.window, text="M.O.B", width=25).grid(pady=5, column=1, row=5)
        tkinter.Label(self.window, text="Y.O.B", width=25).grid(pady=5, column=1, row=6)
        tkinter.Label(self.window, text="Gender", width=25).grid(pady=5, column=1, row=7)
        tkinter.Label(self.window, text="Home Address", width=25).grid(pady=5, column=1, row=8)
        tkinter.Label(self.window, text="Phone Number", width=25).grid(pady=5, column=1, row=9)
        tkinter.Label(self.window, text="Email ID", width=25).grid(pady=5, column=1, row=10)
        tkinter.Label(self.window, text="Blood Group", width=25).grid(pady=5, column=1, row=11)
        tkinter.Label(self.window, text="Patient History", width=25).grid(pady=5, column=1, row=12)
        tkinter.Label(self.window, text="Doctor", width=25).grid(pady=5, column=1, row=13)

        # Set previous values
        self.database = Database()
        self.searchResults = self.database.Searchp(id)

        tkinter.Label(self.window, text=self.searchResults[0][1], width=25).grid(pady=5, column=2, row=2)
        tkinter.Label(self.window, text=self.searchResults[0][2], width=25).grid(pady=5, column=2, row=3)
        tkinter.Label(self.window, text=self.searchResults[0][3], width=25).grid(pady=5, column=2, row=4)
        tkinter.Label(self.window, text=self.searchResults[0][4], width=25).grid(pady=5, column=2, row=5)
        tkinter.Label(self.window, text=self.searchResults[0][5], width=25).grid(pady=5, column=2, row=6)
        tkinter.Label(self.window, text=self.searchResults[0][6], width=25).grid(pady=5, column=2, row=7)
        tkinter.Label(self.window, text=self.searchResults[0][7], width=25).grid(pady=5, column=2, row=8)
        tkinter.Label(self.window, text=self.searchResults[0][8], width=25).grid(pady=5, column=2, row=9)
        tkinter.Label(self.window, text=self.searchResults[0][9], width=25).grid(pady=5, column=2, row=10)
        tkinter.Label(self.window, text=self.searchResults[0][10], width=25).grid(pady=5, column=2, row=11)
        tkinter.Label(self.window, text=self.searchResults[0][11], width=25).grid(pady=5, column=2, row=12)
        tkinter.Label(self.window, text=self.searchResults[0][12], width=25).grid(pady=5, column=2, row=13)

        # Fields
        # Entry widgets
        self.fNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.fName)
        self.lNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lName)
        self.addressEntry = tkinter.Entry(self.window, width=25, textvariable=self.address)
        self.phoneEntry = tkinter.Entry(self.window, width=25, textvariable=self.phone)
        self.emailEntry = tkinter.Entry(self.window, width=25, textvariable=self.email)
        self.historyEntry = tkinter.Entry(self.window, width=25, textvariable=self.history)
        self.doctorEntry = tkinter.Entry(self.window, width=25, textvariable=self.doctor)

        self.fNameEntry.grid(pady=5, column=3, row=2)
        self.lNameEntry.grid(pady=5, column=3, row=3)
        self.addressEntry.grid(pady=5, column=3, row=8)
        self.phoneEntry.grid(pady=5, column=3, row=9)
        self.emailEntry.grid(pady=5, column=3, row=10)
        self.historyEntry.grid(pady=5, column=3, row=12)
        self.doctorEntry.grid(pady=5, column=3, row=13)

        # Combobox widgets
        self.dobBox = tkinter.ttk.Combobox(self.window, values=self.dateList, width=20)
        self.mobBox = tkinter.ttk.Combobox(self.window, values=self.monthList, width=20)
        self.yobBox = tkinter.ttk.Combobox(self.window, values=self.yearList, width=20)
        self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderList, width=20)
        self.bloodGroupBox = tkinter.ttk.Combobox(self.window, values=self.bloodGroupList, width=20)

        self.dobBox.grid(pady=5, column=3, row=4)
        self.mobBox.grid(pady=5, column=3, row=5)
        self.yobBox.grid(pady=5, column=3, row=6)
        self.genderBox.grid(pady=5, column=3, row=7)
        self.bloodGroupBox.grid(pady=5, column=3, row=11)

        # Button widgets
        tkinter.Button(self.window, width=20, text="Update", command=self.Update).grid(pady=15, padx=5, column=1,
                                                                                       row=14)
        tkinter.Button(self.window, width=20, text="Reset", command=self.Reset).grid(pady=15, padx=5, column=2, row=14)
        tkinter.Button(self.window, width=20, text="Close", command=self.window.destroy).grid(pady=15, padx=5, column=3,
                                                                                              row=14)

        self.window.mainloop()

    def Update(self):
        self.database = Database()
        self.database.Updatep(self.fNameEntry.get(), self.lNameEntry.get(), self.dobBox.get(), self.mobBox.get(),
                             self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(), self.phoneEntry.get(),
                             self.emailEntry.get(), self.bloodGroupBox.get(), self.historyEntry.get(),
                             self.doctorEntry.get(), self.id)
        tkinter.messagebox.showinfo("Updated data", "Successfully updated the above data in the database")

    def Reset(self):
        self.fNameEntry.delete(0, tkinter.END)
        self.lNameEntry.delete(0, tkinter.END)
        self.dobBox.set("")
        self.mobBox.set("")
        self.yobBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.phoneEntry.delete(0, tkinter.END)
        self.emailEntry.delete(0, tkinter.END)
        self.bloodGroupBox.set("")
        self.historyEntry.delete(0, tkinter.END)
        self.doctorEntry.delete(0, tkinter.END)


class SearchDeleteWindow:
    def __init__(self, task):
        window = tkinter.Tk()
        window.wm_title(task + " data")

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.heading = "Please enter Patient ID to " + task

        # Labels
        tkinter.Label(window, text=self.heading, width=50).grid(pady=20, row=1)
        tkinter.Label(window, text="Patient ID", width=10).grid(pady=5, row=2)

        # Entry widgets
        self.idEntry = tkinter.Entry(window, width=5, textvariable=self.id)

        self.idEntry.grid(pady=5, row=3)

        # Button widgets
        if (task == "Search"):
            tkinter.Button(window, width=20, text=task, command=self.Search).grid(pady=15, padx=5, column=1, row=14)
        elif (task == "Delete"):
            tkinter.Button(window, width=20, text=task, command=self.Delete).grid(pady=15, padx=5, column=1, row=14)

    def Search(self):
        self.database = Database()
        self.data = self.database.Searchp(self.idEntry.get())
        self.databaseView = DatabaseView(self.data)

    def Delete(self):
        self.database = Database()
        self.database.Deletep(self.idEntry.get())


class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.wm_title("Database View")

        # Label widgets
        tkinter. \
            Label(self.databaseViewWindow, text="Database View Window", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ("id", "fname", "lname", "gender", "speciality", "phone", "email")

        # Treeview column headings
        self.databaseView.heading("id", text="ID")
        self.databaseView.heading("fname", text="First Name")
        self.databaseView.heading("lname", text="Last Name")
        self.databaseView.heading("gender", text="Gender")
        self.databaseView.heading("speciality", text="Speciality")
        self.databaseView.heading("phone", text="Phone Number")
        self.databaseView.heading("email", text="Email ID")

        # Treeview columns
        self.databaseView.column("id", width=40)
        self.databaseView.column("fname", width=100)
        self.databaseView.column("lname", width=100)
        self.databaseView.column("gender", width=60)
        self.databaseView.column("speciality", width=200)
        self.databaseView.column("phone", width=100)
        self.databaseView.column("email", width=200)

        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()


class DatabaseViewp:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.wm_title("Database View")

        # Label widgets
        tkinter.Label(self.databaseViewWindow, text="Database View Window", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = (
        "id", "fName", "lName", "dob", "mob", "yob", "gender", "address", "phone", "email", "bloodGroup", "history",
        "doctor")

        # Treeview column headings
        self.databaseView.heading("id", text="ID")
        self.databaseView.heading("fName", text="First Name")
        self.databaseView.heading("lName", text="Last Name")
        self.databaseView.heading("dob", text="D.O.B")
        self.databaseView.heading("mob", text="M.O.B")
        self.databaseView.heading("yob", text="Y.O.B")
        self.databaseView.heading("gender", text="Gender")
        self.databaseView.heading("address", text="Home Address")
        self.databaseView.heading("phone", text="Phone Number")
        self.databaseView.heading("email", text="Email ID")
        self.databaseView.heading("bloodGroup", text="Blood Group")
        self.databaseView.heading("history", text="History")
        self.databaseView.heading("doctor", text="Doctor")

        # Treeview columns
        self.databaseView.column("id", width=40)
        self.databaseView.column("fName", width=100)
        self.databaseView.column("lName", width=100)
        self.databaseView.column("dob", width=60)
        self.databaseView.column("mob", width=60)
        self.databaseView.column("yob", width=60)
        self.databaseView.column("gender", width=60)
        self.databaseView.column("address", width=200)
        self.databaseView.column("phone", width=100)
        self.databaseView.column("email", width=200)
        self.databaseView.column("bloodGroup", width=100)
        self.databaseView.column("history", width=100)
        self.databaseView.column("doctor", width=100)

        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()


class DeleteWindow:
    def __init__(self):
        window = tkinter.Tk()
        window.wm_title(" data")

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.fname = tkinter.StringVar()
        self.lname = tkinter.StringVar()



        tkinter.Label(window, text="Patient ID", width=50).grid(pady=20, row=1)

        # Entry widgets
        self.idEntry = tkinter.Entry(window, width=5, textvariable=self.id)

        self.idEntry.grid(ipady=6, row=2)

        # Button widgets

        tkinter.Button(window, width=20, text="DELETE", command=self.Delete).grid(pady=10,row=3)
        self.DeleteWindow.destroy()
    def Delete(self):
        self.database = Database()
        self.database.Deleted(self.idEntry.get())


class HomePage:
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.geometry("1000x1000")
        self.homePageWindow.wm_title("Hospital Management System")

        label1 = tkinter.Label(self.homePageWindow, height=3,
                               text="Welcome to Snjeevani HealthCare\nHow can I help you?", relief="solid", fg="white",
                               bg="blue", font=("arial", 14, "bold"))
        label1.pack(fill="x", padx="2")
        label2 = tkinter.Label(self.homePageWindow, height=2, text="Doctor's Section", fg="blue",
                               font=("arial", 14, "bold"))
        label2.place(x=450, y=120)
        button1 = tkinter.Button(self.homePageWindow, height=1, width=20, fg="white", bg="blue", text="REGISTRATION",relief="solid",
                                 command=self.Insertd)
        button1.place(x=350, y=180)
        button2 = tkinter.Button(self.homePageWindow, height=1, width=20, fg="white", bg="blue", text="UPDATE",relief="solid",
                                 command=self.Updated)
        button2.place(x=550, y=180)
        button3 = tkinter.Button(self.homePageWindow, height=1, width=20, fg="white", bg="blue", text="DELETE",relief="solid",
                                 command=self.Deleted)
        button3.place(x=350, y=220)
        button4 = tkinter.Button(self.homePageWindow, height=1, width=20, fg="white", bg="blue", text="DISPLAY LIST",relief="solid",
                                 command=self.Displayd)
        button4.place(x=550, y=220)

        label3 = tkinter.Label(self.homePageWindow, height=2, text="Patient's Section", fg="blue",
                               font=("arial", 14, "bold"))
        label3.place(x=450, y=350)
        button5 = tkinter.Button(self.homePageWindow, height=1, width=20, fg="white", bg="blue", text="APPOINTMENTS",relief="solid",
                                 command=self.Insertp)
        button5.place(x=350, y=420)
        button6 = tkinter.Button(self.homePageWindow, height=1, width=20, fg="white", bg="blue", text="UPDATE",relief="solid",command=self.Updatep)
        button6.place(x=550, y=420)
        button7 = tkinter.Button(self.homePageWindow, height=1, width=20, fg="white", bg="blue", text="DELETE",relief="solid",command=self.Deletep)
        button7.place(x=350, y=460)
        button8 = tkinter.Button(self.homePageWindow, height=1, width=20, fg="white", bg="blue", text="SEARCH",relief="solid",command=self.Searchp)
        button8.place(x=550, y=460)
        button9 = tkinter.Button(self.homePageWindow, height=1, width=20, fg="white", bg="blue", text="DISPLAY LIST",relief="solid",
                                 command=self.Displayp)
        button9.place(x=450, y=500)

        button10 = tkinter.Button(self.homePageWindow, height=2, width=22, fg="white", bg="blue", text="ABOUT US",relief="solid",
                                  command=self.About)
        button10.place(x=450, y=610)
        button11 = tkinter.Button(self.homePageWindow, height=2, width=22, fg="white", bg="blue", text="EXIT",relief="solid",
                                  command=self.homePageWindow.destroy)
        button11.place(x=450, y=660)
        self.homePageWindow.mainloop()

    def Insertd(self):
        self.insertWindow = InsertWindow()

    def Updated(self):
        self.updateIDWindow = tkinter.Tk()
        self.updateIDWindow.wm_title("Update data")

        # Initializing all the variables
        self.id = tkinter.StringVar()

        # Label
        tkinter.Label(self.updateIDWindow, text="Enter ID ", width=50).grid(pady=20, row=1)

        # Entry widgets
        self.idEntry = tkinter.Entry(self.updateIDWindow, width=5, textvariable=self.id)

        self.idEntry.grid(ipady=6, row=2)

        # Button widgets
        tkinter.Button(self.updateIDWindow, width=20, text="Update", command=self.updateID).grid(pady=10, row=3)

        self.updateIDWindow.mainloop()

    # def Search(self):
    #   self.searchWindow = SearchDeleteWindow("Search")

    def updateID(self):
        self.updateWindow = UpdateWindow(self.idEntry.get())
        self.updateIDWindow.destroy()

    def Deleted(self):
        self.deleteWindow = DeleteWindow()



    def Displayd(self):
        self.database = Database()
        self.data = self.database.Displayd()
        self.displayWindow = DatabaseView(self.data)

    def Insertp(self):
        self.insertWindow = InsertWindowp()

    def Displayp(self):
        self.database = Database()
        self.data = self.database.Displayp()
        self.displayWindow = DatabaseViewp(self.data)

    def Updatep(self):
        self.updateIDpWindow = tkinter.Tk()
        self.updateIDpWindow.wm_title("Update data")

        # Initializing all the variables
        self.id = tkinter.StringVar()

        # Label
        tkinter.Label(self.updateIDpWindow, text="Enter the ID to update", width=50).grid(pady=20, row=1)

        # Entry widgets
        self.idEntry = tkinter.Entry(self.updateIDpWindow, width=5, textvariable=self.id)

        self.idEntry.grid(pady=10, row=2)

        # Button widgets
        tkinter.Button(self.updateIDpWindow, width=20, text="Update", command=self.updateIDp).grid(pady=10, row=3)

        self.updateIDpWindow.mainloop()

    def Searchp(self):
       self.searchWindow = SearchDeleteWindow("Search")


    def updateIDp(self):
        self.updateWindow = UpdateWindowp(self.idEntry.get())
        self.updateIDWindow.destroy()

    def Deletep(self):
        self.deleteWindow = SearchDeleteWindow("Delete")
        self.deleteWindow.destroy()

    def About(self):
        self.aboutWindow = tkinter.Tk()
        self.aboutWindow.geometry("1200x1000")
        self.aboutWindow.wm_title("Hospital Management System")

        label2 = tkinter.Label(self.aboutWindow, height=1,
                               text="Sanjeevani Healthcare was established on 1990.At present we have 20 doctors and 30 other medical staffs.",
                               fg="blue",
                               font=("arial", 14, "bold"))
        label2.place(x=20, y=60)

        label3 = tkinter.Label(self.aboutWindow, height=1, text="We assure you to provide the best medical facility.",
                               fg="blue",
                               font=("arial", 14, "bold"))
        label3.place(x=20, y=90)

        label4 = tkinter.Label(self.aboutWindow, height=1, text="Contact No: 9807698756, 8789876756",
                               fg="blue",
                               font=("arial", 14, "bold"))
        label4.place(x=20, y=120)

        label5 = tkinter.Label(self.aboutWindow, height=1, text="Email us at: sanjeevaniMedicare12@gmail.com",
                               fg="blue",
                               font=("arial", 14, "bold"))
        label5.place(x=20, y=150)

        label6 = tkinter.Label(self.aboutWindow, height=1, text="link: www.sanjeevaniHealthcare.com",
                               fg="blue",
                               font=("arial", 14, "bold"))
        label6.place(x=20, y=180)


homePage = HomePage()
