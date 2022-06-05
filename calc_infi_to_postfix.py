def braces_check(exp: str) -> bool:
	stack = []
	for char in exp:
		if char == '(':
			stack.append(char)
		elif char == ')':
			if stack:
				stack.pop()
			else:
				return False
	if not stack:
		return True
	return False

def infix_to_postfix(epx: list) -> list:
	operators = ['+', '-', '*', '/', '(', ')', '^']
	priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
	stack = []
	output = []
	
	for char in epx:
		if char not in operators:
			output.append(char)
		elif char == '(':
			stack.append('(')
		elif char == ')':
			while stack and stack[-1] != '(':
				output += stack.pop()
			stack.pop()
		else:
			while stack and stack[-1] != '(' and priority[char] <= priority[stack[-1]]:
				output += stack.pop()
			stack.append(char)
	while stack:
		output += stack.pop()
	return output


def exp_tolist(exp: str) -> list:
	tmp = ''
	for char in exp:
		if char.isnumeric():
			tmp += char
		else:
			if tmp:
				yield tmp
			yield char
			tmp = ''
	if tmp:
		yield tmp


def calculate(exp: list[str]) -> float:
	def operator(a ,b, char):
		match char:
			case '+':
				return a + b
			case '-':
				return a - b
			case '*':
				return a * b
			case '/':
				return a / b
			case '^':
				return a ** b
		
	calc_stack = []
	for elem in exp:
		print(calc_stack)
		if elem.isdigit():
			calc_stack.append(float(elem))
		else:
			y, x = calc_stack.pop(), calc_stack.pop()
			calc_stack.append(operator(x, y, elem))
	
	return calc_stack

	
if __name__ == '__main__':
	alive = True
	while alive:
		usrinp = input()
		if usrinp in set(['exit', 'end', 'e', 'kill', 'stop']):
			alive = False
			continue
		if braces_check(usrinp):
			expression = usrinp
		else:
			print('unbalanced braces')
			continue
		expression = list(exp_tolist(expression))
		expression = infix_to_postfix(expression)
		print(calculate(expression))