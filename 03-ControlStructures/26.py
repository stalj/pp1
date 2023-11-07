car_speed = int(input("Enter car speed: "))

speed_limit_min = 40
speed_limit_max = 140

if car_speed < speed_limit_min:
    print("You're driving too slow, slowpoke!")
elif car_speed > speed_limit_max:
    print("SLOW DOWN, YOU WHITE DEVIL! YOU'RE GONNA KILL US ALL!!")
else:
    print("...Whomever would've thought that giving you a driving licence wasn't such a bad idea.")
