class Bank:
    totalBalance = 0
    totalLoanAmount = 0
    loanActive = True
    users = {}
    admins = {}

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def addUser(self, user):
        Bank.users[user.accountNumber] = user

    def addAdmin(self, admin):
        Bank.admins[admin.adminId] = admin

    def getLoanAmount(self, adminId):
        if adminId in self.admins:
            return Bank.totalLoanAmount
        else:
            return "Only admins can check the total loan amount."
    
    def checkBankBalance(self, adminId):
        if adminId in self.admins:
            return Bank.totalBalance
        else:
            return "Only admins can check the bank balance."

    

    def changeLoanFeature(self, adminId):
        if adminId in self.admins:
            Bank.loanActive = not Bank.loanActive
            return f"Loan feature is {'active' if Bank.loanActive else 'disabled'}."
        else:
            return "Only admins can change the loan functionality"

    def __repr__(self) -> str:
        print(" ")
        print(" ")
        print(" ")
        print(f"*********Bank Name:{self.name}*********")
        print(" ")
        print(f"##########Bank-Information#############")
        print(" ")
        print(" ")
        print(" ")
        print(f"Total Balance: {self.totalBalance}")
        print(f"Total Loan: {self.totalLoanAmount}")
        print(f"Loan Status: {self.loanActive}")
        print(" ")
        print(f"############Bank Admins#########")
        print(" ")
        print("--------------------")
        for key, admin in self.admins.items():
            print(f"Name: {admin.name}")
            print(f"Id: {key}")
            print(f"Email: {admin.email}")
        print(" ")
        print(f"===========Bank Users==========")
        print(" ")
        
        
        ####looping all users account information
        
        for key, user in self.users.items():
            print(f"Name: {user.name}")
            print(f"Account Number: {key}")
            print(f"Balance: {user.balance}")
            print(f"Loan Amount: {user.loanAmount}")
            print(f"Transaction History: not a match fixing in cricket {user.transactionHistory}")
            print("---------end-----------")

        return ""