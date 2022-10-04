class User: #THIS IS THE CORE OF THIS ASSIGNMENT - it was asking for this User class to be created and associated with the BankAccount class, I did this under the __ini__ method with the self.account = BankAccount(etc.)
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

#copied and pasted below from the previous BankAccount assignment to add additional functionality in this Users with Bank Account assignment.

class BankAccount: #created a class called "BankAccount"
    account = [] # this is going to be used for the @class method, it is a variable attached to this BankAccount class
    balance = 0  # these are attributes that belong to this class only
    int_rate = 0.00

    def __init__(self, int_rate, balance): # here is where i can initiate instances of the class
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account.append(self) #this adds to the list account variable when a new instance gets created
    
    def deposit(self, amount): 
        self.balance = self.balance + amount
        print(f"You deposited {amount}")
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance = self.balance - amount
            print(f"You withdrew {amount}")
        else: 
            print("Insufficient funds: Charging a $5 fee") 
            self.balance = self.balance - 5 
        return self
    
    def display_account_info(self):
        print("You're balance is", str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        print(f"You're interest is {self.int_rate}")
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.account:
            account.display_account_info()

Steven = BankAccount(0.05, 1000) # initializing an instance of Bank Account for Steven 

Maggie = BankAccount(0.10, 500)
Honey = BankAccount(0.025, 2000)