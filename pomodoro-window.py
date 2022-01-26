from cgitb import text
from curses import window
from tkinter import ttk, Tk, Canvas, PhotoImage
from tkinter import *


x = 5
yellow = "#f7f5dd"
reps = 0
work_time = 3
rest_time = 5
timer = NONE

# trasform the value in the timer 
def count_down(count):
    minutes = count // 60
    seconds = count % 60 
    timer_format = '{:02d}:{:02d}'.format(minutes,seconds)
    canvas.itemconfig(timer_text, text=f"{timer_format}")
   
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        count = 0
        
def restart_timer():
    global reps
    reps = 0
    count_down(0)
    
def start_timer():
    global reps
    reps += 1
    count_down(work_time)

#Create the interface Window 
window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg=yellow)

#Create and configure Tomato image
canvas = Canvas(width=400, height=400, bg=yellow, highlightthickness=0)
tomato_img = PhotoImage(file = "./pomodoro-clock/resources/tomato-image.png")
canvas.create_image(190, 190, image=tomato_img)

#Create and configure Buttons
start_button = ttk.Button(text="Start", command = start_timer) 
start_button.place(x = 100, y = 360)
restart_button = ttk.Button(text="Restart", command = restart_timer)
restart_button.place(x = 200, y = 360)

#Initial values for timer
timer_text = canvas.create_text(200, 250, text = "00:00", fill = "white", font=("Courier", 50, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
