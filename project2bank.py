class user():
    def __init__(self,fn,ln,age,gender):
        self.fn = fn.strip().title()
        self.ln = ln.strip().title()
        self.age = age
        self.gender = gender
       # self.email = f"{self.fn.lower()}.{self.ln.lower()}@gmail.com"
    def showdetails(self):
        print(f"firstname : {self.fn}\n lastname : {self.ln}\n age : {self.age} \n gender:{self.gender}")
class bank(user):
    bankuser=0
    __balance=0
    def __init__(self,fn,ln,age,gender):
        super().__init__(fn,ln,age,gender)
        bank.bankuser=bank.bankuser + 1
        self.ac=bank.bankuser
        self.bankac= (f"bankac0001{self.ac}")
    def showdetails(self):
        print(f"firstname : {self.fn}\n lastname : {self.ln}\n age : {self.age} \n gender:{self.gender}")
        print(f"Your bank account no is {self.bankac}")
        print(f"your bank account {self.bankac} has balance of {self.__balance}")
    def deposit(self,deposited):
        self.deposited=deposited
        self.__balance=self.__balance+self.deposited
        print(f"your balance after updating is {self.__balance}")
    def withdraw(self,withdrawn):
        self.withdrawn=withdrawn
        if (self.withdrawn>self.__balance):
            print("sorry! you have insufficient balance")
        elif (self.withdrawn >=100 and self.withdrawn<= self.__balance):
            self.__balance=self.__balance-self.withdrawn
            print(f"your balance after withdrawing is {self.__balance}")
        else:
            print("please enter correct amount")
    def transfer(self,username,amount):
        self.amount=amount
        
        if (self.amount>self.__balance):
            print("sorry! you have insufficient balance")
        elif (self.amount >=1 and self.amount<= self.__balance):
            self.__balance=self.__balance - self.amount
            print(f"your balance after transfering {self.amount} is {self.__balance}")
        else:
            print("please enter correct amount")
        username.__balance=username.__balance+self.amount
        
user1=bank("Rahul","Kotecha",21,"Male")
user2=bank("Yash","Gajra",24,"male")
