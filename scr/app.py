class Bank():
    def __init__(self):
        self.balance = 0
        self.extract = []
    

    def withdraw(self, amount):
        
        if (amount <= 0):
            return print("Incorrect value")
            
        elif (amount > self.balance):
            return print("Amount reported above the balance")
        
        else:
            self.balance -= amount
            self.extract.append(amount)


    def deposit(self, amount):
        pass


    def view_extract(self):
        pass