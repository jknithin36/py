# collection module
from collections import deque
# deque() , append(), popleft(), clear()
# if deque is full it remove oppositr eements
# FIFO QUEUE
customQueue = deque(maxlen=3)
print(customQueue)
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue)
# customQueue.append(4) # 1st element is overridden instead of throwing error "DeQuue is full"
# print(customQueue)
print(customQueue.popleft())
print(customQueue)
customQueue.clear()
print(customQueue)
# 2 - Queue Module

print("-----------------------")

import queue as q
customQueue = q.Queue(maxsize=3)

print(customQueue.qsize())
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.qsize())
print(customQueue.full())
customQueue.get()
print(customQueue.qsize())
print(customQueue.full())



# multi prceessing model

from multiprocessing import Queue

customQueue = Queue(maxsize=3)

customQueue.put(3)
customQueue.put(3)
customQueue.put(3)
print(customQueue)
print(customQueue.full)

list =[]

while not customQueue.empty():  # understand this logic very important 
    list.append(customQueue.get())