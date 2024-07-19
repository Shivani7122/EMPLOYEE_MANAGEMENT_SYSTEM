import pymysql as sql
import sys 
con=sql.connect(host="localhost",user="root",password="sql",database="emp",charset="utf8")
def insertRecord():
    id=int(input("Enter Employee Id:"))
    name=input("Enter Name:")
    gender=input("Enter gender :")
    email=input("Enter Email Id :")
    pswd=input("Enter Password :")
    date= input("Enter Date :")
    dept = input("Enter Department :")
    cur=con.cursor()
    # qry = "insert into empinfo values(%d,'%s','%s','%s','%s','%s','%s')"%(id,name,gender,email,pswd,date,dept)
    qry=f"insert into empinfo values({id},'{name}','{gender}','{email}','{pswd}','{date}','{dept}')"
    print(qry)
    cur.execute(qry)
    if cur.rowcount==1:
        print("Record Inserted Successfully .....!!")
    else:
        print("Error in inserting the record....!!")
    con.commit()

def deleteRecord():
    id=int(input("Enter Employee Id:"))
    qry=f"delete from empinfo where eid=(id)"
    cur= con.cursor()
    cur.execute(qry)
    con.commit()
    if cur.rowcount==1:
        print("Record deleted Successfully.....!!")
    else:
        print("Error in deleting the Record....!!")

def updateRecord():
    id=int(input("Enter Employee Id:"))
    cur= con.cursor()
    cur.execute(f"select * from empinfo where eid={id} ")
    if cur.rowcount==1:
        print("Press 1 to update name :")
        print("Press 2 to update gender :")
        print("Press 3 to update email id :")
        print("Press 4 to update password :")
        print("Press 5 to update joining date:")
        print("Press 6 to update department name :")
        print("Press 7 to go back to previous menu :")
        ch= int(input("Enter choice: "))
        if ch==1:
            name=input("Enter Name : ")
            qry = f"update empinfo set name='{name}'where eid={id}"
        elif ch==2:
            gender=input("Enter gender : ")
            qry = f"update empinfo set gender='{gender}'where eid={id}"
        elif ch==3:
            email=input("Enter email id : ")
            qry = f"update empinfo set email='{email}'where eid={id}"
        elif ch==4:
            pswd=input("Enter Password : ")
            qry = f"update empinfo set password='{pswd}'where eid={id}"
        elif ch==5:
            jdate=input("Enter joining date : ")
            qry = f"update empinfo set jdate='{jdate}'where eid={id}"
        elif ch==6:
            dept=input("Enter department Name : ")
            qry = f"update empinfo set department name='{dept}'where eid={id}"
        elif ch==7:
            pass
        else:
            pass
        if ch<7:
            cur.execute(qry)
            if cur.rowcount==1:
                print("Record updated successfully....!!")
            else:
                print("Error in updating the Record.........!!!!")
    else:
        print("Invalid employee id......!!")


def displayAllrecord():
    qry= 'Select * from empinfo'
    cur=con.cursor()
    cur.execute(qry)
    if cur.rowcount!=0:
        # print(cur.fetchone())
        # print(cur.fetchone())
        # print(cur.fetchone())       ----->> for one record
        # for i in cur.fetchmany(3):         ---->> for many records
        #     print(i)
        for i in cur.fetchall():
            print(i)
    else:
        print("No record Found...!!")
while True:
    print("Press 1 to insert")
    print("Press 2 to Update")
    print("Press 3 for deletion")
    print("Press 4 for Display All Records")
    print("Press 5 to Exit")
    choice = int(input("Enter Choice : "))
    if choice==1:
        insertRecord()
    elif choice==2:
        updateRecord()
    elif choice==3:
        deleteRecord()
    elif choice==4:
        displayAllrecord()
    elif choice==5:
        con.close()
        sys.exit()
    else:
        print("Invalid Choice........!!")

