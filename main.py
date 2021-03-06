def is_operator(s):
	if s in '*+-()':
		return True
	return False


class Node:
	def __init__(self, lchild_ind):
		self.left = lchild_ind
		self.right = -1
		self.val = ''


class Exp:
	def __init__(self, charcount):
		self.tree = [Node(i) for i in range(1, charcount + 1)]
		self.tmp = []
		self.root = 0
		self.next_fchild = 0
	
	def insert(self, token):
		if self.next_fchild == -1:
			return 'tree full'
		if self.next_fchild == 0:
			self.tree[self.root].val = token
			self.next_fchild = self.tree[self.root].left
			self.tree[self.root].left = -1
			
		else:
			cur = 0
			prev = -1
			NewNode = self.tree[self.next_fchild]
			NewNode.val = token
			while cur != -1:
				CurNode = self.tree[cur]
				if is_operator(CurNode.val):
					if CurNode.left == -1:
						CurNode.left = self.next_fchild
						self.next_fchild = NewNode.left
						NewNode.left = -1
						cur = -1
					elif CurNode.right == -1:
						CurNode.right == self.next_fchild
						self.next_fchild = NewNode.left
						NewNode.left = -1
						cur = -1
					elif is_operator(self.tree[CurNode.left].val):
						prev = cur
						cur = CurNode.left
						self.tmp.append(prev)
					elif is_operator(self.tree[CurNode.right].val):
						prev = cur
						cur = CurNode.right
						self.tmp.append(prev)
					else:
						prev = self.tmp.pop(-1)
						cur = self.tree[prev].right
				else:
					return
	
	def __str__(self):
		out = ''
		for i in range(len(self.tree)):
			out += f'Index: {i} Val: {self.tree[i].val} left: {self.tree[i].left} right: {self.tree[i].right}\n'
		return out


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


if __name__ == '__main__':
	working = True
	while working:
		usrinp = input().strip().replace(' ', '')
		if usrinp == 'exit':
			working = False
			continue
		if not braces_check(usrinp):
			print('unbalanced braces')
			continue
		exp = list(exp_tolist(usrinp))
		calculator = Exp(len(exp))
		a = []
		for elem in exp:
			calculator.insert(calculator.braces(elem, a))
		print(calculator)
		#print(calculator.calc())
	
