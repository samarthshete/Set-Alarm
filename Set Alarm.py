import time
from pygame import mixer


def sound():
    mixer.init()
    mixer.music.load('analog-watch-alarm_daniel-simion.mp3')
def alarm():
    hr=int(input("Enter the hour:"))
    min=int(input("Enter the Min:"))
    sec=int(input("Enter the Sec:"))
    n=3
    print("Alarm Set for"+str(hr)+str(min))
    while True:
        if time.localtime().tm_hour==hr and time.localtime().tm_min==min and time.localtime().tm_sec==sec:
            print("Wake up")
            break
    sound()
    while n>0:
        mixer.music.play()
        time.sleep(2)

    sn=str(input("Press s for snooze"))
    if sn=='s':
        n=3
        time.sleep(100)
        while n>0:
            mixer,music.play()
            time.sleep()
    else:
        exit()

alarm()
