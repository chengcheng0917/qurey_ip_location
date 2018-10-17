#!/usr/bin/env python
# -*- coding: utf-8 -*-
#created by chengcheng at Oct 17 2018

import urllib2
from pyquery import PyQuery as pq



def qurey_ip(ip):
    url = 'https://ip.cn/index.php?ip=' + ip
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
    opener = urllib2.build_opener()
    f = opener.open(request)
    a = f.read()
    d = pq(a)
    print ip,d('p').eq(1).html().replace('code','').replace('<>','').replace('</>',''),d('p').eq(2).html(),d('p').eq(3).html()







def main():
    ip = '117.35.134.250'
    qurey_ip(ip)

if __name__ == '__main__':
    main()