# F = open('mytext.txt','r')

F = open('mytext.txt','w')
data = F.write("I love pyhton langauge")
F.truncate(5)
# F.seek(10)
# print(F.tell())
# data = F.read(3)
print(data)

# seel_tell_truncate.py