#!/usr/local/bin/python
#coding = utf-8
#Author:
import urllib
import urllib2
import json

ip = raw_input('Please Enter IP Address:')
url = "http://ip.taobao.com/service/getIpInfo.php?ip="+ip

try:
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    jsondata = json.loads(res)
    print ""
    print "IP Address:"+jsondata['data']['ip']
    print "Country:"+jsondata['data']['country']
    print "Area:"+jsondata['data']['area']
    print "Region:"+jsondata['data']['region']
    print "City:"+jsondata['data']['city']
    print "ISP:"+jsondata['data']['isp']
    
except Exception as error:  
        print error
    print "Sorry,We Got a Error.Please Try Again Or Check Your Internet."
