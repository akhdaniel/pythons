import thread
import time


def print_time(threadName, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count +=1
		print "%s: %s" % (threadName, time.ctime(time.time()) )

try:
	thread.start_new_thread(print_time, ('Thread1', 2 ) )
	thread.start_new_thread(print_time, ('Thread2', 4 ) )

except:
	print "gagal start thread.. "

while 1: 
	pass