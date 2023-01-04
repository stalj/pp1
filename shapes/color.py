from datetime import datetime

now1 = datetime.now()
now2 = datetime.now()
time=now2-now1
current_time = now1.strftime("%H:%M:%S")
print("Current Time =", time)