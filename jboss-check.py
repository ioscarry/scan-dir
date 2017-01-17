#!/usr/bin/env python
# -*- coding: utf-8 -*

import urllib2
import time
from sys import argv
import threadpool


"""
python jboss-check.py ips.txt 50

"""


file = argv[1]
f  = open(file,'r')

urls = f.readlines()
f.close()

vuls =['/jmx-console','/web-console','/invoker/JMXInvokerServlet','/admin-console']


def get_content(url):
	for vul in vuls:
		try: 
			x = url.strip()
			url_go = 'http://%s'%x+vul
			print url_go
			content = urllib2.urlopen(url_go,timeout=5)
			#html = content.read()
			code = content.code
			#print content.url
			if code != 404:
				w = 'http://'+url.strip()+'\n'
				write(w)
				break	


		except urllib2.HTTPError,e:
			print str(e.code)+url_go+' HTTPError'
			continue

		except Exception,e: ### timeout
			print e
			break

		except urllib2.URLError,e:
			print str(e.code)+url_go+' URLError'
			break


def write(url):
	with open('success.txt','a') as f:
		f.write(url)
		print 'success one - -'



pool = threadpool.ThreadPool(argv[2])  

start = time.time()

requests = threadpool.makeRequests(get_content, urls)
[pool.putRequest(req) for req in requests] 
pool.wait()  

print 'Need '+str(time.time()-start)
