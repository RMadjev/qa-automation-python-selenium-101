class BankAccount:

    def __init__(self, name, balance, currency):
        if not currency or not name:
            raise ValueError
        self.name = name
        self.current_balance = balance
        self.currency = currency
        self.acc_history = []
        self.acc_history.append('Account was created')

    def balance(self):
        self.acc_history.append('Balance check -> {amount}{currency}'.format(amount=self.current_balance, currency=self.currency))
        return self.current_balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError

        self.acc_history.append('Deposited {amount}{currency}'.format(amount=amount, currency=self.currency))
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance < amount:
            return False
        self.acc_history.append('{amount}{currency} was withdrawn'.format(amount=amount, currency=self.currency))
        self.current_balance -= amount
        return True

    def __str__(self):
        self.acc_history.append('Balance check -> {amount}{currency}'.format(amount=self.current_balance, currency=self.currency))
        return "Bank account for {name} with balance of {amount}{currency}".format(name=self.name, amount=self.current_balance, currency=self.currency)

    def __int__(self):
        self.acc_history.append('__int__ check -> {amount}{currency}'.format(amount=self.current_balance, currency=self.currency))
        return self.current_balance

    def history(self):
        return self.acc_history

    def transfer_to(self, account, amount):
        if amount < 0:
            raise ValueError

        if account.currency != self.currency or amount > self.current_balance:
            raise TypeError

        if self.withdraw(amount):
            account.deposit(amount)

        return True
