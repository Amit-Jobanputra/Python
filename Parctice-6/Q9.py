import re
a="Amit Sui gayo che and suvaa dyo ssss some"
b=re.findall(r'\bs\w{3}',a)
print(b)