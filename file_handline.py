# reading this code txt file

# f = open('mytext.file','r')
# text = f.read()
# print(text)
# f.close()

# creating a txt file

# f = open('mytext2.file','w')
# f.write('Hello, I am Kulwant')
# f.close()

# appending a txt file
# f = open('mytext2.file','a')
# f.write('This is a good python Developer')
# f.close()

# with using the with statement

# with open('mytext2.file','a') as f: 
    
#     f.write("\n file handling is very important in python")


# reading a file line by line
# f= open('mytext2.file','r')
# while True:
#     line = f.readline()
#     if not line:
#         break

#     print(line)
# f.close()

#writing multiple line in a file
f = open('multipleline.file','w')
line = ['Hello, I am Kulwant', 'I am a good python developer']

for lines in line:
    f.writelines(lines + '\n')

f.close()



# reading a file line by line
f= open('mytext2.file','r')
i =0 
while True:
    i += 1
    line = f.readline()
    if not line:
        break
   
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])
    print(f"student marks are show {i} in english: {m1*2}")

    print(f"student marks are show {i} in hindi: {m2*2}")
    
    print(f"student marks are show {i} in math: {m3*2}")
f.close()