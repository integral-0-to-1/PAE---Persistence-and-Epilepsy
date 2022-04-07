import tkinter as tk
from random import choice
from datetime import datetime

count = 1000
temp = 0
after_id = ''
start_game = True


def random_color():
    colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    pre_color = []
    for j in range(6):
        pre_color.append(choice(colors))
    color = '#' + ''.join(pre_color)
    return color


def start_timer():
    global temp, after_id
    after_id = win.after(1000, start_timer)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    timer['text'] = f_temp
    temp += 1


def counter():
    global count, start_game
    if start_game:
        start_timer()
        start_game = False
    count -= 1
    if count > 0:
        return buttons_disabled()
    return finish(), win.after_cancel(after_id)


def buttons_disabled():
    buttons = [btn1, btn2, btn3, btn4]
    for i in buttons:
        i['state'] = tk.DISABLED
        i['bg'] = random_color()
    return push()


def push():
    buttons = [btn1, btn2, btn3, btn4]
    push_button = choice(buttons)
    timer['bg'] = random_color()
    win.config(bg=timer['bg'])

    push_button['state'] = tk.NORMAL
    push_button['bg'] = '#e6e6e6'
    push_button['text'] = f'Need to press: {count}'

    if push_button == btn1:
        btn2['text'] = '🠔'
        btn3['text'] = '🠕'
        btn4['text'] = '⤣'
    elif push_button == btn2:
        btn1['text'] = '🠖'
        btn3['text'] = '⤤'
        btn4['text'] = '🠕'
    elif push_button == btn3:
        btn1['text'] = '🠗'
        btn2['text'] = '⤦'
        btn4['text'] = '🠔'
    elif push_button == btn4:
        btn1['text'] = '⤥'
        btn2['text'] = '🠗'
        btn3['text'] = '🠖'
    else:
        win.destroy()

    return


def finish():
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()

    button_quit = tk.Button(win,
                            text='Click to Quit',
                            fg='blue',
                            bg='#bebebe',
                            font=('Times New Roman', 16, 'bold'),
                            command=win.destroy
                            )

    label = tk.Label(win,
                     text='You win!',
                     fg='red',
                     bg='white',
                     font=('Times New Roman', 50, 'bold'),
                     height=13,
                     width=15
                     )

    timer['fg'] = 'blue'
    timer['bg'] = '#bebebe'
    win.config(bg='white')
    button_quit.grid(row=0, columnspan=2, sticky='n', stick='we')
    label.grid(row=1, columnspan=2)
    timer.grid(row=2, columnspan=2)


win = tk.Tk()

btn1 = tk.Button(win,
                 text=f'Need to press: {count}',
                 widt=15,
                 height=3,
                 font=('Times New Roman', 18, 'bold'),
                 state=tk.NORMAL,
                 relief=tk.RAISED,
                 bd=10,
                 command=counter
                 )

btn2 = tk.Button(win,
                 text=f'Need to press: {count}',
                 widt=15,
                 height=3,
                 font=('Times New Roman', 18, 'bold'),
                 state=tk.NORMAL,
                 relief=tk.RAISED,
                 bd=10,
                 command=counter
                 )

btn3 = tk.Button(win,
                 text=f'Need to press: {count}',
                 widt=15,
                 height=3,
                 font=('Times New Roman', 18, 'bold'),
                 state=tk.NORMAL,
                 relief=tk.RAISED,
                 bd=10,
                 command=counter
                 )

btn4 = tk.Button(win,
                 text=f'Need to press: {count}',
                 widt=15,
                 height=3,
                 font=('Times New Roman', 18, 'bold'),
                 state=tk.NORMAL,
                 relief=tk.RAISED,
                 bd=10,
                 command=counter
                 )

timer = tk.Button(win,
                  text='00:00',
                  font=('Ubuntu', 16, 'bold'),
                  bg='#bebebe',
                  bd=7
                  )

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=2, column=0)
btn4.grid(row=2, column=1)
timer.grid(row=0, columnspan=2, sticky='n')

win.grid_columnconfigure(0, minsize=960)
win.grid_columnconfigure(1, minsize=960)
win.grid_rowconfigure(1, minsize=519)
win.grid_rowconfigure(2, minsize=519)
win.grid_rowconfigure(0, minsize=42)

win.config(bg='#bebebe')
win.title('Persistence')
win.attributes('-fullscreen', True)

win.mainloop()
