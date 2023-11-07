time_24 = input("Enter time (in the objectively correct 24-h format): ")
time_24_hour = int(time_24[0:2])
time_24_minutes = int(time_24[3:5])

if time_24_hour > 12:
    time_12 = f"{time_24_hour - 12}:{time_24_minutes}"
else:
    time_12 = time_24

print(f"Time in the objectively inferior 12-h format: {time_12}pm")