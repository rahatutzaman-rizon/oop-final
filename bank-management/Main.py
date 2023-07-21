#import part

from Bank import Bank
from Admin import Admin
from User import User


def main():
    bank = Bank("Dhaka Bank", "Dhaka")

    # create admin
    admin1 = Admin("redwan-tamim", "redwantamim525@gmail.com", "12345", bank)
    admin2 = Admin("rizon-rahat", "rizonrahat@gmail.com", "54321", bank)
    admin3 = Admin("rizon-rahat", "rizonrahat@gmail.com", "54321", bank)
   
    #admin in bank 
    bank.addAdmin(admin1)
    bank.addAdmin(admin2)
    bank.addAdmin(admin3)

    # create user three
    
    user1 = User("sakib al hasan", "sakib75@gmail.com", "1234")
    user2 = User("tamim iqbal", "tamim29@gmail.com", "4321")
    user3 = User("musfiqur rahim", "mushfiq@gmail.com", "4321")
    
    # add user to bank by admin
    
    admin1.create_account(user1)
    admin1.create_account(user2)
    admin2.create_account(user3)

    # deposit money of 3 users
    
    user1.deposit_money(50000)
    user2.deposit_money(10000)
    user3.deposit_money(30000)

    # withdraw
    withdraw1 = user1.withdraw_money(2500)
    print(withdraw1)
    
    withdraw2=user2.withdraw_money(5000)
    print(withdraw2)
    # check Balance
    print(f" after withdraw Balance user1: {user1.checkBalance()}")
    print(f" after withdraw Balance user2: {user2.checkBalance()}")

    # transfer money
    money_transfer = user2.transfer(1000, user3)
    print(money_transfer)
    
    money_transfer2=user3.transfer(1500,user1)
    print(money_transfer2)

    # check transaction history
    print(user2.checkTransactionHistory())

    # take loan
    bank_loan = user1.takeLoan()
    print(bank_loan)
    
    
    #user3 can withdraw the transfer money
    user3.withdraw_money(1000)
    

    # admin check balance
    total_balance = admin1.checkBankBalance()
    print(f"Total Balance: {total_balance}")

    # admin check loan amount
    total_loan = admin1.checkLoanAmount()
    print(f"Total Loan : {total_loan}")

    # admin can change loan
    admin1.changeLoanFeature()

    print(bank)


if __name__ == "__main__":
    main()