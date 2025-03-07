tup = (1,2,10,20,30,2,2)

news =  list(tup)
print(type(tup))
newtup = tuple(news)
chk = tup.index(10)
chk1 = len(tup)
chk2 = tup.count(2)

print(chk2)

news[2] = 100
print(type(news))
print(type(newtup))

print(tup[:])
print(tup[2:5])
print(tup[0:5])
print(len(tup))
print(tup[-4:-2]) #total of tuple len and negative value of index example 7-2 = 5 , 7-4 = 3

print(tup[1:2:5])

