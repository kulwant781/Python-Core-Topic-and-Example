def average(*number):

    sum = 0
    for i in number:
        sum = sum + i
        print(sum)
        avg = sum/len(number)
        return avg
    
chk =average(1,2,3,4,5)
print(chk)