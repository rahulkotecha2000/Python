class user():
    def __init__(self,fn,ln,age,gender,date,month,year):
        self.fn=fn.strip().title()
        self.ln=ln.strip().title()
        self.age=age
        self.gender=gender.strip().title()
        self.date=date
        self.month=month
        self.year=year
        self.dob=(f"{self.date}-{self.month}-{self.year}")

    def showdetails():
        print(f"""Full name: {self.fn} {self.ln}
Age: {self.age}
Gender: {self.gender}
Date of Birth: {self.dob}""")


class bank(user):
    bankuser=0
    __balance=0
    __pin=0
    
    import datetime as dt
    
    def __init__(self,fn,ln,age,gender,date,month,year):
        super().__init__(fn,ln,age,gender,date,month,year)
        bank.bankuser=bank.bankuser+1
        self.ac=bank.bankuser
        self.accountno=(f"bankaccountno1823537{self.ac}")
        self.pbk=[["Date","Time","Amount Debited/Credited","Balance"]]

    def viewdetails(self):
        print (f"""Full name: {self.fn} {self.ln}
Age: {self.age}
Gender: {self.gender}
Date of Birth: {self.dob}""")
        print(f"Your account number is {self.accountno}")
        print(f"Your Saving\'s Account balance is Rs.{self.__balance}")

    def deposit(self,depamt):
        import datetime as dt
        self.depamt=depamt
        self.__balance=self.__balance+self.depamt
        now=dt.datetime.today()
        aaj=now.strftime("%d-%b-%Y")
        samay=now.strftime("%H:%M:%S")
        self.x=[]
        self.x.append(aaj)
        self.x.append(samay)
        self.x.append(str(self.depamt))
        self.x.append(str(self.__balance))
        self.pbk.append(self.x)
        print("Thank you for using Bank Deposit Services!")
        print(f"Your account balance has been updated to Rs.{self.__balance}")

    def withdraw(self,withdrawamt):
        import datetime as dt
        self.withdrawamt=withdrawamt
        if(self.withdrawamt>self.__balance):
            print("Acoount balance Insufficient! Transaction Unsuccessful!")
        elif(self.withdrawamt>=10 and self.withdrawamt<=self.__balance):
            self.__balance=self.__balance-self.withdrawamt
            now=dt.datetime.today()
            aaj=now.strftime("%d-%b-%Y")
            samay=now.strftime("%H:%M:%S")
            self.y=[]
            self.y.append(aaj)
            self.y.append(samay)
            self.y.append(str(self.withdrawamt))
            self.y.append(str(self.__balance))
            self.pbk.append(self.y)
            print("Thank you for using Bank Withdrawal Services!")
            print(f"Your account balance has been updated to Rs.{self.__balance}")
        else:
            print("Transaction Unsuccessful! Please contact a Bank representative for further assistance.")

    def transfer(self,transferamt,username):
        import datetime as dt
        self.transferamt=transferamt
        if(self.transferamt>self.__balance):
            print("Acoount balance Insufficient! Transaction Unsuccessful!")
        elif((self.transferamt>=1) and (self.transferamt<=self.__balance)):
             self.__balance=self.__balance-self.transferamt
             username.__balance=username.__balance+self.transferamt
             now=dt.datetime.today()
             aaj=now.strftime("%d-%b-%Y")
             samay=now.strftime("%H:%M:%S")
             self.pbk.append([aaj,samay,str(self.transferamt),str(self.__balance)])
             username.pbk.append([aaj,samay,str(self.transferamt),str(username.__balance)])
             print("Thank you for using Bank Transfer Services!")
             print(f"Your account balance has been updated to Rs.{self.__balance}")
             

    def setpin(self):
        sett=int(input("Enter a new pin for your ATM:"))
        self.__pin=sett



    def ministat(self):
        for i in self.pbk:
            print(f"{i[0]:^15} {i[1]:^20} {i[2]:^30} {i[3]:^20}")

    def atm(self):
        xx=(input("Enter your Bank Account Number:"))
        yy=int(input("Enter your ATM Pin:"))
        if(xx==self.accountno and yy==self.__pin):
            while(True):
                print("Dear Customer,Welcome to XYZ Bank Automatic Tailor Machine:\n\n")
                print (f"""Full name: {self.fn} {self.ln}
Age: {self.age}
Gender: {self.gender}
Date of Birth: {self.dob}\n""")
                print("Choose the function to be undertaken:\n")
                print("Code 1: Balance Inquiry")
                print("Code 2: Deposit")
                print("Code 3: Withdrawal")
                print("Code 4: Change Card Settings")
                print("Code 5:Exit")

                c=int(input("Enter the code of the function to be executed:"))

                if(c==1):
                    print(f"{self.viewdetails()}\n")
                if(c==2):
                    l=int(input("Enter the amount to be deposited:"))
                    print(self.deposit(l))
                if(c==3):
                    k=int(input("Enter the amount to be deposited:"))
                    print(self.withdraw(k))
                if(c==4):
                    self.setpin()
                    print("Thank you for using ATM Card Pin updation services! For any queries contact our e-Customer Helpline Executive on 1800-111-010101")
                    
                if(c==5):
                    break
            
        



user1=bank("rahul","kotecha",21,"male",28,10,2000)
user2=bank("rushabh","kotecha",24,"male",25,9,1998)

