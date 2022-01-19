import time

init_work_time = 25 * 60 #25 minutes
init_break_time = 5 * 60 #5 minutes
work_time = init_work_time
break_time = init_break_time

print("Pomodoro starts now!")
for i in range(4):
    #Work Session
    while work_time:
        break_time = init_break_time
        minutes = work_time // 60
        seconds = work_time % 60 
        timer = '{:02d}:{:02d}'.format(minutes,seconds)
        print(timer, end="\r")
        time.sleep(1)
        work_time -= 1
    print('Break time!!!')
    
    #Break Session
    while break_time:
        work_time = init_work_time
        minutes = break_time // 60
        seconds = break_time % 60 
        timer = '{:02d}:{:02d}'.format(minutes,seconds)
        print(timer, end="\r")
        time.sleep(1)
        break_time -= 1
    print('Work time!!!')

print('End of Pomodoro !!!')


