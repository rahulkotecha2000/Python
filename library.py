import datetime as dt
def datentime():
    now=dt.datetime.today()
    aaj=now.strftime("%d-%b-%Y")
    return(aaj)
def timendate():
    now=dt.datetime.today()
    samay=now.strftime("%H:%M:%S")
    return (samay)

books=[["To Kill a Mockingbird","Harper Lee",4],["Harry Potter and the Philosopher\'s Stone","J.K. Rowling",5],["The Lord of the Rings","J.R.R. Tolkien",8],["The Great Gatsby","F.Robertson",6],["Pride and Prejudice","Jane Austen",4],["The Diary Of A Young Girl","Anne Frank",10],["C++","Devendra Goswami",12],["Core of Java","Dhruv Kotecha",5],["Python","Mrityunjay Kumar Panday",2]]

def bookissue():
    name=input("Enter the name of the book you want to borrow:")
    for i in books:
        if(name==i[0]):
            i[2]=i[2]-1
    return name

def bookreturn():
    name=input("Enter the name of the book you want to borrow:")
    for i in books:
        if(name==i[0]):
            i[2]=i[2]+1
    return name


while(True):
    print("\nWelcome to the National Library of India Directory records\n\n")
    
    print("Choose the function to be undertaken:\n")

    print("Code 1:Show books available")
    print("Code 2:Show the  records")
    print("Code 3:Add Library entry time")
    print("Code 4:Add Library exit time")
    print("Code 5:Book Issue entry")
    print("Code 6:Book Return entry")
    print("Code 7: Exit")

    c=int(input("Enter your function selection code:"))

    

    if (c==1):
        data=["\nTo Kill a Mockingbird by Harper Lee","Harry Potter and the Philosopher\'s Stone by J.K. Rowling","The Lord of the Rings by J.R.R. Tolkien","The Great Gatsby by F.Robertson","Pride and Prejudice by Jane Austen","The Diary Of A Young Girl by Anne Frank","C++","Core of Java","Python by Mrityunjay Kumar Panday"]
        for i in data:
            print(i)
    
    if(c==2):
        data=[]
        database=["Date","StudentID","Name","Surname","Book-Issued","Book-Returned","Penalty","Time","Status"]    
        
        file=open("pro2.txt","r")
        cont=file.readlines()
        file.close()
        if(len(cont)==0):
            data.append(database)
        for i in cont:
            if(i.isspace()):
                pass
            else:
                data.append(i.strip().split())
        file=open("pro2.txt","r")
        for nl in data:
            print(f"{nl[0]:{15}} {nl[1]:{10}} {nl[2]:{10}} {nl[3]:{10}} {nl[4]:{20}} {nl[5]:{20}} {nl[6]:{20}} {nl[7]:{20}} {nl[8]:{10}}\n")
        file.close()

        
    if(c==3):
        data=[]
        database=["Date","StudentID","Name","Surname","Book-Issued","Book-Returned","Penalty","Time","Status"]
        file=open("pro2.txt","r")
        cont=file.readlines()
        file.close()
        if(len(cont)==0):
            data.append(database)
        for i in cont:
            data.append(i.strip().split())
        def newentry():
            date=str(datentime())
            studentid=str(input("Enter the student library id:"))
            name=input("Enter the name:")
            surname=input("Enter the surname:")
            bookissued="NA"
            bookreturned="NA"
            penalty="NA"
            time=str(timendate())
            status="Check-in"
            return date,studentid,name,surname,bookissued,bookreturned,penalty,time,status
        newdata=list(newentry())
        data.append(newdata)
        file=open("pro2.txt","w")
        for nl in data:
            file.write(f"{nl[0]:{15}} {nl[1]:{10}} {nl[2]:{10}} {nl[3]:{10}} {nl[4]:{20}} {nl[5]:{20}} {nl[6]:{20}} {nl[7]:{20}} {nl[8]:{10}}\n")
        file.close()


    if(c==4):
        data=[]
        database=["Date","StudentID","Name","Surname","Book-Issued","Book-Returned","Penalty","Time","Status"]
        file=open("pro2.txt","r")
        cont=file.readlines()
        file.close()
        if(len(cont)==0):
            data.append(database)
        for i in cont:
            data.append(i.strip().split())
        def newentry():
            date=str(datentime())
            studentid=str(input("Enter the student library id:"))
            name=input("Enter the name:")
            surname=input("Enter the surname:")
            bookissued="NA"
            bookreturned="NA"
            penalty="NA"
            time=str(timendate())
            status="Check-out"
            return date,studentid,name,surname,bookissued,bookreturned,penalty,time,status
        newdata=list(newentry())
        data.append(newdata)
        file=open("pro2.txt","w")
        for nl in data:
            file.write(f"{nl[0]:{15}} {nl[1]:{10}} {nl[2]:{10}} {nl[3]:{10}} {nl[4]:{20}} {nl[5]:{20}} {nl[6]:{20}} {nl[7]:{20}} {nl[8]:{10}}\n")
        file.close()


    if(c==5):
        data=[]
        database=["Date","StudentID","Name","Surname","Book-Issued","Book-Returned","Penalty","Time","Status"]
        file=open("pro2.txt","r")
        cont=file.readlines()
        file.close()
        if(len(cont)==0):
            data.append(database)
        for i in cont:
            data.append(i.strip().split())
        def newentry():
            date=str(datentime())
            studentid=str(input("Enter the student library id:"))
            name=input("Enter the name:")
            surname=input("Enter the surname:")
            bookissued=bookissue()
            bookreturned="NA"
            penalty="NA"
            time=str(timendate())
            status="BookIssue"
            return date,studentid,name,surname,bookissued,bookreturned,penalty,time,status
        newdata=list(newentry())
        data.append(newdata)
        file=open("pro2.txt","w")
        for nl in data:
            file.write(f"{nl[0]:{15}} {nl[1]:{10}} {nl[2]:{10}} {nl[3]:{10}} {nl[4]:{20}} {nl[5]:{20}} {nl[6]:{20}} {nl[7]:{20}} {nl[8]:{10}}\n")
        file.close()


    if(c==6):
        data=[]
        database=["Date","StudentID","Name","Surname","Book-Issued","Book-Returned","Penalty","Time","Status"]
        file=open("pro2.txt","r")
        cont=file.readlines()
        file.close()
        if(len(cont)==0):
            data.append(database)
        for i in cont:
            data.append(i.strip().split())
        def newentry():
            date=str(datentime())
            studentid=str(input("Enter the student library id:"))
            name=input("Enter the name:")
            surname=input("Enter the surname:")
            bookissued="NA"
            bookreturned=bookreturn()
            penalty="NA"
            time=str(timendate())
            status="BookReturn"
            return date,studentid,name,surname,bookissued,bookreturned,penalty,time,status
        newdata=list(newentry())
        data.append(newdata)
        file=open("pro2.txt","w")
        for nl in data:
            file.write(f"{nl[0]:{15}} {nl[1]:{10}} {nl[2]:{10}} {nl[3]:{10}} {nl[4]:{20}} {nl[5]:{20}} {nl[6]:{20}} {nl[7]:{20}} {nl[8]:{10}}\n")
        file.close()

    if(c==7):
        break






























