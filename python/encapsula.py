class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
      # self.balance = balance
        self.__balance = balance#private variable

    def deposit(self,amount):
        self.__balance += amount
        print(f'deposited{amount}.new balance')
    def get_balance(self):
        return self.__balance#controlled access
    
account = BankAccount('1234',5000)   
    
account.deposit(2000)
print(account.get_balance())

#print(account._balance)this gives attribute error