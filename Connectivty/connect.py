import mysql.connector
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password=''
# )
# print(mydb)
# mycursor =mydb.cursor()
# mycursor.execute('Create Database python')
# mycursor.execute('Show Databases')
# for i in mycursor:
#     print(i)

#Creating The Table
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python'
)
mycursor=mydb.cursor()
# mycursor.execute('Create table stud(Enroll int ,Name varchar(20))')
# mycursor.execute('show tables')
# for i in mycursor:
#     print(i)


#Inserting Records
# insert='insert into stud(Enroll,Name) values(%s,%s)'
# records=[(1,"Amit"),(2,"Dev"),(3,'Rohan')]
# mycursor.executemany(insert,records)
# mydb.commit()
# mydb.close()
# mycursor.close()
# print("Records Are inserted")

#Displaying All the Records
mycursor=mydb.cursor()
mycursor.execute("Select * from stud")
result=mycursor.fetchall()
for i in result:
    print(i)