from cgitb import text
from curses import window
from tkinter import *
from tkinter import ttk
import math
import time

x = 5
yellow = "#f7f5dd"
reps = 0
work_time = 60

def count_down(count):
    global timer
    minutes = count // 60
    seconds = count % 60 
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    timer = window.after(1000, count_down, count -1)
def start_timer():
    global reps
    reps += 1
    count_down(work_time)

#Window
window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg=yellow)

#Tomato image
canvas = Canvas(width=400, height=400, bg=yellow, highlightthickness=0)
tomato_img = PhotoImage(file = "./pomodoro-clock/resources/tomato-image.png")
canvas.create_image(190, 190, image=tomato_img)

#Buttons
button_start = ttk.Button(text="Start") 
button_start.place(x = 100, y = 360)
button_restart = ttk.Button(text="Restart")
button_restart.place(x = 200, y = 360)

#timer
timer_text = canvas.create_text(200, 250, text = "00:00", fill = "white", font=("Courier", 50, "bold"))
canvas.grid(column=1, row=1)

start_timer()

window.mainloop()
