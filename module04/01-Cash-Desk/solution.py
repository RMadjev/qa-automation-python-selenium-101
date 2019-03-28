class Bill:

    def __init__(self, amount):
        if amount < 0:
            raise ValueError

        if not isinstance(amount, int):
            raise TypeError

        self.amount = amount

    def __str__(self):
        return "A " + str(self.amount) + "$ bill"

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other

    def __hash__(self):
        return hash(self.__str__())


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum([int(amount) for amount in self.bills])

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:
    money = 0
    bills = []

    def take_money(self, bill):
        if isinstance(bill, BatchBill):
            self.money += bill.total()
            for b in range(len(bill)):
                self.bills.append(bill[b])
        else:
            self.money += bill.amount
            self.bills.append(bill)

    def total(self):
        return self.money

    def inspect(self):
        table = "We have a total of " + str(self.money) + "$ in the desk\n"
        table += "We have the following count of bills, sorted in ascending order:\n"
        bills_by_amount = {}
        for bill in self.bills:
            if bill.amount not in bills_by_amount:
                bills_by_amount[bill.amount] = [bill]
            else:
                bills_by_amount[bill.amount].append(bill)

        list = [amount for amount in bills_by_amount.keys()]
        list.sort()

        for key in list:
            table += str(key) + '$ bills - ' + str(len(bills_by_amount[key])) + '\n'

        return table.strip()




