#Parent Class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)



#Child Classs
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Acount balance has been updated : $", self.balance)

    def withdrawal(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insuficient Funds | Balance Available : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Withdrawn Amount: $", self.amount)
            print("Acount balance has been updated : $", self.balance)

    def view_balance(self):
        self.show_details()
        print("Acount balance : $", self.balance)

#johan = Bank("Johan", 20, "Male")
#johan.deposit(1000)
#johan.view_balance()
#johan.withdrawal(1000)

#johan = User("Johan", 31, "Male")
#johan.show_details()
#print(johan.name)
#print(johan.age)
#print(johan.gender)