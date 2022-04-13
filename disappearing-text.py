# -*- coding: utf-8 -*-
"""
Disappearing Text Writing App

@author: ANAT-H

timer icon by https://icons8.com/icon/YpYKjtEKaXLy/timer" 
icon by "https://icons8.com"

"""
from tkinter import *
from tkinter import ttk
from string import printable
from time import sleep

# consts
BG = 'black'
TEXT_FONT=('courier', 20, 'bold')
COUNTER_FONT=('courier', 28, 'bold')
TEXTBOX_FONT = ('courier', 12, 'bold')
BUTTON_FONT = ('courier', 15, 'normal')
P_CODES = {'exclam': 49,
 'quotedbl': 222,
 'numbersign': 51,
 'dollar': 52,
 'percent': 53,
 'ampersand': 55,
 'backslash': 220,
 'parenleft': 57,
 'parenright': 48,
 'asterisk': 106,
 'plus': 107,
 'minus': 109,
 'period': 110,
 'slash': 111,
 'colon': 186,
 'less': 188,
 'equal': 187,
 'greater': 190,
 'question': 191,
 'at': 50,
 'bracketleft': 219,
 'bracketright': 221,
 'asciicircum': 54,
 'underscore': 189,
 'asciitilde': 192,
 'backspace': 8}

start_timer=False
after_id=None

def start():
    global after_id
    intro.grid_forget()
    start_btn.grid_forget()
    label_text.set('Start Writing...')
    label.grid(column=2, row=1, pady=(40,10), sticky=(W,E)) 
    countdown.grid(column=2, row=1, pady=(40,10), sticky=E) 
    count.set('5')
    after_id = root.after(1000, update)
    textbox.grid(column=2, row=2, padx=(10,0), pady=20, sticky=(N ,W, E, S))
    scroller.grid(column=3, row=2, padx=(0, 10), pady=20, sticky=(N, S, E))
    textbox.focus()

  
def start_timing(event):
    '''
    set start_timer as True upon typing.
    reset timer while typing
  
    Parameters
    ----------
    event : Event
      KeyPress Event.
  
    '''
    global start_timer
    if (event.keysym in printable) or (event.keycode in P_CODES.values()):
      start_timer=True
      label_text.set('Writing...')
      count.set('5')  

def update():
    '''
    update timer if started.
    call clear_text() if timer reaches 0.
    scheduled next after() call
  
    '''
    
    global after_id
    if start_timer==True:
      sec = int(count.get())-1 
      if sec > 0:
        count.set(str(sec)) 
      else:  
        count.set('0')  
        after_id = root.after(100, clear_text)    
    after_id = root.after(1000, update)
      

def clear_text():
    '''
    clear textbox content
  
    '''
    global start_timer 
    textbox.delete('1.0',END) 
    label_text.set('Start Writing...')
    count.set('5')
    start_timer=False

def wquit():
    '''
    remove all pending tasks and exit.
  
    '''
    if after_id:
      root.after_cancel(after_id)
    root.destroy()
    
## main window
root = Tk()
root.title('Disappearing Text Writing App')
root.minsize(600,500)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

## styles
style = ttk.Style()
style.configure('style.TFrame', background=BG)
style.configure('style.TLabel', background=BG, foreground='pink', font=TEXT_FONT)
style.configure('stylecount.TLabel', background=BG, foreground='pink', font=COUNTER_FONT)
style.configure('style.TButton', background=BG, foreground='black', font=BUTTON_FONT)

## main frame
frame = ttk.Frame(root, padding='20 0 20 20', style='style.TFrame')
frame.grid(column=0, row=0, sticky=(N ,W, E, S))
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=2)
frame.columnconfigure(3, weight=0)
frame.columnconfigure(4, weight=1)
frame.rowconfigure(2, weight=1)

## content
# first screen
intro = ttk.Label(frame, text='Write a poem, a novel, or a short story,\nbut do not linger..\nor your work will be undone...', style='style.TLabel')
intro.grid(column=1, row=1, padx=20, pady=(150, 10), sticky=(W,E))
start_btn = ttk.Button(frame, text="Let's go", command=start, style='style.TButton')
start_btn.grid(column=1, row=2, sticky=S, pady=(0, 120), ipady=3)

# second screen
label_text = StringVar()
label = ttk.Label(frame, textvariable=label_text, style='style.TLabel')
count = StringVar()
image=PhotoImage(file="icons8-timer-64.png")
countdown = ttk.Label(frame, image=image, textvariable=count, compound='left', style='stylecount.TLabel')
textbox = Text(frame, wrap='word', width=60, height=20, font=TEXTBOX_FONT)
scroller = ttk.Scrollbar(frame, orient=VERTICAL, command=textbox.yview)
textbox['yscrollcommand'] = scroller.set
textbox.bind('<KeyPress>',start_timing)

root.protocol('WM_DELETE_WINDOW', wquit)
root.mainloop()










