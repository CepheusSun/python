# -- coding: UTF-8 --

import urllib2
# import timeit
import thread
import time


i = 0
x = 0
mylock = thread.allocate_lock()


def test(no,r):
    global i
    url = 'http://cepheussun.com/'
    for j in range(1,r):
        req=urllib2.Request(url)
        req.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)")
        file = urllib2.urlopen(req)
        print file.getcode()
        mylock.acquire()
        i += 1
        mylock.release()
        print i
        thread.exit_thread()


def fast():
        thread.start_new_thread(test,(1,50))
        thread.start_new_thread(test,(2,50))
        thread.start_new_thread(test,(3,50))
        thread.start_new_thread(test,(4,50))
        thread.start_new_thread(test,(5,50))
        thread.start_new_thread(test,(6,50))
        thread.start_new_thread(test,(7,50))

for x in range(1,150):
    fast()
    time.sleep(0.08)
    x = x + 1
