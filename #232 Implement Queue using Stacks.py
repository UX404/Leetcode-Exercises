'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''


class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while len(self.stack) > 1:
            self.temp.append(self.stack.pop())
        result = self.stack.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        return result

    def peek(self) -> int:
        while len(self.stack) > 1:
            self.temp.append(self.stack.pop())
        result = self.stack[0]
        while self.temp:
            self.stack.append(self.temp.pop())
        return result

    def empty(self) -> bool:
        if self.stack:
            return False
        else:
            return True