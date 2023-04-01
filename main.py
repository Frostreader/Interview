
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")

    def size(self):
        return len(self.items)


def is_balanced(expression):
    stack = Stack()

    for char in expression:
        if char in ["(", "{", "["]:
            stack.push(char)
        elif char in [")", "}", "]"]:
            if stack.is_empty():
                return "Несбалансированно"
            elif char == ")" and stack.peek() == "(":
                stack.pop()
            elif char == "}" and stack.peek() == "{":
                stack.pop()
            elif char == "]" and stack.peek() == "[":
                stack.pop()
            else:
                return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"

expression = input()
print(is_balanced(expression))

