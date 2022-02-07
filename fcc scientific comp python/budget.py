class Category:
    def __init__(self, desc):
        self.des = desc
        self.ledger = []
        self.balance = 0.0

    def deposit(self, value, dep_typ=''):
        self.ledger.append({"amount": value, 'description': dep_typ})
        self.balance += value

    def withdraw(self, amount, spend_typ=''):
        if self.balance >= amount:
            self.ledger.append({"amount": -1*amount, 'description': spend_typ})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, transfer_obj):
        if self.balance >= amount:
            self.balance -= amount
            transfer_obj.balance += amount
            self.ledger.append({"amount": -1*amount, 'description': str('Transfer to ' + transfer_obj.des.capitalize())})
            transfer_obj.ledger.append({"amount": amount, 'description': str('Transfer from ' + self.des.capitalize())})
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def __str__(self):
        name = self.des
        name = name.capitalize()
        srep = name.center(30, '*') + '\n'
        for j in range(len(self.ledger)):
            des = self.ledger[j]["description"]
            am = "{0:.2f}".format(self.ledger[j]["amount"])
            leng = 30 - len(am)
            des = des.ljust(leng, ' ') if len(des) < leng else des[:leng-1] + ' '
            srep += des + am + '\n'
            srep += "Total: " + str(self.get_balance())
        return srep


def create_spend_chart(categories):
    spending = []
    for i in categories:
        i
        amoun = 0
        for j in range(len(i.ledger)):
            if i.ledger[j]['amount'] < 0:
                amoun += i.ledger[j]['amount']
            spending.append(abs(amoun))
        spending = [i*100/sum(spending) for i in spending]
        spending = [i//10 for i in spending]
    distr = "Percentage spent by category\n"
    for i in range(11):
        distr += str(10*(10-i)).rjust(3, ' ') + "| "
        for j in range(len(spending)):
            distr += 'o  ' if spending[j] >= 10-i else '   '
            distr += '\n'
    distr += '    ' + '-'*(3*len(categories)+1) + '\n'
    categories = [i.des.capitalize() for i in categories]
    catlen = max([len(i) for i in categories])
    for i in range(catlen):
        distr += '     '
        for j in range(len(categories)):
            distr += categories[j][i] + '  ' if i < len(categories[j]) else '   '
            if i < catlen-1:
                distr += '\n'
    return distr
