class Bank():
    def __init__(self):
        self.balance = 0
        self.extract = {"withdraw": [], "deposit": []}
    

    def withdraw(self, amount):
        
        if (amount <= 0):
            return print("Incorrect value")
            
        elif (amount > self.balance):
            return print("Amount reported above the balance")
        
        elif (amount > 500):
            print("Maximum withdrawal limit of R$500")
        
        else:
            self.balance -= amount
            self.extract["withdraw"].append(amount)


    def deposit(self, amount):
        
        if (amount <= 0):
            print("Incorrect value")

        else:
            self.balance += amount
            self.extract["deposit"].append(amount)


    def view_extract(self):
        pass
