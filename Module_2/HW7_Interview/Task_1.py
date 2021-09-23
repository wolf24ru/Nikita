from ClassStack import Stack

if __name__ == '__main__':
    stack_1 = Stack('123 45')
    empty_stack = Stack('')

    print(stack_1.isEmpty())
    print(empty_stack.isEmpty())
    stack_1.push('7')
    empty_stack.push('1')
    print(f'''
Количество элементов в stack_1 = {stack_1.size()}
Последний элемент stack_1 =  {stack_1.peek()}
Количество элементов в empty_stack = {empty_stack.size()}
Последний элемент empty_stack = {empty_stack.peek()}

Элемент {stack_1.pop()} был удален
Элемент {empty_stack.pop()} был удален

Количество элементов в stack_1 = {stack_1.size()}
Последний элемент stack_1 =  {stack_1.peek()}
Количество элементов в empty_stack = {empty_stack.size()}
Последний элемент empty_stack = {empty_stack.peek()}
  ''')
