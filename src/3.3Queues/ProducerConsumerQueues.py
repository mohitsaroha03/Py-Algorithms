# Link: 
# IsDone: 0
#!/usr/bin/env python

from random import randint
from time import sleep
from Queue import Queue
from myThread import MyThread

def writeQ(queue):
	print ('producing object for Q...',)
	queue.put('MONK', 1)
	print ("size now", queue.qsize())

def readQ(queue):
	val = queue.get(1)
	print ('consumed object from Q... size now', queue.qsize())

def producer(queue, loops):
	for i in range(loops):
	   writeQ(queue)
	   sleep(randint(1, 3))

def consumer(queue, loops):
	for i in range(loops):
	   readQ(queue)
	   sleep(randint(2, 5))

funcs = [producer, consumer]
nfuncs = range(len(funcs))

nloops = randint(2, 5)
q = Queue(32)

threads = []
for i in nfuncs:
   t = MyThread(funcs[i], (q, nloops),
       funcs[i].__name__)
   threads.append(t)

for i in nfuncs:
   threads[i].start()

for i in nfuncs:
   threads[i].join()

print ('all DONE')
