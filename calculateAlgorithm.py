# Global Variables
numbers = '0123456789'
operators = ['+', '-', 'x', ':', ':R', '^']
parenthesis = '()[]'


#  ========================== Expression Manipulation ==========================
# ##############################################################################


# Check for syntax in expression
def checkForValidSyntax(expression):
	if expression[0] in ['x', ':', '^']:
		return False

	if expression[len(expression) - 1] in operators:
		False

	# Check parethesis syntax
	stack = []

	for char in expression:
		if char in ['(', '[']:
			stack.append(char)

		if char in [')', ']']:
			if len(stack) == 0:
				return False
			else:
				stack.pop()

	if len(stack) != 0:
		return False

	return True


# Eliminate unecessary elements in expression string
def minimizeInput(expression):
	expression = expression.strip()
	newInput = ''

	for element in expression:
		if element not in ['+', '-'] or len(newInput) == 0:
			newInput += element

		else:
			lastElement = newInput[len(newInput) - 1]
			if lastElement not in ['+', '-']:
				newInput += element

			else:
				if element == '+':
					continue

				else:
					newInput = newInput[0:-1]
					if lastElement == '+':
						newInput += '-'
					else:
						newInput += '+'

	return newInput


# Seperate expression into a list that contains seperately operand and operator as element
def seperateExpr(expression):
	listOfElement = []
	tmp = ''

	for i in range(len(expression)):
		if expression[i] in numbers:
			tmp += expression[i]

			if i == len(expression) - 1:
				tmp = int(tmp)
				listOfElement.append(tmp)
		else:
			if tmp != '':
				tmp = int(tmp)
				listOfElement.append(tmp)
			listOfElement.append(expression[i])
			tmp = ''

	return listOfElement


#  ========================== Calculation Code	==========================
# ########################################################################

# get the priority of operator
def operatorPriority(operator):
	return {
		'+': 1,
		'-': 1,
		'x': 2,
		':': 2,
		'^': 3,
	}.get(operator)


# Compare if operator 1 (op1) has higher priorty than op2
def higherPriority(op1, op2):
	return True if operatorPriority(op1) >= operatorPriority(op2) else False


# Infix to Postfix using Stack
def infixToPostfix(exprList):
	postfix = []
	stack = []

	for i in range(len(exprList)):
		if str(exprList[i]) in numbers:
			postfix.append(exprList[i])

		elif exprList[i] == '(':
			stack.append(exprList[i])

		elif exprList[i] == ')':
			while len(stack) > 0 and stack[len(stack) - 1] != '(':
				postfix.append(stack[len(stack) - 1])
				stack.pop()
			stack.pop()

		else: #if str(exprList[i]) in operators:
			while len(stack) > 0 and stack[len(stack) - 1] != '(' and higherPriority(stack[len(stack) - 1], exprList[i]):
				postfix.append(stack[len(stack) - 1])
				stack.pop()

			stack.append(exprList[i])

	while len(stack) > 0:
		postfix.append(stack[len(stack) - 1])
		stack.pop()

	return postfix


# Calculate number base on operator
def calculate(operand1, operator, operand2):
	return {
		'+': operand1 + operand2,
		'-': operand1 - operand2,
		'x': operand1 * operand2,
		':': operand1 / operand2,
		'^': operand1 ** operand2,
	}.get(operator)


# Calculate the result base on postfix
def calculateExpr(expr):
	if not checkForValidSyntax(expr):
		return "Invalid Syntax"

	expr = minimizeInput(expr)
	postfix = infixToPostfix(seperateExpr(expr))

	stack =[]
	for element in postfix:
		if element not in operators:
			stack.append(element)

		else:
			operand1 = stack.pop()
			operand2 = stack.pop()
			result = calculate(operand2, element, operand1)
			stack.append(result)

	return stack[0]



# print(checkForValidSyntax('6-----(5+-------+--3)x2'))
# print(minimizeInput('6-----(5+-------+--3)x2'))
# print(seperateExpr('6-(5-3)x2'))
# print(operatorPriority('x'))
# print(higherPriority(':', 'x'))
# print(calculate(5, '-', 6))
# print(infixToPostfix(seperateExpr('6-(5-3)x2')))
# print(calculateExpr(''))



