# -*- coding: UTF-8 -*-
import urllib
import urllib2
import re

InfoName = 743
url = 'http://dep.gdpu.edu.cn/jwc/plus/view.php?aid=' + str(InfoName)
try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    url = response.geturl()
    content = response.read().decode('utf-8')
    pattern = re.compile('<h5.style="font.+?>(.+?)</h5>',re.S)
    # pattern = re.compile('<h5.+?>(.+?)</h5>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item
        print "来源：".decode('utf-8').encode('gbk')
        print str(url)
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
except:
    print "暂无"
