'''

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''


class MyStack:

    def __init__(self):
        self.queue = []
        self.temp = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for n in range(len(self.queue) - 1):
            self.temp.append(self.queue.pop(0))
        result = self.queue.pop()
        self.queue = self.temp.copy()
        self.temp.clear()
        return result

    def top(self) -> int:
        for n in range(len(self.queue) - 1):
            self.temp.append(self.queue.pop(0))
        result = self.queue.pop()
        self.temp.append(result)
        self.queue = self.temp.copy()
        self.temp.clear()
        return result

    def empty(self) -> bool:
        return not self.queue