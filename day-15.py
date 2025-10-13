import time

timestamp = time.strftime('%I:%M:%S %p')
hours = int (time.strftime('%H'))

# print formate time
print("====================================")
print(f"        Current Time: {timestamp}")
print("====================================")

# Greeting message based on time

if 5<=hours <12:
    print("Good Morning! ")
elif 12<=hours <17:
    print("Good Afternoon! ")
elif 17<= hours <21:
    print("Good Evening! ")

else:
    print("Good Night! ")

print("======================================")

