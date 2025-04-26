import sqlite3
con= sqlite3.connect('data.dp')

#Creating Table
# con.execute("Create Table stud(Enr integer ,Name Varchar)")


#inserting Record 
# con.execute('''
#         insert into stud values 
#         (1,"Amit"),
#         (2,"Dev")
#         ''')
# con.commit()

#display All Record
data=con.execute('select * from stud')
for i in data:
    print(i)

#display record of selected record
# data=con.execute('select * from stud where Enr=1')
# for i in data:
#     print(i)

#Updating Record
# update="update stud set Name ='DEV' where Enr=2"
# con.execute(update)
# con.commit()

#Delete selected record
# con.execute("Delete from stud where Enr=2")
# con.commit()

#Delete All Record
con.execute('Delete from stud')
con.commit()