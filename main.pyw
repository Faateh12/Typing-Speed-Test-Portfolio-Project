from tkinter import *
from tkinter import ttk
from test import Sentence
import os

window = Tk()
window.title("Typing Speed Test")
window.geometry("800x600")
window["background"] = "#FBC5C5"

s = Sentence()
words = s.show()
counter = 60

def restart():
    window.destroy()
    os.startfile("main.pyw")

def countdown():
    entry_box.configure(state="normal")
    global counter, Score
    if counter > 0:
        mins, secs = divmod(counter, 60)
        counter -= 1
        counter_label.configure(text='{:02d}:{:02d}'.format(mins, secs))
        counter_label.after(1000, countdown)
    elif counter == 0:
        entry_box.delete(0, END)
        entry_box.configure(state="disabled")
        counter_label.configure(text="Time is Over!")
        wpm_label.configure(text=f"Your WPM is {Score}")

def go(event):
    while True:
        global index, Score
        try:
            if entry_box.get() == words[index]:
                index += 1
                Score += 1
                entry_box.delete(0, END)
                label.configure(text=words[index])
                # score_label.configure(text=f"Score:{Score}")
                break
            elif entry_box.get() != words[index]:
                index = index
                Score = Score
                entry_box.delete(0, END)
                label.configure(text=words[index])
                # score_label.configure(text=f"Score:{Score}")
                break
        except IndexError:
            label.configure(text="Congrats!")
            break

index = 0
Score = 0

main_label = ttk.Label(window, text="Faateh's Typing Speed Test", font=("Times", 30, "italic"), background=[("#FBC5C5")])
main_label.pack(pady=10)

counter_label = ttk.Label(window, text="Time", font=("Cambria", 22), background=[("#FBC5C5")])
counter_label.pack(pady=40)


label = ttk.Label(window, text=words[index], font=("Times", 25, "bold"), background=[("#FBC5C5")])
label.pack()

entry_box = ttk.Entry(window, state="disabled")
entry_box.pack(pady=10, ipady=3, ipadx=3)

wpm_label = ttk.Label(window, text="WPM", font=("Times", 14), background=[("#FBC5C5")])
wpm_label.pack()

# score_label = Label(window, text=f"Score:{Score}", font=("Helvetica", 14), bg="#FBC5C5")
# score_label.grid(row=5, column=0)
s = ttk.Style()
s.configure('my.TButton', font=('Cambria', 11, "bold"))

start_timer_button = ttk.Button(window, text="Start Test", command=countdown, style='my.TButton')
start_timer_button.pack(side=LEFT, padx=100, ipadx=10, ipady=10)

window.bind("<Return>", go)

restart_button = ttk.Button(window, text="Play Again", command=restart, style='my.TButton')
restart_button.pack(side=RIGHT, padx=100, ipadx=10, ipady=10)





window.mainloop()


