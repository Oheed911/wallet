#wallet class
#create a class of wallet with balance as a atribute and setAmmount(), getAmmount and removeAmmount() as methods
class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def setAmmount(self, ammount):
        self.balance = ammount
        return self.balance

    def getAmmount(self, ammount):
        return self.balance

    def removeAmmount(self):
        self.balance = 0
        return self.balance
        