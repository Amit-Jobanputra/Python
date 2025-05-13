with open('simple.txt','wb') as file:
    subs=["react","laravel","Java","python"]
    for sub in subs:
        file.write((sub + '\n').encode())
sub_no=int(input("Please Enter The Subject Number Which You Want to see :-"))
with open('simple.txt','rb') as file :
     line = file.readlines()
print((line[sub_no]).decode())