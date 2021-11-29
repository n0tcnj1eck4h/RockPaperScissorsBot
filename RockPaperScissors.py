import tkinter as tk
from tkinter import *
import os

root = tk.Tk()
root.title('')
root.geometry('215x355')
root.resizable(False, False)

canvas = tk.Canvas(root, bg='lavenderblush', width=215, height=355)
canvas.pack()

label = tk.Label(root, text='Rock, paper, scissors!', bg='lavenderblush', justify=LEFT)
label.config(font=('arial', 14, 'bold'))
canvas.create_window(105, 15, window=label)

img_dir = os.path.join(os.getcwd(), 'Data')

empty_img = PhotoImage(file=(os.path.join(img_dir, 'empty.png')))
rock_img = PhotoImage(file=(os.path.join(img_dir, 'rock.png')))
paper_img = PhotoImage(file=(os.path.join(img_dir, 'paper.png')))
scissors_img = PhotoImage(file=(os.path.join(img_dir, 'scissors.png')))

print('img_dir', img_dir)
print('rock_img', rock_img)

movehistory = ['1', '2', '3']
counterhistory = ['1', '2', '3']


def display_result():
    if counter_throw == 1:
        label3['image'] = rock_img
        counterhistory.append('Rock')
    elif counter_throw == 2:
        label3['image'] = paper_img
        counterhistory.append('Paper')
    else:
        label3['image'] = scissors_img
        counterhistory.append('Scissors')


def check_result():
    import random
    global counter_throw

    r = random.randint(1, 100)

    if r < 80:
        last0 = movehistory[-1]
        last1 = movehistory[-2]
        last2 = movehistory[-3]

        counter0 = counterhistory[-1]

        if last0 == last1 == last2:
            if last0 == 'Rock':
                counter_throw = 2
            elif last0 == 'Paper':
                counter_throw = 3
            else:
                counter_throw = 1
        elif last0 == 'Rock':
            if counter0 == 'Paper':
                counter_throw = 1
        elif last0 == 'Paper':
            if counter0 == 'Scissors':
                counter_throw = 2
        elif last0 == 'Scissors':
            if counter0 == 'Rock':
                counter_throw = 3
        else:
            if last0 == 'Rock':
                counter_throw = 2
            elif last0 == 'Paper':
                counter_throw = 3
            else:
                counter_throw = 1

    else:
        counter_throw = random.randint(1, 3)

    display_result()


throw = 0
wins = 0
losses = 0


def throw_rock():
    print('Rock!')
    global throw
    throw = 1
    check_result()
    if counter_throw == 1:   # it's a tie
        label2['text'] = 'Tied!'
        print("Tied!")
    elif counter_throw == 2:  # it's a lose
        label2['text'] = 'You lost!'
        print('lost')
        global losses
        losses = losses + 1
        print(f'Losses:{losses}')
        labellosses['text'] = f'Lost:{losses}'
    else:
        label2['text'] = 'You won!'
        print('won')
        global wins
        wins = wins + 1
        print(f'Wins:{wins}')
        labelwins['text'] = f'Won:{wins}'

    movehistory.append('Rock')


def throw_paper():
    print('Paper!')
    global throw
    throw = 2
    check_result()
    if counter_throw == 2:  # it's a tie
        label2['text'] = 'Tied!'
        print("Tied!")
    elif counter_throw == 3:  # it's a lose
        label2['text'] = 'You lost!'
        print('lost')
        global losses
        losses = losses + 1
        print(f'Losses:{losses}')
        labellosses['text'] = f'Lost:{losses}'
    else:
        label2['text'] = 'You won!'
        print('won')
        global wins
        wins = wins + 1
        print(f'Wins:{wins}')
        labelwins['text'] = f'Won:{wins}'

    movehistory.append('Paper')


def throw_scissors():
    print('Scissors!')
    global throw
    throw = 3
    check_result()
    if counter_throw == 3:  # it's a tie
        label2['text'] = 'Tied!'
        print("Tied!")
    elif counter_throw == 1:  # it's a lose
        label2['text'] = 'You lost!'
        print('lost')
        global losses
        losses = losses + 1
        print(f'Losses:{losses}')
        labellosses['text'] = f'Lost:{losses}'
    else:
        label2['text'] = 'You won!'
        print('won')
        global wins
        wins = wins + 1
        print(f'Wins:{wins}')
        labelwins['text'] = f'Won:{wins}'

    movehistory.append('Scissors')


button_rock = tk.Button(canvas, text='Rock!', command=throw_rock, width=7, height=2, bg='pink', fg='black',
                        activebackground='black', activeforeground='pink')
button_rock.config(font=('arial', 10, 'bold'))
canvas.create_window(40, 55, window=button_rock)

button_paper = tk.Button(canvas, text='Paper!', command=throw_paper, width=7, height=2, bg='pink', fg='black',
                         activebackground='black', activeforeground='pink')
button_paper.config(font=('arial', 10, 'bold'))
canvas.create_window(105, 55, window=button_paper)

button_scissors = tk.Button(canvas, text='Scissors!', command=throw_scissors, width=7, height=2, bg='pink', fg='black',
                            activebackground='black', activeforeground='pink')
button_scissors.config(font=('arial', 10, 'bold'))
canvas.create_window(170, 55, window=button_scissors)

label3 = tk.Label(root, image=empty_img, bg='lavenderblush')
canvas.create_window(110, 200, window=label3)

label2 = tk.Label(root, text='Throw these hands!', bg='lavenderblush')
label2.config(font=('arial', 14, 'bold'))
canvas.create_window(110, 315, window=label2)

labelwins = tk.Label(root, text=f'Won:{wins}', bg='lavenderblush')
labelwins.config(font=('arial', 14, 'bold'))
canvas.create_window(170, 340, window=labelwins)

labellosses = tk.Label(root, text=f'Lost:{losses}', bg='lavenderblush')
labellosses.config(font=('arial', 14, 'bold'))
canvas.create_window(50, 340, window=labellosses)


def exitbtn():
    root.destroy()
    import subprocess
    subprocess.call("Menu.py", shell=True)


exitbt = tk.Button(root, text='Back', command=exitbtn, font=('arial', 8), bg='pink', fg='black')
canvas.create_window(110, 340, window=exitbt)

root.mainloop()
