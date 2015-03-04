#encoding=utf-8

import urllib, urllib2, cookielib, sys  ,time

class YiQiWo(object):
    
    index_page = "http://wap.17wo.cn/Login.action"
    login_page = "http://wap.17wo.cn/Login!process.action"
    login_header = {'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}   
    #mobile = ''
    #password = ''
    #cookie = None
    #cookieFile = './cookie.dat'
    #初始化
    def __init__(self,mobile,pwd):
        self.mobile = mobile
        self.password = pwd
        self.header = {'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        #self.cookie = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(opener)

    #登录
    def login(self):
        postdata = {'mobile':self.mobile,'password':self.password, 'loginType':'0','chkType':'on'}
        postdata = urllib.urlencode(postdata)
        print 'Logining...'
        req = urllib2.Request(url='http://wap.17wo.cn/Login!process.action',data=postdata) 
        result = urllib2.urlopen(req).read()  
        self.cookie.save(self.cookieFile)  

        if '密码' in result:  
            print 'Login failed due to Email or Password error...'  
            sys.exit()  
        else :  
            print 'Login successfully!'
 
    #签到
    def signIn(self):
        #index_page = "http://wap.17wo.cn/Login.action"
        #login_page = "http://wap.17wo.cn/Login!process.action"
        postdata = {'mobile':self.mobile,'password':self.password, 'loginType':'0','chkType':'on'}
        postdata = urllib.urlencode(postdata) 
        print 'signing...'
        req = urllib2.Request(url='http://wap.17wo.cn/SignIn.action?checkIn=true') 
        result = urllib2.urlopen(req).read()  
        self.cookie.save(self.cookieFile)  


    #领取签到成长值    
    def growUp(self):
        print 'growUp...'
        time = time.time()
        time = repr(time)
        s1 = time[0:10]
        s2 = time[11:14]
        time = s1 + s2
        url = "http://wap.17wo.cn/UserCenterGrowup!gainTaskAwards.action?aId=117&taskId=28&_=" + time
        req = urllib2.Request(url=url) 
        result = urllib2.urlopen(req).read()  
        #self.cookie.save(self.cookieFile) 

    #派发红包 领取成长值
    def hongbao(self):
        print 'sedding hongbao...'
        req = urllib2.Request(url='http://wap.17wo.cn/FlowRedPacket!sendFlowRedPacket.action?packetAmount=10&sendFlowValue=10') 
        result = urllib2.urlopen(req).read()  
        req = urllib2.Request(url='http://wap.17wo.cn/UserCenterGrowup!gainTaskAwards.action?aId=117&taskId=36&_=1424850788759')
        result = urllib2.urlopen(req).read()  
        #self.cookie.save(self.cookieFile)

    #领取流量红包 
    def flowbag(self): #领取流量红包 
        print 'receiveing flowbag...'
        req = urllib2.Request(url='http://wap.17wo.cn/FlowRedPacket!LuckDraw.action?pageName=&1730&_=1425262650204')
        result = urllib2.urlopen(req).read()
        print 'receiveing flowbag OK!' 

    #签到后 每日抽奖
    def earnflow(self):
        print '********lottery...*******'
        tmp = 1
        while tmp <= 3:
            req = urllib2.Request(url='http://wap.17wo.cn/FlowRedPacket!LuckDraw.action?pageName=earnflow&_=1425263094369')
            result = urllib2.urlopen(req).read()
            tmp = tmp + 1
            print 'lottery OK!' 


if __name__== '__main__':
        user = YiQiWo('手机','密码')
        user.login()
        user.signIn()
        user.growUp()
        user.hongbao()
        user.earnflow()