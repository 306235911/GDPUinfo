# -*- coding: UTF-8 -*-
import urllib
import urllib2
import re
import mysql

class GDPU:
    def __init__(self):
        # 初始页面的代码
        self.InfoName = 720
        # 生产url
        self.url = 'http://dep.gdpu.edu.cn/jwc/plus/view.php?aid=' + str(self.InfoName)
        # 初始化title
        self.title = []
        # 初始化（连接）数据库
        self.mysql = mysql.Mysql()
        # url连接的头文件
        self.user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent' : self.user_agent }


    def getPage(self,url):
        try:
            # 使用头文件连接url
            request = urllib2.Request(url, headers = self.headers)
            # 获得响应
            response = urllib2.urlopen(request)
            # 德到网页源码
            content = response.read().decode('utf-8')
            # 正则表达式，以得到通知名
            pattern = re.compile('<h5.style="font.+?>(.+?)</h5>',re.S)
            # 获得通知group
            title = re.findall(pattern,content)
            return title
        except urllib2.URLError, e:
            if hasattr(e,'code'):
                print e.code
                return None
            if hasattr(e,"reason"):
                print e.reason
                return None
        except:
            print "暂无".decode('utf-8').encode('gbk')
            return None

    def main(self):
        # print self.getPage(self.url)
        title = self.getPage
        InfoName = self.InfoName
        url = self.url
        # 如果返回的是正数即正常，0为异常
        if self.mysql.insertData(self.InfoName,title,url):
            print "保存通知到数据库成功"
        else:
            print "保存到数据库失败"
        
            
hah = GDPU()
hah.main()