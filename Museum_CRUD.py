#Project CRUD
while(True):
    print("\nWelcome to the Nelson Mandela Museum Visitlog:\n\n")
    print("Choose the function to be undertaken:\n")

    print("Code 1:Read the monthly visitlog")
    print("Code 2:Add/Append the monthly visitlog")
    print("Code 3:Update the monthly visitlog")
    print("Code 4:Remove from the monthly visitlog")
    print("Code 5:Insert in the monthly visitlog")
    print("Code 6:Exit\n\n")

    c=int(input("Enter your function selection code:"))

    if(c==1):
        data=[]
        database=["Date","Name","Surname","In","Out","Baggage"]    
        
        file=open("pro1.txt","r")
        cont=file.readlines()
        file.close()
        if(len(cont)==0):
            data.append(database)
        for i in cont:
            if(i.isspace()):
                pass
            else:
                data.append(i.strip().split())
        file=open("pro1.txt","r")
        for nl in data:
            print(f"{nl[0]:^3} {nl[1]:^10} {nl[2]:^10} {nl[3]:^5} {nl[4]:^5} {nl[5]:^3}")
        file.close()

    if(c==2):
        data=[]
        database=["Date","Name","Surname","In","Out","Baggage"]
        file=open("pro1.txt","r")
        cont=file.readlines()
        file.close()
        if(len(cont)==0):
            data.append(database)
        for i in cont:
            data.append(i.strip().split())
        def newentry():
            date=str(int(input("Enter the date of entry:")))
            name=input("Enter the name:")
            surname=input("Enter the surname:")
            intime=str(input("Enter the entry-in time:"))
            outtime=str(input("Enter the entry-out time:"))
            baggage=str(input("Enter the check-in baggage:"))
            return date,name,surname,intime,outtime,baggage
        newdata=list(newentry())
        data.append(newdata)
        file=open("pro1.txt","w")
        for nl in data:
            file.write(f"{nl[0]:{3}} {nl[1]:{10}} {nl[2]:{10}} {nl[3]:{5}} {nl[4]:{5}} {nl[5]:{3}}\n")
        file.close()
        
    if(c==3):
        data=[]
        database=["Date","Name","Surname","In","Out","Baggage"]
        file=open("pro1.txt","r")
        cont=file.readlines()
        file.close()
        
        if(len(cont)==0):
            data.append(database)
            
        pp=int(input("Enter the index number of the entry to be updated:"))
        
        for i in cont:
            data.append(i.strip().split())
            
        data.pop(pp)
        def newentry():
            date=str(int(input("Enter the date of entry:")))
            name=input("Enter the name:")
            surname=input("Enter the surname:")
            intime=str(int(input("Enter the entry-in time:")))
            outtime=str(int(input("Enter the entry-out time:")))
            baggage=str(int(input("Enter the check-in baggage:")))
            return date,name,surname,intime,outtime,baggage
        
        date,name,surname,intime,outtime,baggage=newentry()
        newdata=[date,name,surname,intime,outtime,baggage]
        data.insert(pp, newdata)
        
        file=open("pro1.txt","w")
        
        for nl in data:
            file.write(f"{nl[0]:{3}} {nl[1]:{10}} {nl[2]:{10}} {nl[3]:{5}} {nl[4]:{5}} {nl[5]:{3}}\n")
        file.close()

    if(c==4):
        data=[]
        database=["Date","Name","Surname","In","Out","Baggage"]
        file=open("pro1.txt","r")
        cont=file.readlines()
        file.close()
        
        if(len(cont)==0):
            data.append(database)
            
        pp=int(input("Enter the index number of the entry to be updated:"))
        
        for i in cont:
            data.append(i.strip().split())
        data.pop(pp)
        file=open("pro1.txt","w")
        
        for nl in data:
            file.write(f"{nl[0]:{3}} {nl[1]:{10}} {nl[2]:{10}} {nl[3]:{5}} {nl[4]:{5}} {nl[5]:{3}}\n")
        file.close()

    if(c==5):
        data=[]
        database=["Date","Name","Surname","In","Out","Baggage"]
        file=open("pro1.txt","r")
        cont=file.readlines()
        file.close()
        
        if(len(cont)==0):
            data.append(database)
            
        pp=int(input("Enter the index number of the entry to be updated:"))
        
        for i in cont:
            data.append(i.strip().split())
            
        def newentry():
            date=str(int(input("Enter the date of entry:")))
            name=input("Enter the name:")
            surname=input("Enter the surname:")
            intime=str(int(input("Enter the entry-in time:")))
            outtime=str(int(input("Enter the entry-out time:")))
            baggage=str(int(input("Enter the check-in baggage:")))
            return date,name,surname,intime,outtime,baggage
        
        date,name,surname,intime,outtime,baggage=newentry()
        newdata=[date,name,surname,intime,outtime,baggage]
        data.insert(pp, newdata)
        
        file=open("pro1.txt","w")
        
        for nl in data:
            file.write(f"{nl[0]:{3}} {nl[1]:{10}} {nl[2]:{10}} {nl[3]:{5}} {nl[4]:{5}} {nl[5]:{3}}\n")
        file.close()
            
    
    if(c==6):
        break

















        
        

    

