class Stack:
    def __init__(self):
        self.my_stack = []


    # проверка стека на пустоту. Метод возвращает True или False
    def isEmpty(self):
        if self.my_stack:
            return False
        else:
            return True

    # добавляет новый элемент на вершину стека. Метод ничего не возвращает
    def push(self, new):
        self.my_stack.append(new)

    # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        res = self.my_stack.pop()
        return res

    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        return self.my_stack[-1]


    # возвращает количество элементов в стеке.
    def size(self):
        return len(self.my_stack)


if __name__ == '__main__':
    example = input('Введите последовательность:')
    stack = Stack()
    brackets = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    isEmpty = True
    for i in example:
        if i in brackets.values():
            stack.push(i)
            print(stack.my_stack)
        if i in brackets:
            if stack.isEmpty():
                isEmpty = False
                break
            if stack.peek() == brackets[i]:
                stack.pop()
            else:
                isEmpty = False
                break

    if isEmpty:
        print('Сбалансированная последовательность')
    else:
        print('Несбалансированная последовательность')

