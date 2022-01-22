from cgitb import text
from curses import window
from tkinter import *
from tkinter import ttk
import math
import time

x = 5
yellow = "#f7f5dd"


# time_input = 10
#Window
window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg=yellow)

#Tomato image
canvas = Canvas(width=400, height=400, bg=yellow, highlightthickness=0)
tomato_img = PhotoImage(file = "./pomodoro-clock/resources/tomato-image.png")
canvas.create_image(190, 190, image=tomato_img)

#timer
timer_text = canvas.create_text(200, 250, text = "00:00", fill = "white", font=("Courier", 50, "bold"))
canvas.grid(column=1, row=1)
min = 60
sec = 60
canvas.itemconfig(timer_text, text=f"{min}:{sec}")


#Buttons
button_start = ttk.Button(text="Start") 
button_start.place(x = 100, y = 360)
button_restart = ttk.Button(text="Restart")
button_restart.place(x = 200, y = 360)

# minutes = time_input // 60
# seconds = time_input % 60 
# timer = '{:02d}:{:02d}'.format(minutes,seconds)
# label = Label(window, text= timer)
# label.config(bg=yellow)
# label.pack()
# time.sleep(1)
# time_input -= 1

window.mainloop()