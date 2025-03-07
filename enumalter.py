
# simple function using the for loop

# marks = [10,30,50,70,90]

# index = 0
# for mark in marks:
#     print(mark)

#     if index == 3:
#         print("The index is 3")
#     index += 1


# The above code can be written using the enumerate function
marks = [10,30,50,70,90]

for index,mark in enumerate(marks, start=1):
    print(mark)

    if index == 3:
        print("The index is 3 runing code done")
