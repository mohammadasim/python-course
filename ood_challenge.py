class Bank_Account:

    def __init__(self, account_holder_name, current_balance):
        self.account_holder_name = account_holder_name
        self.current_balance = current_balance

    def __str__(self):
        return 'Account name: {}\nBalance: {}'.format(self.account_holder_name,self.current_balance)

    def deposit(self,amount):
        try:
            val = float(amount)
            self.current_balance = self.current_balance + val
        except ValueError as wrongInput:
            print(wrongInput)

    def withdraw_funds(self,amount):
        try:
            val = float(amount)
            if val <= self.current_balance:
                self.current_balance = self.current_balance - val
                print('Withdrawal Successful. Current Balance is {}'.format(self.current_balance))
            else:
                print("You don't have enough funds to make this withdrawal.")
        except ValueError as wrongInput:
            print(wrongInput)
        


myCurrentAccount= Bank_Account('Alex', 1000)
print(myCurrentAccount)
myCurrentAccount.deposit(1000)
print(myCurrentAccount.current_balance)
myCurrentAccount.withdraw_funds(5000)
    