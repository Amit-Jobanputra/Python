import pandas as pd
# df=pd.read_csv('sample_records.csv')
# print(df)
# df=pd.read_excel('sample_records.xlsx')
# print(df)
people = [
    ("Alice Johnson", 30, "New York", "Software Engineer", 75000),
    ("Bob Smith", 28, "Los Angeles", "Data Analyst", 68000),
    ("Charlie Lee", 35, "Chicago", "Project Manager", 82000),
    ("Diana Prince", 32, "Houston", "UX Designer", 70000),
    ("Ethan Brown", 27, "Phoenix", "DevOps Engineer", 77000)
]
df=pd.DataFrame(people)
print(df)