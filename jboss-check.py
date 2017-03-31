#!/usr/bin/env python
# -*- coding: utf-8 -*

import requests
import time
from sys import argv
import threadpool
from random import randint
from os import  path

"""
python jboss-check.py ips.txt 50

"""


file = argv[1]
f  = open(file,'r')

url = f.readlines()
urls=[]
for i in url:
	urls.append(i.strip())
f.close()





def get_random_user_agent():
    user_agents = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
                   "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
                   "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
                   "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1)",
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
                   "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
                   "Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.17",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"]
    return user_agents[randint(0, len(user_agents) - 1)]

def get_headers():
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Connection": "keep-alive",
               "User-Agent": get_random_user_agent()}
    return  headers

vuls =['/jmx-console','/web-console','/invoker/JMXInvokerServlet','/admin-console']
def get_content(host):
    for vul in vuls:
        try:
            url = 'http://'+host+vul
            #print url
            content = requests.get(url,headers=get_headers(),timeout=5,allow_redirects=False)
            code =content.status_code
            if code == 200 and "jboss" in content.text:
                write(host)
                break

            elif code == 401:
                write(host)
                print '401'
                break
        except Exception,e:
            #print e.message
            break

pwd=path.dirname(argv[1])
global counter
counter=0
def write(url_succ):
	with open(pwd+'/success.txt','a') as f:
		f.write(url_succ+'\n')
		global counter
		counter =counter+1
		print 'success one - - '+str(counter)

def w_401(url_succ):
    with open(pwd+'/success_401.txt','a') as f:
		f.write(url_succ+'\n')
		#global counter
		#counter =counter+1
		#print 'success one - - '+str(counter)

if __name__ == '__main__':
    pool = threadpool.ThreadPool(int(argv[2]))
    start = time.time()
    requests_ = threadpool.makeRequests(get_content,urls)
    [pool.putRequest(req) for req in requests_]
    pool.wait()
    print 'Need ' + str(time.time() - start)
