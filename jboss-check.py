#coding:utf-8
"""
shortcoming:only test 200 ips.
"""
import urllib2
import threading
#import multiprocessing
import time
from sys import argv
file = argv[1]
#url = 'http://103.237.144.234:8080' ##http://103.237.144.234:8080/
f  = open(file,'r')

urls = f.readlines()
f.close()
#success = []
vuls =['/jmx-console','/web-console','/invoker/JMXInvokerServlet','/admin-console']

#lock = threading.Semaphore(100)
def get_content(url,vuls):
	#lock.acquire()
	for vul in vuls:
		try: 
			x = url.strip()
			url_go = 'http://%s'%x+vul
			print url_go
			content = urllib2.urlopen(url_go,timeout=8)
			html = content.read()
			code = content.code
			#print content.url
			w = 'http://'+url.strip()+'\r\n'
			if code != 404:
				if code ==401:
					write(w)
					break	
				elif 'JMX Management Console' in html:  #jmx-console
					write(w)
					break
				elif 'Administration Console' in html:  #web-console
					write(w)
					break
				elif 'jboss' in html :					#admin-console
					write(w)
					break
				elif 'jboss' in html:					#JMXInvokerServlet
					write(w)
					break
				else:pass

		except urllib2.HTTPError,e:
			print str(e.code)+' HTTPError'
			continue

		except Exception,e:   ### timeout
			print e
			continue

		except urllib2.URLError,e:
			print str(e.code)+' URLError'
			continue

	#lock.release()
def write(url):
	with open('success.txt','a') as f:
		f.write(url)
	print 'success one - -'



threads=[]
start = time.time()

#with open(file,'r') as urls:
for url in urls:
	t = threading.Thread(target=get_content,args=(url,vuls))
	threads.append(t)

if __name__=='__main__':
	for i in range(len(threads)):
		threads[i].start()
		#threads[i].join()
	for i in range(len(threads)):
		threads[i].join()

print 'Need '+str(time.time()-start)

