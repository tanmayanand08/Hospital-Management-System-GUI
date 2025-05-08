from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # Variables
        self.NameOfTablets = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.NumberOfTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.NhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        # Title
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                         fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Dataframe
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                   font=("times new roman", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # Buttons frame
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # Details frame
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # DataframeLeft
        lblNameTablet = Label(DataframeLeft, text="Name Of Tablet", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0, sticky=W)

        comNameTablet = ttk.Combobox(DataframeLeft, textvariable=self.NameOfTablets, state="readonly",
                                     font=("arial", 12, "bold"), width=33)
        comNameTablet["values"] = ("Tetanus", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)

        lblRef = Label(DataframeLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2, pady=6)
        lblRef.grid(row=1, column=0, sticky=W)
        txtRef = Entry(DataframeLeft, textvariable=self.Ref, font=("arial", 13, "bold"), width=35)
        txtRef.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=6)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, textvariable=self.Dose, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataframeLeft, font=("arial", 12, "bold"), text="No Of Tablets:", padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataframeLeft, textvariable=self.NumberOfTablets, font=("arial", 13, "bold"), width=35)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, textvariable=self.Lot, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4, column=1)

        lblIssueDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataframeLeft, textvariable=self.IssueDate, font=("arial", 13, "bold"), width=35)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, textvariable=self.ExpDate, font=("arial", 13, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, textvariable=self.DailyDose, font=("arial", 13, "bold"), width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, textvariable=self.SideEffect, font=("arial", 13, "bold"), width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherInfo = Label(DataframeLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2, pady=6)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(DataframeLeft, textvariable=self.FurtherInformation, font=("arial", 13, "bold"), width=35)
        txtFurtherInfo.grid(row=0, column=3)

        lblStorage = Label(DataframeLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=1, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, textvariable=self.StorageAdvice, font=("arial", 13, "bold"), width=35)
        txtStorage.grid(row=1, column=3)

        lblMedicine = Label(DataframeLeft, font=("arial", 12, "bold"), text="Medication:", padx=2, pady=6)
        lblMedicine.grid(row=2, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, textvariable=self.HowToUseMedication, font=("arial", 13, "bold"), width=35)
        txtMedicine.grid(row=2, column=3)

        lblPatientId = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Id:", padx=2, pady=6)
        lblPatientId.grid(row=3, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, textvariable=self.PatientId, font=("arial", 13, "bold"), width=35)
        txtPatientId.grid(row=3, column=3)

        lblNhsNumber = Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblNhsNumber.grid(row=4, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, textvariable=self.NhsNumber, font=("arial", 13, "bold"), width=35)
        txtNhsNumber.grid(row=4, column=3)

        lblPatientName = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientName.grid(row=5, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, textvariable=self.PatientName, font=("arial", 13, "bold"), width=35)
        txtPatientName.grid(row=5, column=3)

        lblDateOfBirth = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date Of Birth:", padx=2, pady=6)
        lblDateOfBirth.grid(row=6, column=2, sticky=W)
        txtDateOfBirth = Entry(DataframeLeft, textvariable=self.DateOfBirth, font=("arial", 13, "bold"), width=35)
        txtDateOfBirth.grid(row=6, column=3)

        lblPatientAddress = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=7, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, textvariable=self.PatientAddress, font=("arial", 13, "bold"), width=35)
        txtPatientAddress.grid(row=7, column=3)

        # DataframeRight
        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # Buttons
        btnPrescription = Button(Buttonframe, command=self.iPrescription, text="Prescription", bg="green", fg="white",
                                 font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, command=self.iPrescriptionData, text="Prescription Data", bg="green",
                                     fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, command=self.update_data, text="Update", bg="green", fg="white",
                           font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, command=self.idelete, text="Delete", bg="green", fg="white",
                           font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, command=self.clear, text="Clear", bg="green", fg="white",
                          font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, command=self.iExit, text="Exit", bg="green", fg="white",
                         font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # Table and Scrollbars
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, columns=(
            "NameOfTablets", "Ref", "Dose", "NoOfTablets", "Lot", "IssueDate", "ExpDate", "DailyDose", "Storage",
            "NhsNumber", "PatientName", "Dob", "Address", "SideEffect", "FurtherInformation", "Medication", "PatientId"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("NameOfTablets", text="Name Of Tablet")
        self.hospital_table.heading("Ref", text="Reference No.")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("NoOfTablets", text="No Of Tablets")
        self.hospital_table.heading("Lot", text="Lot")
        self.hospital_table.heading("IssueDate", text="Issue Date")
        self.hospital_table.heading("ExpDate", text="Exp Date")
        self.hospital_table.heading("DailyDose", text="Daily Dose")
        self.hospital_table.heading("Storage", text="Storage")
        self.hospital_table.heading("NhsNumber", text="NHS Number")
        self.hospital_table.heading("PatientName", text="Patient Name")
        self.hospital_table.heading("Dob", text="DOB")
        self.hospital_table.heading("Address", text="Address")
        self.hospital_table.heading("SideEffect", text="Side Effect")
        self.hospital_table.heading("FurtherInformation", text="Further Information")
        self.hospital_table.heading("Medication", text="Medication")
        self.hospital_table.heading("PatientId", text="Patient Id")

        self.hospital_table["show"] = "headings"
        for col in self.hospital_table["columns"]:
            self.hospital_table.column(col, width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # Functionality
    def iPrescriptionData(self):
        if self.NameOfTablets.get() == "" or self.Ref.get() == "":
            messagebox.showerror("Error", "Name of Tablets and Reference No are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="user@123", database="Mydata")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO hospital VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.NameOfTablets.get(),
                        self.Ref.get(),
                        self.Dose.get(),
                        self.NumberOfTablets.get(),
                        self.Lot.get(),
                        self.IssueDate.get(),
                        self.ExpDate.get(),
                        self.DailyDose.get(),
                        self.StorageAdvice.get(),
                        self.NhsNumber.get(),
                        self.PatientName.get(),
                        self.DateOfBirth.get(),
                        self.PatientAddress.get(),
                        self.SideEffect.get(),
                        self.FurtherInformation.get(),
                        self.HowToUseMedication.get(),
                        self.PatientId.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}")

    def update_data(self):
        if self.Ref.get() == "":
            messagebox.showerror("Error", "Reference No is required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="user@123", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    """UPDATE hospital SET NameOfTablets=%s, Dose=%s, No_Of_Tablets=%s, Lot=%s, Issue_Date=%s, 
                    Exp_Date=%s, Daily_Dose=%s, Storage=%s, NHSNumber=%s, Patient_Name=%s, DOB=%s, Address=%s, 
                    Side_Effect=%s, Further_Information=%s, Medication=%s, Patient_Id=%s WHERE Reference_No=%s""",
                    (
                        self.NameOfTablets.get(),
                        self.Dose.get(),
                        self.NumberOfTablets.get(),
                        self.Lot.get(),
                        self.IssueDate.get(),
                        self.ExpDate.get(),
                        self.DailyDose.get(),
                        self.StorageAdvice.get(),
                        self.NhsNumber.get(),
                        self.PatientName.get(),
                        self.DateOfBirth.get(),
                        self.PatientAddress.get(),
                        self.SideEffect.get(),
                        self.FurtherInformation.get(),
                        self.HowToUseMedication.get(),
                        self.PatientId.get(),
                        self.Ref.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been updated")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}")

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="user@123", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM hospital")
            rows = my_cursor.fetchall()
            if rows:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for row in rows:
                    self.hospital_table.insert("", END, values=row) 
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        if row:
            self.NameOfTablets.set(row[0])
            self.Ref.set(row[1])
            self.Dose.set(row[2])
            self.NumberOfTablets.set(row[3])
            self.Lot.set(row[4])
            self.IssueDate.set(row[5])
            self.ExpDate.set(row[6])
            self.DailyDose.set(row[7])
            self.StorageAdvice.set(row[8])
            self.NhsNumber.set(row[9])
            self.PatientName.set(row[10])
            self.DateOfBirth.set(row[11])
            self.PatientAddress.set(row[12])
            self.SideEffect.set(row[13])
            self.FurtherInformation.set(row[14])
            self.HowToUseMedication.set(row[15])
            self.PatientId.set(row[16])

    def iPrescription(self):
        self.txtPrescription.delete("1.0", END)
        self.txtPrescription.insert(END, f"Name Of Tablets:\t\t{self.NameOfTablets.get()}\n")
        self.txtPrescription.insert(END, f"Reference No:\t\t{self.Ref.get()}\n")
        self.txtPrescription.insert(END, f"Dose:\t\t{self.Dose.get()}\n")
        self.txtPrescription.insert(END, f"Number Of Tablets:\t\t{self.NumberOfTablets.get()}\n")
        self.txtPrescription.insert(END, f"Lot:\t\t{self.Lot.get()}\n")
        self.txtPrescription.insert(END, f"Issue Date:\t\t{self.IssueDate.get()}\n")
        self.txtPrescription.insert(END, f"Exp Date:\t\t{self.ExpDate.get()}\n")
        self.txtPrescription.insert(END, f"Daily Dose:\t\t{self.DailyDose.get()}\n")
        self.txtPrescription.insert(END, f"Side Effect:\t\t{self.SideEffect.get()}\n")
        self.txtPrescription.insert(END, f"Further Information:\t\t{self.FurtherInformation.get()}\n")
        self.txtPrescription.insert(END, f"Storage Advice:\t\t{self.StorageAdvice.get()}\n")
        self.txtPrescription.insert(END, f"Driving Using Machine:\t\t{self.DrivingUsingMachine.get()}\n")
        self.txtPrescription.insert(END, f"Medication:\t\t{self.HowToUseMedication.get()}\n")
        self.txtPrescription.insert(END, f"Patient Id:\t\t{self.PatientId.get()}\n")
        self.txtPrescription.insert(END, f"NHS Number:\t\t{self.NhsNumber.get()}\n")
        self.txtPrescription.insert(END, f"Patient Name:\t\t{self.PatientName.get()}\n")
        self.txtPrescription.insert(END, f"Date Of Birth:\t\t{self.DateOfBirth.get()}\n")
        self.txtPrescription.insert(END, f"Patient Address:\t\t{self.PatientAddress.get()}\n")

    def idelete(self):
        if self.Ref.get() == "":
            messagebox.showerror("Error", "Reference No is required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="user@123", database="mydata")
                my_cursor = conn.cursor()
                query = "DELETE FROM hospital WHERE Reference_No=%s"
                value = (self.Ref.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Patient record has been deleted")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}")

    def clear(self):
        self.NameOfTablets.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.NumberOfTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.NhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
        if iExit:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    ob = Hospital(root)
    root.mainloop()