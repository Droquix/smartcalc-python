import tkinter as tk
from math import *
from datetime import datetime

# ---------------------------------
# SIMPLE TWO-COLOR CALCULATOR
# ---------------------------------
root = tk.Tk()
root.title('SmartCalc')
root.geometry('400x700')
root.configure(bg='#111111')
root.resizable(False, False)

expression = ''

PRIMARY = '#111111'
SECONDARY = '#f2f2f2'

# HEADER
header = tk.Frame(root, bg=PRIMARY, height=50)
header.pack(fill='x')

clock = tk.Label(header, text=datetime.now().strftime('%H:%M'), fg=SECONDARY, bg=PRIMARY, font=('Segoe UI', 12, 'bold'))
clock.pack(side='left', padx=12, pady=10)

brand = tk.Label(header, text='SmartCalc', fg=SECONDARY, bg=PRIMARY, font=('Segoe UI', 14, 'bold'))
brand.pack(side='right', padx=12)

# DISPLAY
entry = tk.Entry(root, font=('Segoe UI', 34), bg=PRIMARY, fg=SECONDARY, bd=0, justify='right', insertbackground=SECONDARY)
entry.pack(fill='x', padx=18, pady=20, ipady=25)

# FUNCTIONS
def refresh_clock():
    clock.config(text=datetime.now().strftime('%H:%M'))
    root.after(1000, refresh_clock)

def update_display():
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def press(v):
    global expression
    expression += str(v)
    update_display()

def clear():
    global expression
    expression = ''
    update_display()

def backspace():
    global expression
    expression = expression[:-1]
    update_display()

def equal():
    global expression
    try:
        expression = str(eval(expression))
    except:
        expression = 'Error'
    update_display()

# BUTTONS
frame = tk.Frame(root, bg=PRIMARY)
frame.pack(expand=True, fill='both', padx=12, pady=10)

buttons = [
 ['C','⌫','%','/'],
 ['7','8','9','*'],
 ['4','5','6','-'],
 ['1','2','3','+'],
 ['0','.','=','**']
]

for r,row in enumerate(buttons):
    for c,text in enumerate(row):
        if text == 'C': cmd = clear
        elif text == '⌫': cmd = backspace
        elif text == '=': cmd = equal
        else: cmd = lambda t=text: press(t)

        btn = tk.Button(frame,
            text=text,
            command=cmd,
            font=('Segoe UI', 18, 'bold'),
            bg=SECONDARY,
            fg=PRIMARY,
            bd=0,
            relief='flat',
            activebackground='#d9d9d9',
            activeforeground=PRIMARY,
            cursor='hand2')
        btn.grid(row=r,column=c,sticky='nsew',padx=6,pady=6,ipady=18)

for i in range(5):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

footer = tk.Label(root, text='Built with Python', fg='#777777', bg=PRIMARY, font=('Segoe UI', 9))
footer.pack(pady=6)

refresh_clock()
root.mainloop()