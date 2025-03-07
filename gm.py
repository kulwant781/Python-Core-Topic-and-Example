import time

# Get the current timestamp
timestamp = time.time()
# print(timestamp)

# Convert timestamp to a human-readable string
current_time = time.localtime(timestamp)
# print(current_time)
hour = current_time.tm_hour
# print(hour)

# Print the timestamp and current time
# print(f"Timestamp: {timestamp}")
# print(f"Current Time: {time.strftime('%H:%M:%S', current_time)}")

# Determine the greeting based on the hour
if 5 <= hour < 12:
    print("Good Morning Everyone")
elif 12 <= hour < 17:
    print("Good Afternoon Everyone")
elif 17 <= hour < 21:
    print("Good Evening Everyone")
else:
    print("Good Night Everyone")
