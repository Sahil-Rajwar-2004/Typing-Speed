'''
~About Me:
    Hello World!
    Creator: Sahil Rajwar Of Class 12th-A Science Student.
    Date: Thursday, 14/Oct/2021

'''

# Import Libraries
from tkinter import *
import random
from tkinter import messagebox
from time import ctime
import time

# Introduction When Application Starts
print('~About Me')
print('Hello World!')
print('Creator: Sahil Rajwar Of Class 12th-A Science Student.')
print('Date: Thursday 14/Oct/2021')
print("************************************************************")

try:
    name = input('Enter Your Name: ')
    print(name)
except KeyboardInterrupt as e:
    print(f'Unknown {e}')

# Main Window
win = Tk()
win.geometry('550x400')
win.title('Speed Typing')
win.iconbitmap(r'<provide the path of Typing_Logo.ico>')
win.resizable(0,0)

# Back END
c_time = ctime()
counter = 60
correct = 0
incorrect = 0

# Set the Record in 
def set_record():
    global correct, incorrect, name
    total = correct + incorrect
    result = round((correct/total)*100,3)
    record = open('record_ts.txt','a')
    record.write('******************************\n')
    record.write(f'Done by {name} at {c_time}\n')
    record.write(f'Miss: {incorrect}\n')
    record.write(f'Correct: {correct}\n')
    record.write(f'Result: {result}% Accuracy\n')
    record.write('******************************\n')
    record.close()

def compare():
    global correct, name
    if correct >= 30:
        print('Good Enough')
    elif correct >= 20:
        print(f'You are Slow! {name} Keep Improving')
    else:
        print(f'Too Slow! {name} Need Improving')

with open("<provide the path of words.txt>", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
word = random.choice(words)

# Reset Function to Reset the Score Board and counter
def reset(event):
    global correct, incorrect, counter
    entry.delete(0,END)
    correct = 0
    incorrect = 0
    counter = 60
    display_time.configure(text = counter)
    result1_label.configure(text = correct)
    result2_label.configure(text = incorrect)
    print('Will Start In 5 sec be ready!')
    time.sleep(5)

# Exit Fuction to exit/quit the game
def Exit(event):
    global correct, incorrect
    print(f'Correct: {correct}')
    print(f'Incorrect: {incorrect}')
    win.destroy()

# Set the Countdown/Timer of 60-secs/1-Min only
def timer():
    global counter, correct, incorrect
    if counter >= 40:
        display_time.configure(fg = 'green')
    elif counter >= 20:
        display_time.configure(fg = 'orange')
    else:
        display_time.configure(fg = 'red')
    if counter > 0:
        counter -= 1
        display_time.config(text = counter)
        display_time.after(1000,timer)
    else:
        req = messagebox.askretrycancel('Note','Do You Want To Play Again?')
        if req == True:
            try:
                total = correct + incorrect
                result = (correct/total)*100
                print(f'{round(result,3)}% Accuracy')
            except ZeroDivisionError:
                print(f'{0}% Accuracy')
            word = random.choice(words)
            set_record()
            compare()
            print('Restarting Again...')
            time.sleep(3)
            display_label.configure(text = word)
            correct = 0
            incorrect = 0
            result1_label.configure(text = correct)
            result2_label.configure(text = incorrect)
            counter = 60
            display_time.config(text = counter)
        else:
            print(f'Correct: {correct}')
            print(f'Incorrect: {incorrect}')
            # print(f'Your Score: {}')
            try:
                total = correct + incorrect
                result = (correct/total)*100
                print(f'{round(result,3)}% Accuracy')
            except ZeroDivisionError:
                print(f'{0}% Accuracy')
            set_record()
            compare()
            print('We hope you like this :)')
            time.sleep(3)
            win.destroy()

# Check Function for Handle the main Task e.g -> varifing spellings, Increasing/Decreaseing the Scores, etc

def check(event):
    global correct, incorrect, word, counter
    # timer()
    if counter == 60:
        timer()
    if entry.get() == display_label['text']:
        print('Correct')
        correct += 1
        result1_label.configure(text = correct)
    else:
        print('Incorrect')
        incorrect += 1
        result2_label.configure(text = incorrect)
        print(f'Its {word} and you typed {entry.get()}')
    entry.delete(0,END)
    word = random.choice(words)
    display_label.configure(text = word)

# Main Frame
heading_frame = Frame(win, relief = GROOVE, bd = 5, bg = 'grey')
heading_frame.pack(fill = BOTH, padx = 10, pady = 5)
heading_label = Label(heading_frame, font = ('Cascadia code',16), text = 'Typing Speed')
heading_label.pack(fill = BOTH)

# Creating Main Display/Board
main_frame = Frame(win, relief = GROOVE, bd = 5, bg = 'grey')
main_frame.pack(fill = BOTH, padx = 10)
display_label = Label(main_frame, text = '', font = ('Cascadia code',18), bg = 'grey', fg = 'white')
display_label.pack(fill = BOTH, padx = 4, pady = 5)
display_label.config(text = word)

# Creating Timer Board
timer_frame = Frame(win, relief = GROOVE, bd = 5)
timer_frame.pack(fill = BOTH, padx = 10, pady = 5)
timer_label = Label(timer_frame, text = 'Time Left =', font = ('Cascadia code',14))
timer_label.grid(row = 0, column = 0)
display_time = Label(timer_frame, text = counter, font = ('Cascadia code',14), fg = 'dark green')
display_time.grid(row = 0, column = 1)

# Creating Score Board
score_frame = Frame(win, relief = GROOVE, bd = 5)
score_frame.pack(fill = BOTH, padx = 10, pady = 5)
score1_label = Label(score_frame, text = 'Correct =', font = ('Cascadia code',14))
score1_label.grid(row = 0, column = 0)
result1_label = Label(score_frame, text = '0', font = ('Cascadia code',14))
result1_label.grid(row = 0, column = 1)
score1_label = Label(score_frame, text = 'Miss =', font = ('Cascadia code',14))
score1_label.grid(row = 1, column = 0)
result2_label = Label(score_frame, text = '0', font = ('Cascadia code',14))
result2_label.grid(row = 1, column = 1)

# Creating Notice Board
note_frame = Frame(win, relief = GROOVE, bd = 5)
note_frame.pack(fill = BOTH, padx = 10, pady = 5)
note_label = Label(note_frame, text = 'Hit Enter to jump to the New Word\nHit Escape Button to Quit the Game\nHit the Delete Button to reset the Game Score', font = ('Cascadia code',13))
note_label.pack()

# Creating An Entry-BOX
entry = Entry(main_frame, font = ('Cascadia code',16), justify = 'center')
entry.pack(fill = BOTH, padx = 4, pady = 5)
entry.focus_set()

# Keyboard Binding
win.bind('<Return>', check) # --> Press return/enter button on the keyboard to pass the value
win.bind('<Escape>', Exit)  # --> Press Escape button on keyboard to exit/quit the game
win.bind('<Delete>', reset) # --> Press Delete button on keyboard to reset/restart the game

win.mainloop()
