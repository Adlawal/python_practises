#Convert the prices to float
prices =['$12.50' ,'$9.99' ,'$100.00']
print(list(map(lambda p: float(p.replace('$' , '')) ,prices)))

#price less than or equal to 100
prices = [120, 30, 300, 80]
print(list(filter(lambda p: p>=100 , prices)))


#students score higher than 70 -nested list
students=[['Maria', 85],['Kumar',90], ['Max',60]]
print(list(filter(lambda row: row[1] > 70 ,students)))

#students whose name starsts with M
students=[['Maria', 85],['Kumar',90], ['Max',60]]

print(list(filter(lambda row: row[0]. startswith('M'), students)))


