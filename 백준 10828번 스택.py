# 백준 10828번 스택

class Stack():
    def __init__(self):
        self.stack_list = []
        self.top = -1
    def push(self, x):
        self.stack_list.append(x)
        self.top += 1
    def empty(self):
        if self.top == -1:
            print(1)
        else:
            print(0)
    def pop(self):
        if self.top == -1:
            print(-1)
        else:
            x = self.stack_list.pop()
            self.top -= 1
            print(x)
    def top(self):
        if self.top == -1:
            print(-1)
        else:
            print(self.stack_list[-1])
    def size(self):
        print(len(self.stack_list))

def function_call(ftn_name, self):
    getattr(Stack, ftn_name)(self)

stack = Stack()
n = int(input())
orders = []
for i in range(n):
    orders.append(input().split())

for order in orders:
    if len(order) == 1:
        function_call(order[0], stack)
    else:
        stack.push(int(order[1]))