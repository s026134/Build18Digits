#An amazing super poggers GUI calculator
#using stinky python

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)


# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)

		# initialize the expression variable
		# by empty string
		expression = ""

	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background="black")

	# set the title of GUI window
	gui.title("POG Calculator uwu")

	# set the configuration of GUI window
	gui.geometry("800x850")

	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()

	# create the text entry box for
	# showing the expression .
	expression_field = Entry(gui, textvariable=equation, font=('Arial 100'), width=13, justify='right')

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	expression_field.grid(columnspan=4, padx=30, pady=10)
	
	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	button1 = Button(gui, text=' 1 ', fg='gray', bg='black', font=('Arial 80'), highlightcolor='yellow',
					command=lambda: press(1), height=1, width=1)
	button1.grid(row=1, column=0, sticky='EW'+'NS', padx=10, pady=10)

	button2 = Button(gui, text=' 2 ', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press(2), height=1, width=1)
	button2.grid(row=1, column=1, sticky='EW'+'NS', padx=10, pady=10)

	button3 = Button(gui, text=' 3 ', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press(3), height=1, width=1)
	button3.grid(row=1, column=2, sticky='EW'+'NS', padx=10, pady=10)

	button4 = Button(gui, text=' 4 ', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press(4), height=1, width=1)
	button4.grid(row=2, column=0, sticky='EW'+'NS', padx=10, pady=10)

	button5 = Button(gui, text=' 5 ', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press(5), height=1, width=1)
	button5.grid(row=2, column=1, sticky='EW'+'NS', padx=10, pady=10)

	button6 = Button(gui, text=' 6 ', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press(6), height=1, width=1)
	button6.grid(row=2, column=2, sticky='EW'+'NS', padx=10, pady=10)

	button7 = Button(gui, text=' 7 ', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press(7), height=1, width=1)
	button7.grid(row=3, column=0, sticky='EW'+'NS', padx=10, pady=10)

	button8 = Button(gui, text=' 8 ', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press(8), height=1, width=1)
	button8.grid(row=3, column=1, sticky='EW'+'NS', padx=10, pady=10)

	button9 = Button(gui, text=' 9 ', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press(9), height=1, width=1)
	button9.grid(row=3, column=2, sticky='EW'+'NS', padx=10, pady=10)

	button0 = Button(gui, text=' 0 ', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press(0), height=1, width=1)
	button0.grid(row=4, column=0, sticky='EW'+'NS', padx=10, pady=10, columnspan=2)

	plus = Button(gui, text=' + ', fg='gray', bg='black', font=('Arial 80'),
				command=lambda: press("+"), height=1, width=1)
	plus.grid(row=4, column=3, sticky='EW'+'NS', padx=10, pady=10)

	minus = Button(gui, text=' - ', fg='gray', bg='black', font=('Arial 80'),
				command=lambda: press("-"), height=1, width=1)
	minus.grid(row=3, column=3, sticky='EW'+'NS', padx=10, pady=10)

	multiply = Button(gui, text=' * ', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press("*"), height=1, width=1)
	multiply.grid(row=2, column=3, sticky='EW'+'NS', padx=10, pady=10)

	divide = Button(gui, text=' / ', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press("/"), height=1, width=1)
	divide.grid(row=1, column=3, sticky='EW'+'NS', padx=10, pady=10)

	equal = Button(gui, text=' = ', fg='gray', bg='black', font=('Arial 80'),
				command=equalpress, height=1, width=1)
	equal.grid(row=5, column=2, sticky='EW'+'NS', padx=10, pady=10, columnspan=2)
	

	clear = Button(gui, text='Clear', fg='gray', bg='black', font=('Arial 80'),
				command=clear, height=1, width=1)
	clear.grid(row=5, column=0, sticky='EW'+'NS', padx=10, pady=10, columnspan=2)

	Decimal= Button(gui, text='.', fg='gray', bg='black', font=('Arial 80'),
					command=lambda: press('.'), height=1, width=1)
	Decimal.grid(row=4, column=2, sticky='EW'+'NS', padx=10, pady=10)
	# start the GUI
	gui.mainloop()
