from functools import lru_cache
import time

@lru_cache(maxsize = None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done the 20")

print(fx(5))
print("Done the 5")

print(fx(10))
print("Done the 10")


print(fx(20))
print("Done the 20")

print(fx(5))
print("Done the 5")

print(fx(10))
print("Done the 10")


print(fx(62))
print("Done the 62")


