
from datetime import datetime
class BankAccount:
class Account:

    def __init__(self, bank, phone_number, first_name, last_name):
        self.bank = bank
    def __init__(self, phone_number, first_name, last_name):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        loan = {}
        self.loan = 0
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_repayments = []


    def getCurrentTime(self):
@@ -20,15 +20,12 @@ def getCurrentTime(self):

    def account_name(self):
        time = self.getCurrentTime()
        name = "{} account for  {} {} at ".format(self.bank, self.first_name,self.last_name, time)
        name = "Account for  {} {} at ".format(self.first_name,self.last_name, time)

        return name


    def deposit(self, amount):



        amount = input("Enter the amount you want to deposit : ")
        try:
            amount = int(amount)
@@ -42,7 +39,7 @@ def deposit(self, amount):
            self.deposits.append(amount) 
            time = self.getCurrentTime()

            print("You have deposited {} to {} on {} ".format(amount, self.account_name(),time)) 
            print("You have deposited {} to {} {} on {} ".format(amount, self.account_name(),time)) 


    def withdraw(self, amount):
@@ -115,18 +112,80 @@ def repay_loan(self,amount):
        else:
            time = self.getCurrentTime()
            self.loan -= amount
            repayment= {"time": time, "amount": amount}
            self.loan_repayments.append(repayment)
            print("Dear Customer, you have repaid your loan with {} , your loan balance is {} on {}".format(amount,self.loan,time))


    def loan_repayment_statement(self,repayment):
        for repayment in self.loan_repayments:
            time = repayment["time"]
            amount = repayment ["amount"]
            time = self.getCurrentTime()
            statement =("You have repaid {} on {}".format(amount, time) )
            print(statement)    



class BankAccount(Account):
    def __init__(self, first_name, last_name, phone_number, bank):
        self.bank = bank
        super().__init__(first_name, last_name, phone_number) 

class MobileMoneyAccount(Account):
    def __init__(self, first_name, last_name, phone_number, service_provider ):
        self.service_provider = service_provider
        self.airtime = []
        self.paybills = []
        super().__init__(first_name, last_name, phone_number)

    def buy_airtime(self,amount):
        try:
            amount +10 
        except TypeError:
            print("Enter the amount in figures.")   
            return

        if amount > self.balance:
            print("You dont have enough money. Your balance is {}".format(self.balance)) 
        else: 
            self.balance -= amount 
            time = self.getCurrentTime()
            airtime = amount
            self.airtime.append(airtime)
            print("You have bought airtime worth KSHs{} on {} ".format(amount, time))





    def paybill(self,amount):
        try:
            amount +10
        except:
            print("Dear Customer please enter the amount in figures.")    
        if amount <= 0:
            print ("Dear Customer kindly top up your balance to enjoy the service.")    
        elif amount > self.balance:
            print("Dear customer your balance is KSHs{} kindly enter an amount that is less than your balance .".format(self.balance))
        else:
            self.balance -= amount
            time = getCurrentTime.now()
            paybills = amount
            self.paybills.append(paybills)
            print("You transferred this amount KSHs {} on {}.".format(amount,time))
    def receive_money(self, amount):
        time = self.getCurrentTime()
        self.balance += amount
        print("You have received this amount KHSs {}, Your account balance is KSHs{} at {}".format(amount, self.balance, time))


    def send_money(self,amount):
        time = self.getCurrentTime()
        try:
            amount +10
        except:
            print("Dear customer please enter the amount in figures.")    
        if amount <= 0:
            print ("Dear Customer kindly top up your balance to enjoy the service.") 
        elif amount > self.balance:
            print("Dear customer your balance is KSHs {}  at {} kindly an amount that is less than your balance.".format( self.balance, time))  
        else:
            self.balance -= amount
            print("You have send this KSHs {}, Your account balance is KSHs{} at {}".format(amount, self.balance, time))