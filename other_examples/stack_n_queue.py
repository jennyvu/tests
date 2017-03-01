#!/usr/bin/env python
from collections import deque

# list as stack
stack = ['a', 'b', 'c']
stack.append('d')
print stack.pop()

# list as queues (lifo & fifo)
# fifo
queue = deque(stack)
queue.append('d')
print queue.popleft()

# lifo
queue.appendleft('e')
print queue.popleft()

# pop from the right
print queue.pop()

# clear queue
print list(queue)
queue.clear()

print list(queue)
print list(stack)

