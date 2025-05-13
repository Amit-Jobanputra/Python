import pandas  as pd
import matplotlib.pyplot as plt
# df=pd.read_csv('sample_records.csv')
# print(df)
# df=pd.read_excel('sample_records.xlsx')
a={'roll':[100,201,302],'name':["dev","Amit",'Nimesh']}
x=a['name']
y=a['roll']
plt.bar(x,y)
plt.xlabel('Name of Student')
plt.ylabel('Marks of Student')
plt.title('Marks Details')
plt.show()