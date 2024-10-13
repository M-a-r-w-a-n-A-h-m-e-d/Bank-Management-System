from tkinter import *
from tkinter import messagebox
from datetime import datetime


class User:
    def __init__(self, Id, customerId, name, age, gender, password, phoneNumber, address, salary, balance, opened,
                 account_type='Checking'):
        self.Id = Id
        self.customerId = customerId
        self.name = name
        self.age = age
        self.gender = gender
        self.password = password
        self.phoneNumber = phoneNumber
        self.address = address
        self.salary = salary
        self.balance = balance
        self.log = []
        self.account_type = account_type
        self.opened = opened
        self.LoanActive = False
        self.loan = 0
        self.loanMonths = 0


class Bank:
    def __init__(self, name, address, money):
        self.name = name
        self.address = address
        self.money = money
        self.Log = []
        self.Tellers = []
        self.Users = []


class Teller:
    def __init__(self, Id, TellerId, name, age, gender, password, phoneNumber, address, salary):
        self.Id = Id
        self.TellerId = TellerId
        self.name = name
        self.age = age
        self.gender = gender
        self.password = password
        self.phoneNumber = phoneNumber
        self.address = address
        self.salary = salary


class GUi(Bank):
    def __init__(self, main):
        self.main = main
        self.main.title('Bank Management System')
        self.main.geometry('500x500+600+200')
        self.main.resizable(False, False)
        self.main.configure(bg='gold')

    def welcomePage(self):
        self.frameWel = Frame(self.main, background="gold")
        self.frameWel.place(relx=0.5, rely=0.5, anchor='center')

        Label(self.frameWel, text='Welcome', font=26).grid(row=0, column=1)
        self.buttonSignUp = Button(
            self.frameWel, text='Sign Up', command=self.signUp, width=15)
        self.buttonSignUp.grid(row=1, column=1, pady=10)

        self.buttonLogIn = Button(
            self.frameWel, text='Log In', command=self.logIn, width=15)
        self.buttonLogIn.grid(row=2, column=1, pady=10)

    def signUp(self):
        def onSignUp():
            Id = self.entryUp1.get()
            name = self.entryUp2.get()
            password = self.entryUp3.get()
            age = self.entryUp4.get()
            gender = gender_var.get()
            phoneNumber = self.entryUp5.get()
            address = self.entryUp6.get()
            salary = self.entryUp7.get()
            account_type = account_type_var.get()

            if not Id or not name or not password or not age or not gender or not phoneNumber or not address or not salary:
                self.warningPage("Warning", "All fields are required.")
                return
            if not Id.isdigit() or not phoneNumber.isdigit() or not salary.isdigit():
                self.warningPage("Warning", "National IdShould Be A Number.")
                return
            if len(password) < 8:
                self.warningPage(
                    "Warning", "Password Should Be At Least 8 Characters.")
                return
            if len(name) < 3 or any(char.isdigit() for char in name):
                self.warningPage(
                    "Warning", "Name Should Be At Least 3 Characters.")
                return
            if len(address) < 3:
                self.warningPage(
                    "Warning", "Address Should Be At Least 3 Characters.")
                return
            if len(phoneNumber) != 11:
                self.warningPage(
                    "Warning", "Phone Number Should Be 11 Numbers")
                return
            calculate = self.calculate_age(age)
            if calculate == False:
                return

            for user in bank.Users:
                if user.customerId == Id:
                    self.warningPage("Warning", "Customer ID already exists.")
                    return

            bank.Users.append(User(Id=(len(bank.Users) + 1), name=name, password=password, customerId=Id,
                                   age=age, gender=gender, phoneNumber=phoneNumber, address=address,
                                   salary=float(salary), balance=0, opened=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                   account_type=account_type))

            self.entryUp1.delete(0, END)
            self.entryUp2.delete(0, END)
            self.entryUp3.delete(0, END)
            self.entryUp4.delete(0, END)
            self.entryUp5.delete(0, END)
            self.entryUp6.delete(0, END)
            self.entryUp7.delete(0, END)

            self.infoPage("SignIn", 'SignUp Completed Successfully')
            self.frameWel.destroy()
            self.frameUp.destroy()
            self.logIn()

        self.frameWel.destroy()
        self.frameUp = Frame(self.main, width=400, height=400)
        self.frameUp.place(relx=0.5, rely=0.5, anchor="center")

        Label(self.frameUp, text='Name :').grid(row=0, column=3)
        self.entryUp2 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp2.grid(row=0, column=4)

        Label(self.frameUp, text='National ID :').grid(row=1, column=3)
        self.entryUp1 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp1.grid(row=1, column=4)

        Label(self.frameUp, text='Password :').grid(row=2, column=3)
        self.entryUp3 = Entry(self.frameUp, insertwidth=4, width=16, show='*')
        self.entryUp3.grid(row=2, column=4)

        Label(self.frameUp, text='Age YYYY-MM-DD:').grid(row=3, column=3)
        self.entryUp4 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp4.grid(row=3, column=4)

        Label(self.frameUp, text='Phone Number :').grid(row=4, column=3)
        self.entryUp5 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp5.grid(row=4, column=4)

        Label(self.frameUp, text='Address :').grid(row=5, column=3)
        self.entryUp6 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp6.grid(row=5, column=4)

        Label(self.frameUp, text='Salary :').grid(row=6, column=3)
        self.entryUp7 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp7.grid(row=6, column=4)

        Label(self.frameUp, text='Gender :').grid(row=7, column=3)
        gender_var = StringVar(value='Male')
        Radiobutton(self.frameUp, text='Male', variable=gender_var,
                    value='Male').grid(row=7, column=4)
        Radiobutton(self.frameUp, text='Female', variable=gender_var,
                    value='Female').grid(row=7, column=5)

        Label(self.frameUp, text='Account Type:').grid(row=10, column=3)
        account_type_var = StringVar(value='Checking')
        Radiobutton(self.frameUp, text='Savings', variable=account_type_var,
                    value='Savings').grid(row=10, column=5)
        Radiobutton(self.frameUp, text='Checking', variable=account_type_var,
                    value='Checking').grid(row=10, column=4)

        def onPressed():
            self.frameWel.destroy()
            self.frameUp.destroy()
            self.logIn()

        Button(self.frameUp, text='Create Account',
               command=onSignUp).grid(row=11, column=4)

        Label(self.frameUp, text='Have An Account?').grid(row=12, column=3)
        Button(self.frameUp, text='Login', command=onPressed).grid(row=12, column=4)

    def logIn(self):
        self.currentUserId = 0
        self.currentTellerId = 0

        def onLogin():
            name = self.entryName.get()
            password = self.entryPass.get()

            if name == "Marwan Ahmed" and password == "1234":
                self.frameIn.destroy()
                self.adminMainPage()
                return

            for teller in bank.Tellers:
                if teller.name == name and teller.password == password:
                    self.infoPage(
                        'Login', 'Login As Teller Successfully Completed')
                    self.currentTellerId = teller.Id
                    self.frameIn.destroy()
                    self.tellerMainPage()
                    return

            for user in bank.Users:
                if user.name == name and user.password == password:
                    self.infoPage('Login', 'Login Successfully Completed')
                    self.currentUserId = user.Id
                    self.frameIn.destroy()
                    self.customerMainPage()
                    return
            self.errorPage('Error', 'Invalid Name or Password')

        self.frameWel.destroy()
        self.frameIn = Frame(self.main)
        self.frameIn.place(relx=0.5, rely=0.5, anchor='center')

        Label(self.frameIn, text='Name :').grid(row=0, column=0, sticky='nsew')
        self.entryName = Entry(self.frameIn, width=16)
        self.entryName.grid(row=0, column=1)

        Label(self.frameIn, text='Pass :').grid(row=1, column=0, sticky='nsew')
        self.entryPass = Entry(self.frameIn, width=16, show='*')
        self.entryPass.grid(row=1, column=1)

        buttonIn = Button(self.frameIn, text='Log In',
                          command=onLogin, background="green")
        buttonIn.grid(row=2, column=1)

        def onPressed():
            self.frameWel.destroy()
            self.frameIn.destroy()
            self.signUp()

        Label(self.frameIn, text='Create An Account :').grid(row=3, column=0)
        Button(self.frameIn, text='Sign Up', command=onPressed).grid(row=3, column=1)

    def customerMainPage(self):
        self.frameMain = Frame(self.main)
        self.frameMain.place(relx=0.5, rely=0.5, anchor="center")

        Button(self.frameMain, text='Deposit',
               command=self.depositPage, width=25).grid(row=1, column=1)
        Button(self.frameMain, text='Withdraw',
               command=self.withdrawPage, width=25).grid(row=2, column=1)
        Button(self.frameMain, text='View Log',
               command=self.viewLog, width=25).grid(row=3, column=1)
        Button(self.frameMain, text='Transfer Funds',
               command=self.transferFunds, width=25).grid(row=4, column=1)
        Button(self.frameMain, text='Change Password',
               command=self.changePassword, width=25).grid(row=5, column=1)
        Button(self.frameMain, text='Show All Your Information',
               command=self.showCurrentUserData, width=25).grid(row=6, column=1)
        Button(self.frameMain, text='Loan',
               command=self.requestLoan, width=25).grid(row=7, column=1)
        Button(self.frameMain, text='Log Out', bg="red",
               command=self.logout, width=25).grid(row=8, column=1)

    def tellerMainPage(self):
        self.frameMain = Frame(self.main)
        self.frameMain.place(relx=0.5, rely=0.5, anchor="center")

        Button(self.frameMain, text='View Log',
               command=self.viewLogTeller, width=25).grid(row=0, column=1)
        Button(self.frameMain, text='Deposit',
               command=self.depositPageTeller, width=25).grid(row=1, column=1)
        Button(self.frameMain, text='Withdraw',
               command=self.withdrawPageTeller, width=25).grid(row=2, column=1)
        Button(self.frameMain, text='Show Customer Information',
               command=self.showAllCustomers, width=25).grid(row=3, column=1)
        Button(self.frameMain, text='Edit Customer Information',
               command=self.editCustomerInfo, width=25).grid(row=4, column=1)
        Button(self.frameMain, text='Search For Customer',
               command=self.searchCustomer, width=25).grid(row=5, column=1)
        Button(self.frameMain, text='Close Account',
               command=self.closeAccount, width=25).grid(row=6, column=1)
        Button(self.frameMain, text='Log Out', bg="red",
               command=self.logout, width=25).grid(row=7, column=1)

    def adminMainPage(self):
        self.frameMain = Frame(self.main)
        self.frameMain.place(relx=0.5, rely=0.5, anchor="center")

        Button(self.frameMain, text='Bank Logs',
               command=self.viewBankLog, width=25).grid(row=0, column=1)

        Button(self.frameMain, text='Create Teller Account',
               command=self.signTellerUp, width=25).grid(row=1, column=1)

        Button(self.frameMain, text='Close Teller Account',
               command=self.closeTellerAccount, width=25).grid(row=2, column=1)

        Button(self.frameMain, text='View Bank Information',
               command=self.showBankInformation, width=25).grid(row=3, column=1)

        Button(self.frameMain, text='Show All Tellers',
               command=self.showAllTellers, width=25).grid(row=4, column=1)

        Button(self.frameMain, text='Search For Teller',
               command=self.searchTeller, width=25).grid(row=5, column=1)

        Button(self.frameMain, text='Log Out', bg="red",
               command=self.logout, width=25).grid(row=6, column=1)

    def showBankInformation(self):
        top = Toplevel(self.main)
        top.title("Bank Info")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))
        Label(top, text=f"Bank Name: {bank.name}").grid(row=0, column=1)
        Label(top, text=f"Bank Address: {bank.address}").grid(row=1, column=1)
        Label(top, text=f"Bank Money: {bank.money:.2f}").grid(row=2, column=1)
        Label(top, text=f"Bank Tellers: {len(bank.Tellers)}").grid(row=4, column=1)
        Label(top, text=f"Bank Users: {len(bank.Users)}").grid(row=3, column=1)

    def showCurrentUserData(self):
        Top = Toplevel(self.main)
        Top.title("Current User Data")
        Top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        frame = Frame(Top)
        frame.pack(padx=10, pady=10)

        for user in bank.Users:
            if user.Id == self.currentUserId:
                Label(frame, text="ID:").grid(row=0, column=0, sticky='w')
                Label(frame, text=user.Id).grid(row=0, column=1, sticky='w')

                Label(frame, text="Customer ID:").grid(row=1, column=0, sticky='w')
                Label(frame, text=user.customerId).grid(row=1, column=1, sticky='w')

                Label(frame, text="Name:").grid(row=2, column=0, sticky='w')
                Label(frame, text=user.name).grid(row=2, column=1, sticky='w')

                Label(frame, text="Age:").grid(row=3, column=0, sticky='w')
                Label(frame, text=user.age).grid(row=3, column=1, sticky='w')

                Label(frame, text="Gender:").grid(row=4, column=0, sticky='w')
                Label(frame, text=user.gender).grid(row=4, column=1, sticky='w')

                Label(frame, text="Phone:").grid(row=5, column=0, sticky='w')
                Label(frame, text=user.phoneNumber).grid(row=5, column=1, sticky='w')

                Label(frame, text="Address:").grid(row=6, column=0, sticky='w')
                Label(frame, text=user.address).grid(row=6, column=1, sticky='w')

                Label(frame, text="Salary:").grid(row=7, column=0, sticky='w')
                Label(frame, text=f"{user.salary:.2f}").grid(row=7, column=1, sticky='w')

                Label(frame, text="Balance:").grid(row=8, column=0, sticky='w')
                Label(frame, text=f"{user.balance:.2f}").grid(row=8, column=1, sticky='w')

                Label(frame, text="Account Type:").grid(row=9, column=0, sticky='w')
                Label(frame, text=user.account_type).grid(row=9, column=1, sticky='w')

                Label(frame, text="Opened:").grid(row=10, column=0, sticky='w')
                Label(frame, text=user.opened).grid(row=10, column=1, sticky='w')

    def signTellerUp(self):
        def onSignUp():
            Id = self.entryUp1.get()
            name = self.entryUp2.get()
            password = self.entryUp3.get()
            age = self.entryUp4.get()
            gender = gender_var.get()
            phoneNumber = self.entryUp5.get()
            address = self.entryUp6.get()
            salary = self.entryUp7.get()

            if not Id or not name or not password or not age or not gender or not phoneNumber or not address or not salary:
                self.errorPage("Error", "All fields are required.")
                return

            for teller in bank.Tellers:
                if teller.TellerId == Id:
                    self.errorPage("Error", "Teller ID already exists.")
                    return

            self.calculate_age(age)

            bank.Tellers.append(Teller(Id=(len(bank.Tellers) + 1), name=name, password=password, TellerId=Id,
                                       age=age, gender=gender, phoneNumber=phoneNumber, address=address,
                                       salary=float(salary)))

            self.entryUp1.delete(0, END)
            self.entryUp2.delete(0, END)
            self.entryUp3.delete(0, END)
            self.entryUp4.delete(0, END)
            self.entryUp5.delete(0, END)
            self.entryUp6.delete(0, END)
            self.entryUp7.delete(0, END)

            self.infoPage("SignUp", 'SignUp Completed Successfully')
            self.frameUp.destroy()
            self.adminMainPage()

        self.frameMain.destroy()
        self.frameUp = Frame(self.main, width=400, height=300)
        self.frameUp.place(relx=0.3, rely=0.2)

        Label(self.frameUp, text='Name :').grid(row=0, column=3)
        self.entryUp2 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp2.grid(row=0, column=4)

        Label(self.frameUp, text='National ID :').grid(row=1, column=3)
        self.entryUp1 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp1.grid(row=1, column=4)

        Label(self.frameUp, text='Password :').grid(row=2, column=3)
        self.entryUp3 = Entry(self.frameUp, insertwidth=4, width=16, show='*')
        self.entryUp3.grid(row=2, column=4)

        Label(self.frameUp, text='Age YYYY-MM-DD:').grid(row=3, column=3)
        self.entryUp4 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp4.grid(row=3, column=4)

        Label(self.frameUp, text='Phone Number :').grid(row=4, column=3)
        self.entryUp5 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp5.grid(row=4, column=4)

        Label(self.frameUp, text='Address :').grid(row=5, column=3)
        self.entryUp6 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp6.grid(row=5, column=4)

        Label(self.frameUp, text='Salary :').grid(row=6, column=3)
        self.entryUp7 = Entry(self.frameUp, insertwidth=4, width=16)
        self.entryUp7.grid(row=6, column=4)

        Label(self.frameUp, text='Gender :').grid(row=7, column=3)
        gender_var = StringVar(value='Male')
        Radiobutton(self.frameUp, text='Male', variable=gender_var,
                    value='Male').grid(row=7, column=4)
        Radiobutton(self.frameUp, text='Female', variable=gender_var,
                    value='Female').grid(row=7, column=5)

        Button(self.frameUp, text='Create Account',
               command=onSignUp).grid(row=10, column=4)

    def closeTellerAccount(self):
        top = Toplevel(self.main)
        top.title("Close Account")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        def close():
            target_user_id = entryTarget.get()

            if not target_user_id.isdigit():
                self.errorPage(
                    "Error", "Please enter valid Customer Id.")
                return
            target_user_id = int(target_user_id)
            for teller in bank.Tellers:
                if teller.TellerId == target_user_id:
                    confirmation = askyesno(
                        "Confirmation", "Are you sure you want to close this account?")
                    if confirmation:
                        bank.Tellers.remove(teller)
                        self.infoPage("Done", "account has been closed.")
                        top.destroy()
                    return
            self.errorPage("Error", "Id Not Found.")

        Label(top, text="Teller ID:").grid(row=0, column=0)
        entryTarget = Entry(top)
        entryTarget.grid(row=0, column=1)

        Button(top, text="Close Account", command=close).grid(
            row=1, columnspan=2)

    def depositPage(self):
        top = Toplevel(self.main)
        top.title("Deposit Money")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        def deposit():
            amount = entryAmount.get()

            amount = int(amount)

            for user in bank.Users:
                if user.Id == self.currentUserId:
                    if amount > 0:
                        user.balance += amount
                        bank.money += amount
                        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        user.log.append(f"you Deposited {amount} \nat {date}\n-------------------------------")
                        bank.Log.append(
                            f"Customer: {user.name} \nDeposited: {amount} \nat {date}\n-------------------------------")
                        self.infoPage("Success", f"Deposited {amount} to {user.name}'s account.")
                        top.destroy()
                    else:
                        self.errorPage(
                            "Error", "Please enter a positive number.")

        Label(top, text="Enter Amount:").grid(row=0, column=0)
        entryAmount = Entry(top)
        entryAmount.grid(row=0, column=1)

        Button(top, text='Deposit', command=deposit).grid(row=2, columnspan=2)

    def depositPageTeller(self):
        top = Toplevel(self.main)
        top.title("Deposit Money")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        def deposit():
            customer_id = entryCustomerId.get()
            amount = entryAmount.get()
            tellerName = ""
            if not customer_id.isdigit() or not amount.isdigit():
                self.errorPage(
                    "Error", "Please enter valid Customer ID and Amount.")
                return

            amount = int(amount)
            customer_id = int(customer_id)

            for user in bank.Tellers:
                if user.Id == self.currentTellerId:
                    tellerName = user.name

            for user in bank.Users:
                if user.customerId == customer_id:
                    if amount > 0:
                        user.balance += amount
                        bank.money += amount
                        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        user.log.append(
                            f"our teller: {tellerName} \nDeposited {amount} \nat {date}\n-------------------------------")
                        bank.Log.append(
                            f"Teller: {tellerName}  \nDeposited: {amount} \nFor Customer: {user.name}\nat {date}\n-------------------------------")
                        self.infoPage("Success", f"Deposited {amount} to {user.name}'s account.")
                        top.destroy()
                    else:
                        self.errorPage(
                            "Error", "Please enter a positive number.")
                else:
                    self.errorPage("Error", "Customer ID not found.")
                break

        Label(top, text="Customer ID:").grid(row=0, column=0)
        entryCustomerId = Entry(top)
        entryCustomerId.grid(row=0, column=1)

        Label(top, text="Enter Amount:").grid(row=1, column=0)
        entryAmount = Entry(top)
        entryAmount.grid(row=1, column=1)

        Button(top, text='Deposit', command=deposit).grid(row=2, columnspan=2)

    def calculate_age(self, birthdate_str):
        try:
            birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - birthdate.year

            if (today.month, today.day) < (birthdate.month, birthdate.day):
                age -= 1
            return age
        except ValueError:
            self.errorPage("Error", "Invalid date format. Use YYYY-MM-DD.")
            return False

    def withdrawPage(self):
        top = Toplevel(self.main)
        top.title("Withdraw Money")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        def withdraw():
            amount = entryAmount.get()

            if not amount.isdigit():
                self.errorPage(
                    "Error", "Please enter valid Customer ID and Amount.")
                return

            amount = int(amount)

            for user in bank.Users:
                if user.Id == self.currentUserId:
                    if amount > user.balance:
                        self.errorPage("Error", "Insufficient funds.")
                        entryAmount.delete(0, END)
                    elif amount <= 0:
                        self.errorPage(
                            "Error", "Please enter a positive number.")
                        entryAmount.delete(0, END)
                    else:
                        user.balance -= amount
                        bank.money -= amount
                        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        user.log.append(f"you Withdrew {amount} \nat {date}\n-------------------------------")
                        bank.Log.append(
                            f"Customer: {user.name} \nWithdrew: {amount} \nat {date}\n-------------------------------")
                        self.infoPage("Success", f"Withdrew {amount} from {user.name}'s account.")
                        top.destroy()
                    break

        Label(top, text="Enter Amount:").grid(row=1, column=0)
        entryAmount = Entry(top)
        entryAmount.grid(row=1, column=1)
        entryAmount.focus_set()

        Button(top, text='Withdraw', command=withdraw).grid(
            row=2, columnspan=2)

    def withdrawPageTeller(self):
        top = Toplevel(self.main)
        top.title("Withdraw Money")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        def withdraw():
            customer_id = entryCustomerId.get()
            amount = entryAmount.get()
            tellerName = ""

            if not customer_id.isdigit() or not amount.isdigit():
                self.errorPage(
                    "Error", "Please enter valid Customer ID and Amount.")
                return

            amount = int(amount)
            customer_id = int(customer_id)

            for user in bank.Tellers:
                if user.Id == self.currentTellerId:
                    tellerName = user.name

            for user in bank.Users:
                if user.customerId == customer_id:

                    if user.balance >= amount > 0:
                        user.balance -= amount
                        bank.money -= amount
                        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        user.log.append(
                            f"our teller: {tellerName} \nWithdrew {amount} \nat {date}\n-------------------------------")
                        bank.Log.append(
                            f"Teller: {tellerName}  \nWithdrew: {amount} \nFor Customer: {user.name}\nat {date}\n-------------------------------")
                        self.infoPage("Success", f"Withdrew {amount} from {user.name}'s account.")
                        top.destroy()
                    elif amount <= 0:
                        self.errorPage(
                            "Error", "Please enter a positive number.")
                    else:
                        self.errorPage("Error", "Insufficient funds.")
                else:
                    self.errorPage("Error", "Customer ID not found.")

        Label(top, text="Customer ID:").grid(row=0, column=0)
        entryCustomerId = Entry(top)
        entryCustomerId.grid(row=0, column=1)

        Label(top, text="Enter Amount:").grid(row=1, column=0)
        entryAmount = Entry(top)
        entryAmount.grid(row=1, column=1)

        Button(top, text='Withdraw', command=withdraw).grid(
            row=2, columnspan=2)

    def viewBankLog(self):
        top = Toplevel(self.main)
        top.title("Transaction Log")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        frame = Frame(top)
        frame.pack(padx=10, pady=10)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        text = Text(frame, yscrollcommand=scrollbar.set)
        text.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar.config(command=text.yview)

        if bank.Log:
            log_info = "\n".join(bank.Log)
        else:
            log_info = "No transactions recorded."

        text.insert(END, log_info)

        text.config(state=DISABLED)

        close_button = Button(top, text="Close", command=top.destroy)
        close_button.pack(pady=10)

    def viewLog(self):
        top = Toplevel(self.main)
        top.title("Transaction Log")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        frame = Frame(top)
        frame.pack(padx=10, pady=10)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        text = Text(frame, yscrollcommand=scrollbar.set)
        text.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar.config(command=text.yview)

        for user in bank.Users:
            if user.Id == self.currentUserId:
                log_info = "\n".join(
                    user.log) if user.log else "No transactions yet."
                break
        else:
            log_info = "User not found."

        text.insert(END, log_info)

        text.config(state=DISABLED)

        close_button = Button(top, text="Close", command=top.destroy)
        close_button.pack(pady=10)

    def viewLogTeller(self):
        top = Toplevel(self.main)
        top.title("View Customer Log")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        Label(top, text="Customer ID:").grid(row=0, column=0)
        entryCustomerId = Entry(top)
        entryCustomerId.grid(row=0, column=1)

        def viewLog():
            userId = entryCustomerId.get()
            if not userId.isdigit():
                self.errorPage("Error", "Please enter a valid Customer ID")
                return
            userId = int(userId)

            log_frame = Frame(top)
            log_frame.grid(row=2, columnspan=2, pady=10)

            scrollbar = Scrollbar(log_frame)
            scrollbar.pack(side=RIGHT, fill=Y)

            text = Text(log_frame, yscrollcommand=scrollbar.set,
                        width=50, height=10)
            text.pack(side=LEFT, fill=BOTH, expand=1)
            scrollbar.config(command=text.yview)

            for user in bank.Users:
                if user.customerId == userId:
                    log_info = "\n".join(
                        user.log) if user.log else "No transactions yet."
                    text.insert(END, log_info)
                    break
            else:
                self.errorPage("Error", "Customer Not Found")
                return

            text.config(state=DISABLED)

        Button(top, text='View Log', command=viewLog).grid(row=1, columnspan=2)

    def showAllCustomers(self):
        Top = Toplevel(self.main)
        Top.title("All Customers")
        Top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        frame = Frame(Top)
        frame.pack(padx=10, pady=10)

        if len(bank.Users) == 0:
            user_info = "No customers yet."
            label = Label(frame, text=user_info)
            label.pack(anchor='w')
        else:
            for user in bank.Users:
                user_info = (
                    f"ID: {user.Id} | "
                    f"Customer ID: {user.customerId} | "
                    f"Name: {user.name} | "
                    f"Age: {user.age} | "
                    f"Gender: {user.gender} | "
                    f"Phone: {user.phoneNumber} | "
                    f"Address: {user.address} | "
                    f"Salary: {user.salary:.2f} | "
                    f"Balance: {user.balance:.2f} | "
                    f"Account Type: {user.account_type} | "
                    f"Opened: {user.opened}"
                )
                label = Label(frame, text=user_info)
                label.pack(anchor='w')

        close_button = Button(Top, text="Close", command=Top.destroy)
        close_button.pack(pady=10)

    def showAllTellers(self):
        Top = Toplevel(self.main)
        Top.title("All Tellers")
        Top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        frame = Frame(Top)
        frame.pack(padx=10, pady=10)

        for teller in bank.Tellers:
            teller_info = (
                f"ID: {teller.Id} | "
                f"Teller ID: {teller.TellerId} | "
                f"Name: {teller.name} | "
                f"Age: {teller.age} | "
                f"Gender: {teller.gender} | "
                f"Phone: {teller.phoneNumber} | "
                f"Address: {teller.address} | "
                f"Salary: {teller.salary:.2f}"
            )
            label = Label(frame, text=teller_info)
            label.pack(anchor='w')

        close_button = Button(Top, text="Close", command=Top.destroy)
        close_button.pack(pady=10)

    def editCustomerInfo(self):
        def find_user():
            customer_id = entryCustomerId.get()
            for user in bank.Users:
                if str(user.customerId) == customer_id:
                    populate_fields(user)
                    return
            self.errorPage("Error", "Customer ID not found.")

        def populate_fields(user):
            entryName.delete(0, END)
            entryName.insert(0, user.name)
            entryAge.delete(0, END)
            entryAge.insert(0, user.age)
            entryGender.delete(0, END)
            entryGender.insert(0, user.gender)
            entryPhone.delete(0, END)
            entryPhone.insert(0, user.phoneNumber)
            entryAddress.delete(0, END)
            entryAddress.insert(0, user.address)
            entrySalary.delete(0, END)
            entrySalary.insert(0, user.salary)
            account_type_var.set(user.account_type)

        def update_info():
            user = bank.Users[self.currentUserId]
            user.name = entryName.get()
            user.age = entryAge.get()
            user.gender = entryGender.get()
            user.phoneNumber = entryPhone.get()
            user.address = entryAddress.get()
            user.salary = float(entrySalary.get())
            user.account_type = account_type_var.get()
            self.infoPage(
                "Update", "Customer information updated successfully!")
            top.destroy()

        top = Toplevel(self.main)
        top.title("Edit Customer Information")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        Label(top, text="Customer ID:").grid(row=0, column=0)
        entryCustomerId = Entry(top)
        entryCustomerId.grid(row=0, column=1)
        Button(top, text="Find Customer",
               command=find_user).grid(row=0, column=2)

        Label(top, text="Name:").grid(row=1, column=0)
        entryName = Entry(top)
        entryName.grid(row=1, column=1)

        Label(top, text="Age:").grid(row=2, column=0)
        entryAge = Entry(top)
        entryAge.grid(row=2, column=1)

        Label(top, text="Gender:").grid(row=3, column=0)
        entryGender = Entry(top)
        entryGender.grid(row=3, column=1)

        Label(top, text="Phone Number:").grid(row=4, column=0)
        entryPhone = Entry(top)
        entryPhone.grid(row=4, column=1)

        Label(top, text="Address:").grid(row=5, column=0)
        entryAddress = Entry(top)
        entryAddress.grid(row=5, column=1)

        Label(top, text="Salary:").grid(row=6, column=0)
        entrySalary = Entry(top)
        entrySalary.grid(row=6, column=1)

        Label(top, text="Account Type:").grid(row=7, column=0)
        account_type_var = StringVar()
        Radiobutton(top, text='Savings', variable=account_type_var,
                    value='Savings').grid(row=7, column=1)
        Radiobutton(top, text='Checking', variable=account_type_var,
                    value='Checking').grid(row=7, column=2)

        Button(top, text="Update", command=update_info).grid(
            row=8, columnspan=3)

    def closeAccount(self):
        top = Toplevel(self.main)
        top.title("Close Account")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        def close():
            target_user_id = entryTarget.get()

            if not target_user_id.isdigit():
                self.errorPage(
                    "Error", "Please enter valid Customer Id.")
                return
            target_user_id = int(target_user_id)
            for user in bank.Users:
                if user.customerId == target_user_id:
                    confirmation = messagebox.askyesno(
                        "Confirmation", "Are you sure you want to close this account?")
                    if confirmation:
                        bank.Users.remove(user)
                        self.infoPage("Done", "account has been closed.")
                        top.destroy()
                    return
            self.errorPage("Error", "Id Not Found.")

        Label(top, text="Customer ID:").grid(row=0, column=0)
        entryTarget = Entry(top)
        entryTarget.grid(row=0, column=1)

        Button(top, text="Close Account", command=close).grid(
            row=2, columnspan=2)

    def searchCustomer(self):
        top = Toplevel(self.main)
        top.title("Customer Information")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        def search():
            target_user_id = entryTarget.get()
            if not target_user_id.isdigit():
                self.errorPage("Error", "Please enter a valid Customer ID.")
                return
            target_user_id = int(target_user_id)

            for user in bank.Users:
                if user.customerId == target_user_id:
                    result_window = Toplevel(self.main)
                    result_window.title("Customer Details")

                    Label(result_window, text="Customer ID:").grid(row=0, column=0, sticky='w')
                    Label(result_window, text=user.customerId).grid(row=0, column=1, sticky='w')
                    Label(result_window, text="Name:").grid(row=1, column=0, sticky='w')
                    Label(result_window, text=user.name).grid(row=1, column=1, sticky='w')
                    Label(result_window, text="Age:").grid(row=2, column=0, sticky='w')
                    Label(result_window, text=user.age).grid(row=2, column=1, sticky='w')
                    Label(result_window, text="Gender:").grid(row=3, column=0, sticky='w')
                    Label(result_window, text=user.gender).grid(row=3, column=1, sticky='w')
                    Label(result_window, text="Phone Number:").grid(row=4, column=0, sticky='w')
                    Label(result_window, text=user.phoneNumber).grid(row=4, column=1, sticky='w')
                    Label(result_window, text="Address:").grid(row=5, column=0, sticky='w')
                    Label(result_window, text=user.address).grid(row=5, column=1, sticky='w')
                    Label(result_window, text="Salary:").grid(row=6, column=0, sticky='w')
                    Label(result_window, text=user.salary).grid(row=6, column=1, sticky='w')
                    Label(result_window, text="Balance:").grid(row=7, column=0, sticky='w')
                    Label(result_window, text=user.balance).grid(row=7, column=1, sticky='w')
                    Label(result_window, text="Account Type:").grid(row=8, column=0, sticky='w')
                    Label(result_window, text=user.account_type).grid(row=8, column=1, sticky='w')
                    Label(result_window, text="Opened:").grid(row=9, column=0, sticky='w')
                    Label(result_window, text=user.opened).grid(row=9, column=1, sticky='w')

                    return

            self.errorPage("Error", "Customer ID not found.")

        Label(top, text="Customer ID:").grid(row=0, column=0)
        entryTarget = Entry(top)
        entryTarget.grid(row=0, column=1)

        Button(top, text="Search", command=search).grid(row=2, columnspan=2)

    def searchTeller(self):
        top = Toplevel(self.main)
        top.title("Teller Information")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        def search():
            target_teller_id = entryTarget.get()
            if not target_teller_id.isdigit():
                self.errorPage("Error", "Please enter a valid Teller ID.")
                return
            target_teller_id = int(target_teller_id)
            for teller in bank.Tellers:
                if teller.TellerId == target_teller_id:
                    result_window = Toplevel(self.main)
                    result_window.title("Teller Details")

                    Label(result_window, text="Teller ID:").grid(row=0, column=0, sticky='w')
                    Label(result_window, text=teller.TellerId).grid(row=0, column=1, sticky='w')
                    Label(result_window, text="Name:").grid(row=1, column=0, sticky='w')
                    Label(result_window, text=teller.name).grid(row=1, column=1, sticky='w')
                    Label(result_window, text="Age:").grid(row=2, column=0, sticky='w')
                    Label(result_window, text=teller.age).grid(row=2, column=1, sticky='w')
                    Label(result_window, text="Gender:").grid(row=3, column=0, sticky='w')
                    Label(result_window, text=teller.gender).grid(row=3, column=1, sticky='w')
                    Label(result_window, text="Phone Number:").grid(row=4, column=0, sticky='w')
                    Label(result_window, text=teller.phoneNumber).grid(row=4, column=1, sticky='w')
                    Label(result_window, text="Address:").grid(row=5, column=0, sticky='w')
                    Label(result_window, text=teller.address).grid(row=5, column=1, sticky='w')
                    Label(result_window, text="Salary:").grid(row=6, column=0, sticky='w')
                    Label(result_window, text=teller.salary).grid(row=6, column=1, sticky='w')

                    return

            self.errorPage("Error", "Teller ID not found.")

        Label(top, text="Teller ID:").grid(row=0, column=0)
        entryTarget = Entry(top)
        entryTarget.grid(row=0, column=1)

        Button(top, text="Search", command=search).grid(row=2, columnspan=2)

    def requestLoan(self):

        for user in bank.Users:
            if user.Id == self.currentUserId:
                user = user
        if user:
            if user.LoanActive == False:
                Top = Toplevel(self.main)
                Top.title("Request Loan")
                Top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

                frame = Frame(Top)
                frame.pack(padx=10, pady=10)

                Label(frame, text="Enter Loan Amount:").grid(row=0, column=0, sticky='w')
                loan_amount_entry = Entry(frame)
                loan_amount_entry.grid(row=0, column=1, sticky='w')

                Label(frame, text="Interest Rate (annual %):").grid(row=1, column=0, sticky='w')
                interest_rate_entry = Entry(frame)
                interest_rate_entry.grid(row=1, column=1, sticky='w')

                Label(frame, text="Loan Term (months):").grid(row=2, column=0, sticky='w')
                loan_term_entry = Entry(frame)
                loan_term_entry.grid(row=2, column=1, sticky='w')

                def calculateMonthlyPayment(principal, annual_rate, months):
                    monthly_rate = annual_rate / 100 / 12
                    if monthly_rate == 0:
                        return principal / months
                    return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)

                def submitLoan():
                    try:
                        loan_amount = float(loan_amount_entry.get())
                        annual_rate = float(interest_rate_entry.get())
                        loan_term = int(loan_term_entry.get())
                        if loan_amount <= 0 or annual_rate <= 0 or loan_term <= 0:
                            self.errorPage("Error",
                                           "Loan amount, interest rate and loan term must be greater than zero.")

                        if user.balance >= 1000:
                            monthly_payment = calculateMonthlyPayment(loan_amount, annual_rate, loan_term)
                            user.balance += loan_amount
                            user.loan = monthly_payment
                            user.loanMonths = loan_term
                            user.LoanActive = True
                            messagebox.showinfo("Success",
                                                f"Loan of {loan_amount:.2f} granted!\n"
                                                f"Monthly payment: {monthly_payment:.2f} for {loan_term} months.")
                            Top.destroy()
                        else:
                            messagebox.showwarning("Eligibility", "Insufficient balance for loan eligibility.")

                    except ValueError:
                        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

                submit_button = Button(frame, text="Request Loan", command=submitLoan)
                submit_button.grid(row=3, column=0, columnspan=2, pady=10)

            else:
                Top = Toplevel(self.main)
                Top.title("Request Loan")
                Top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

                Label(Top, text="Monthly Payment:").grid(row=1, column=0)
                Label(Top, text=f"{user.loan:.2f}").grid(row=1, column=1)

                Label(Top, text="Months :").grid(row=2, column=0)
                Label(Top, text=user.loanMonths).grid(row=2, column=1)

    def transferFunds(self):
        top = Toplevel(self.main)
        top.title("Transfer Funds")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        def transfer():
            target_user_id = entryTarget.get()
            amount = entryAmount.get()
            if not amount.isdigit() or not target_user_id.isdigit():
                self.errorPage(
                    "Error", "Please enter valid IDs and amounts.")
                return

            amount = int(amount)
            target_user_id = int(target_user_id)

            for user in bank.Users:
                if user.Id == self.currentUserId:
                    if user.balance >= amount:
                        for target_user in bank.Users:
                            if target_user.Id == self.currentUserId:
                                self.errorPage(
                                    "Error", "You cant send money to yourself")
                                return
                            if target_user.customerId == target_user_id:
                                user.balance -= amount
                                target_user.balance += amount
                                date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                                user.log.append(
                                    f"Transferred {amount} to {target_user.name} \nat {date}\n-------------------------------")
                                target_user.log.append(
                                    f"Received {amount} from {user.name} \nat {date}\n-------------------------------")
                                bank.Log.append(
                                    f"Customer: {user.name}  \nTransferred: {amount} \nto Customer: {target_user.name}\nat {date}\n-------------------------------")
                                top.destroy()
                                self.infoPage("Success ", f"Transferred {amount} to {target_user.name}.")
                                return
                        self.errorPage("Error", "Target user not found.")
                        return
                    else:
                        self.errorPage("Error", "Insufficient funds.")
                        return

        Label(top, text="Target User ID:").grid(row=0, column=0)
        entryTarget = Entry(top)
        entryTarget.grid(row=0, column=1)

        Label(top, text="Amount:").grid(row=1, column=0)
        entryAmount = Entry(top)
        entryAmount.grid(row=1, column=1)

        Button(top, text="Transfer", command=transfer).grid(
            row=2, columnspan=2)

    def changePassword(self):
        top = Toplevel(self.main)
        top.title("Change Password")
        top.geometry("+%d+%d" % (self.main.winfo_x() + 200, self.main.winfo_y() + 200))

        def update_password():
            new_password = entryNewPass.get()
            if new_password:
                for user in bank.Users:
                    if user.Id == self.currentUserId:
                        user.password = new_password
                        self.infoPage(
                            "Success", "Password changed successfully.")
                        top.destroy()
                        return
            self.errorPage("Error", "Please enter a new password.")

        Label(top, text="New Password:").grid(row=0, column=0)
        entryNewPass = Entry(top, show='*')
        entryNewPass.grid(row=0, column=1)

        Button(top, text="Change Password",
               command=update_password).grid(row=1, columnspan=2)

    def logout(self):
        self.frameMain.destroy()
        self.welcomePage()

    def errorPage(self, main, txt):
        messagebox.showerror(main, txt)

    def warningPage(self, main, txt):
        messagebox.showwarning(main, txt)

    def infoPage(self, main, txt):
        messagebox.showinfo(main, txt)


if __name__ == '__main__':
    main = Tk()
    bank = Bank('Al Ahly', 'El Dokki, Egypt', 0)
    user = GUi(main)
    user.welcomePage()
    main.mainloop()
