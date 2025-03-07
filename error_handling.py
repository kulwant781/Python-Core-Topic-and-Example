def error_handling():

    try:
        l = [1,4,5,6]
        i = int(input("enter a valid index"))
        print (l[i])
        return 1

    except:
        print ("index out of range")
        return 0
    finally:
        print ("this will always execute")

# print ("this will always execute")    

x = error_handling()
print(x)