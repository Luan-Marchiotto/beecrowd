from datetime import datetime

data_str = input().strip()

data_obj = datetime.strptime(data_str, '%d/%m/%y')

formato1 = data_obj.strftime('%m/%d/%y')  # MM/DD/AA
formato2 = data_obj.strftime('%y/%m/%d')  # AA/MM/DD
formato3 = data_obj.strftime('%d-%m-%y')  # DD-MM-AA

print(formato1)
print(formato2)
print(formato3)