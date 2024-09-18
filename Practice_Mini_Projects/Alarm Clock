from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1) #wait 1 second
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 #floor division
        seconds_left = time_left % 60 #modulo, remainder

        print(f"{CLEAR_AND_RETURN} Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    playsound("Alarm.mp3")
        
minutes = int(input("How many minutes would you like me to wait: "))
seconds = int(input("How many seconds would you like me to wait: "))
total_seconds = (minutes * 60) + seconds
alarm(total_seconds)


#Credits
# Project based on a tutorial by [Tech With Tim]
# YouTube channel: [https://www.youtube.com/@TechWithTim]
# Original video: [https://www.youtube.com/watch?v=no5dz0GOWy8]
