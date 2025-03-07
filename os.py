import os

if not os.path.exists('test'):
    os.mkdir('test')
for i in range(0, 100):
    os.mkdir(f'test/day {i+1}')     #create a folder
    os.rename(f'test/tutorial {i+1}' ,f'test/checking {i+1}') #change the name of the folder
    print(f'test/checking {i+1}')
    folder = os.listdir('test')  #list the folder
    print(folder)

    for file in folder:
       print(file)
       print(os.path.join('test', file))

os.rmdir('test/checking 1')    #remove the folder