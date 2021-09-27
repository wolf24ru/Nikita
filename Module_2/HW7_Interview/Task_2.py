from ClassStack import Stack


def balanced(brackits_str: str) -> str:
    balanced_stack = Stack(brackits_str)
    empty_stack = Stack('')
    brackits_open = ['[', '(', '{']
    brackits_list = ['[]', '()', '{}']
    if balanced_stack.size() % 2 != 0:
        return 'Несбалансированно'
    empty_stack.push(balanced_stack.pop())
    for i in range(balanced_stack.size()):
        if balanced_stack.peek() in brackits_open and (balanced_stack.peek() + empty_stack.peek()) in brackits_list :
            balanced_stack.pop()
            empty_stack.pop()
            continue
        elif balanced_stack.peek() in brackits_open and (balanced_stack.peek() + empty_stack.peek()) not in brackits_list:
            return 'Несбалансированно'
    if balanced_stack.size()+empty_stack.size() == 0:
        return 'Сбалансированно'
    return 'Несбалансированно'


if __name__ == '__main__':
    print(balanced('[[{())}]'))