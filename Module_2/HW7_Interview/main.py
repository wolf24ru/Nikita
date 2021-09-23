# https://github.com/netology-code/py-homeworks-advanced/tree/master/7.Interview

from collections import deque


class Stack:
	def __init__(self, stec_elements):
		self.stec_elements = deque(stec_elements)

	def isEmpty(self) -> bool:
		"""
		проверка стека на пустоту.
		Метод возвращает True если стек пуст
		или False если стек не пуст
		:return: bool
		"""
		if len(self.stec_elements):
			return False
		return True

	def push(self, new_element):
		"""
		добавляет новый элемент на вершину стека. Метод ничего не возвращает
		"""
		self.stec_elements.append(new_element)

	def pop(self):
		"""
		удаляет верхний элемент стека. Стек изменяется.
		:return:Метод возвращает верхний элемент стека
		"""
		return self.stec_elements.pop()

	def peek(self):
		"""
		возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
		:return:Возвращает верхний элемент стека, но не удаляет
		"""
		if len(self.stec_elements) > 0:
			return self.stec_elements[-1]
		return None

	def size(self) -> int:
		"""
		возвращает количество элементов в стеке.
		:return: int
		"""
		return len(self.stec_elements)

	# def balanced(self) -> str:
	# 	brackits = ['[]', '()', '{}']
	# 	for self.
	# 	return self.stec_elements.count('(')

def balanced(brackits_str: str) -> str:
	balanced_stack = Stack(brackits_str)
	empty_stack = Stack('')
	brackits_open = ['[', '(', '{']
	brackits_close =[']', ')', '}']
	if balanced_stack.size() % 2 != 0:
		return 'Несбалансированно'

	for i in range(balanced_stack.size()):
		pass

	# for i in range(int(balanced_stack.size()/2)):
	# 	empty_stack.push(balanced_stack.pop())
	#
	# while not balanced_stack.isEmpty():
	# 	brackits = balanced_stack.pop() + empty_stack.pop()
	# 	if brackits not in brackits_list:
	# 		return 'Несбалансированно'
	# return 'Сбалансированно'



if __name__ == '__main__':
	print(balanced('[([])((([[[]]])))]{()}'))
# 	stack_1 = Stack('123 45')
# 	empty_stack = Stack('')
#
# 	print(stack_1.isEmpty())
# 	print(empty_stack.isEmpty())
# 	stack_1.push('7')
# 	empty_stack.push('1')
# 	print(f'''
# Количество элементов в stack_1 = {stack_1.size()}
# Последний элемент stack_1 =  {stack_1.peek()}
# Количество элементов в empty_stack = {empty_stack.size()}
# Последний элемент empty_stack = {empty_stack.peek()}
#
# Элемент {stack_1.pop()} был удален
# Элемент {empty_stack.pop()} был удален
#
# Количество элементов в stack_1 = {stack_1.size()}
# Последний элемент stack_1 =  {stack_1.peek()}
# Количество элементов в empty_stack = {empty_stack.size()}
# Последний элемент empty_stack = {empty_stack.peek()}
# 	''')



