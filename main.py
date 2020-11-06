import tkinter as tk

# FONTS
buttonFonts = ("Gothic", 15, 'bold')
funcButtonSize = (0.15, 0.1)
symbols = ('-', '+', ':', 'x', 'R', '^', '(', ')')


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
class nonFuncButton():
	def __init__(self, canvas, text, row, column, width, height):
		self.canvas = canvas
		self.text = text
		self.row = row
		self.column = column
		self.width = width
		self.height = height
		self.create()


	def create(self):
		self.name = tk.Button(self.canvas, text=self.text, bg='black', fg='white', 
						font=("Helvetica", 14, 'bold'), command=self.insert)
		self.name.grid(row=self.row, column=self.column, ipadx=self.width, ipady=self.height)


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


equalBt = funcButton(canvas, '=', summit, (0.8, 0.2))

answerBt = funcButton(canvas, 'Ans', get_recent_answer, (0.65, 0.2))

deleteBt = funcButton(canvas, 'Del', lambda: main_al.delete(len(main_al.get()) - 1), (0.65, 0.3))

clearBt = funcButton(canvas, 'C', clear_main, (0.8, 0.3))

resetBt = funcButton(canvas, 'Reset', clear_documet, (0.8, 0.4))

lastAlBt = funcButton(canvas, 'L.A', last_algorithm, (0.65, 0.4))




# make number buttons
numFrame = tk.Frame(canvas, bg='black')
numFrame.place(relx=0.05, rely=0.2, relwidth=0.58, relheight=0.75)

text = 1
for row in range(1, 4):
	for column in range(1, 4):
		bt = nonFuncButton(numFrame, text, row, column, 35, 30)
		text += 1

zero_bt = nonFuncButton(numFrame, 0, 4, 2, 35, 30)


# make operator buttons
operatorFrame = tk.Frame(canvas, bg='gray')
operatorFrame.place(relx=0.65, rely=0.55, relwidth=0.3, relheight=0.4)

count = 0
for row in range(1, 5):
	for column in range(1, 3):
		text = symbols[count]
		bt = nonFuncButton(operatorFrame, text, row, column, 18.875, 6.3125)
		count += 1





root.mainloop()