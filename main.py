import tkinter as tk

# FONTS
buttonFonts = ("Gothic", 15, 'bold')
funcButtonSize = (0.15, 0.1)


# BUTTON FUNCTIONS
def summit():
	print('summit')


def get_recent_answer():
	print('Recent answer')


def clear_main():
	print('clear main')


def clear_documet():
	print('clear document')


def last_algorithm():
	print('last al')


# buttons preresent number
class numberButton():
	def __init__(self,name, text, row, column, x, y):
		self.name = name
		self.text = text
		self.row = row
		self.column = column
		self.x = x
		self.y = y
		self.create()

	def create(self):
		self.name = tk.Button(num_lab, text=self.text, bg='black', fg='white', 
						font=("Helvetica", 14, 'bold'), command=self.insert)
		self.name.grid(row=self.row, column=self.column, ipadx=self.x, ipady=self.y)

	def insert(self):
		if main_al['justify'] == 'right':
			main_al['justify'] = 'left'
			main_al.delete(0, tk.END)
		main_al.insert(tk.END, self.name['text'])


# Button class to preresent functions button such as minus, plus ...
class funcButton():
	def __init__(self, canvas, text, function, coordinate=(0, 0), size=funcButtonSize, bg='black', fg='white', font=buttonFonts):
		self.canvas = canvas
		self.text = text
		self.function = function
		self.coordinate = coordinate
		self.size = size
		self.bg = bg
		self.fg = fg
		self.font = font
		self.create()


	def create(self):
		summit = tk.Button(	canvas, 
							text 	=	self.text, 
							bg   	=	self.bg, 
							fg   	=	self.fg, 
							font 	=	self.font,
							command	=	self.function)
		x, y = self.coordinate
		width, height = self.size
		summit.place(relx=x, rely=y, relwidth=width, relheight=height)



root = tk.Tk()
root.title('Calculator')

canvas = tk.Canvas(root, height=500, width=500, bg='gray')
canvas.pack()

main_al = tk.Entry(canvas, bg='white', font=("Courier", 20), selectbackground='red',
					highlightcolor='yellow', bd=5)
main_al.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

# summit = tk.Button(canvas, text='=', bg='black', fg='white', font=buttonFonts,
# 					command=summit)
# summit.place(relx=0.8, rely=0.2, relwidth=0.15, relheight=0.1)

equalBt = funcButton(canvas, '=', summit, (0.8, 0.2))

# anws = tk.Button(canvas, text='ANS', bg='black', fg='white', font=buttonFonts,
# 					command=get_recent_answer)
# anws.place(relx=0.65, rely=0.2, relwidth=0.15, relheight=0.1)

answerBt = funcButton(canvas, 'Ans', get_recent_answer, (0.65, 0.2))

# delete = tk.Button(canvas, text='Del', bg='black', fg='white', font=buttonFonts,
# 					command=lambda: main_al.delete(len(main_al.get()) - 1))
# delete.place(relx=0.65, rely=0.3, relwidth=0.15, relheight=0.1)

deleteBt = funcButton(canvas, 'Del', lambda: main_al.delete(len(main_al.get()) - 1), (0.65, 0.3))

# clear = tk.Button(canvas, text='C', bg='black', fg='white', font=buttonFonts,
# 					command=clear_main)
# clear.place(relx=0.8, rely=0.3, relwidth=0.15, relheight=0.1)

clearBt = funcButton(canvas, 'C', clear_main, (0.8, 0.3))

# reset = tk.Button(canvas, text='Reset', bg='black', fg='white', font=buttonFonts,
# 					command=clear_documet)
# reset.place(relx=0.8, rely=0.4, relwidth=0.15, relheight=0.1)
resetBt = funcButton(canvas, 'Reset', clear_documet, (0.8, 0.4))

# L_A = tk.Button(canvas, text='L.A', bg='black', fg='white', font=buttonFonts,
# 					command=last_algorithm)
# L_A.place(relx=0.65, rely=0.4, relwidth=0.15, relheight=0.1)

lastAlBt = funcButton(canvas, 'L.A', last_algorithm, (0.65, 0.4))

plus = tk.Button(canvas, text='+', bg='black', fg='white', font=buttonFonts,
					command= lambda: main_al.insert(tk.END, plus['text']))
plus.place(relx=0.8, rely=0.55, relwidth=0.15, relheight=0.1)

minus = tk.Button(canvas, text='-', bg='black', fg='white', font=buttonFonts,
					command= lambda: main_al.insert(tk.END, minus['text']))
minus.place(relx=0.65, rely=0.55, relwidth=0.15, relheight=0.1)

time = tk.Button(canvas, text='x', bg='black', fg='white', font=buttonFonts,
					command= lambda: main_al.insert(tk.END, time['text']))
time.place(relx=0.8, rely=0.65, relwidth=0.15, relheight=0.1)

divide = tk.Button(canvas, text='/', bg='black', fg='white', font=buttonFonts,
					command= lambda: main_al.insert(tk.END, divide['text']))
divide.place(relx=0.65, rely=0.65, relwidth=0.15, relheight=0.1)

power = tk.Button(canvas, text='^', bg='black', fg='white', font=buttonFonts,
					command= lambda: main_al.insert(tk.END, power['text']))
power.place(relx=0.8, rely=0.75, relwidth=0.15, relheight=0.1)

remainder = tk.Button(canvas, text='%R', bg='black', fg='white', font=buttonFonts,
					command= lambda: main_al.insert(tk.END, '%'))
remainder.place(relx=0.65, rely=0.75, relwidth=0.15, relheight=0.1)

open_bracket = tk.Button(canvas, text='(', bg='black', fg='white', font=buttonFonts,
					command= lambda: main_al.insert(tk.END, '('))
open_bracket.place(relx=0.65, rely=0.85, relwidth=0.15, relheight=0.1)

close_bracket = tk.Button(canvas, text=')', bg='black', fg='white', font=buttonFonts,
					command= lambda: main_al.insert(tk.END, ')'))
close_bracket.place(relx=0.8, rely=0.85, relwidth=0.15, relheight=0.1)

num_lab = tk.Frame(canvas, bg='black')
num_lab.place(relx=0.05, rely=0.2, relwidth=0.58, relheight=0.75)

text = 1
for row in range(1, 4):
	for column in range(1, 4):
		bt = numberButton('button', text, row, column, 35, 30)
		text += 1

bt = numberButton('button', 0, 4, 2, 35, 30)


root.mainloop()