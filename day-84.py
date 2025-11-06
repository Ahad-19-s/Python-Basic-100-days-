import time
import time
print(time.time())
# 👉 মানে হচ্ছে human-readable date & time।
print(time.ctime())  

# 🕐 1️⃣ time module কী?

# time হলো Python-এর built-in module যা সময় ও তার সঙ্গে সম্পর্কিত ফাংশন দেয়।
# এটার মাধ্যমে তুমি —

# বর্তমান সময় পেতে পারো,

# কোডের execution সময় মাপতে পারো,

# sleep (pause/delay) দিতে পারো,

# timestamp (epoch time) নিয়ে কাজ করতে পারো।
import time

print("Start")
time.sleep(10)   # 3 সেকেন্ডের জন্য থামবে
print("End after 10 seconds")
import time

start = time.time()

# কিছু কাজ (যেমন loop)
for i in range(1000000):
    pass

end = time.time()
print("Execution time:", end - start, "seconds")
