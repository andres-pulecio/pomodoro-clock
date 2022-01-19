import time

time_input = int(input("How many seconds do you want to set the timer for?\n"))

while time_input:
    minutes = time_input // 60
    seconds = time_input % 60 
    timer = '{:02d}:{:02d}'.format(minutes,seconds)
    print(timer, end="\r")
    time.sleep(1)
    time_input -= 1
print('Blast off!!!')