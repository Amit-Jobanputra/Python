no_subs=int(input("How many Subject You Want :- "))
with open('marks.bat','w')as file:
    for i in range(no_subs):
        sub=input("Enter Your Subject Name :-")
        mark=int(input("Enter Your Subject Marks :-"))
        file.write(f"{sub} and {mark}")