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
