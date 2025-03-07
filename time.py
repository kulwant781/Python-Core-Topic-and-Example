import time
current_time = time.ctime()

print(f"please show the time we{current_time}")

for i in range(4):
    time.sleep(5)
    print(i)