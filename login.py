#coding=utf-8

import urllib2
import urllib
import httplib2
import re
import random
from encryption import QQmd5
import cookielib
import requests

class HTTPRefererProcessor(urllib2.BaseHandler):
    def __init__(self):
        self.referer = None

    def http_request(self, request):
        if ((self.referer is not None) and not request.has_header("Referer")):
            request.add_unredirected_header("Referer", self.referer)

        return request

    def http_response(self, request, response):
        self.referer = response.geturl()
        return response

    https_request = http_request
    https_response = http_response

class webqq:
    def __init__(self):
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(
                urllib2.HTTPHandler(),
                urllib2.HTTPSHandler(),
                urllib2.HTTPCookieProcessor(self.cookies),
                HTTPRefererProcessor(),
                )
        urllib2.install_opener(self.opener)
        #response, content = httplib2.Http().request('http://ui.ptlogin2.qq.com/cgi-bin/login?target=self&style=5&mibao_css=m_webqq&appid=1003903&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fweb.qq.com%2Floginproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20121029001')
        req = urllib2.urlopen('https://ui.ptlogin2.qq.com/cgi-bin/login?target=self&style=5&mibao_css=m_webqq&appid=1003903&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fweb.qq.com%2Floginproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20121029001',)
        #s = requests.Session()
        #req = s.get('https://ui.ptlogin2.qq.com/cgi-bin/login?target=self&style=5&mibao_css=m_webqq&appid=1003903&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fweb.qq.com%2Floginproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20121029001')
        safecode = re.search(r'(var g_login_sig=")(.*?)(")', req.read())
        self.login_sig = safecode.group(2)
        print self.login_sig
        cs = ['%s=%s' %  (c.name, c.value) for c in self.cookies]
        cookies = ";".join(cs)
        print cookies
        #self.check_url = "https://ssl.ptlogin2.qq.com/check?uin=1063918489@qq.com&appid=1003903&js_ver=10015&js_type=0&login_sig=" + str(self.login_sig)  +"&u1=http%3A%2F%2Fweb.qq.com%2Floginproxy.html&r=" +  str(random.random()) + "3"
        self.check_url = 'https://ssl.ptlogin2.qq.com/check?uin=1063918489@qq.com&appid=1003903&js_ver=10015&js_type=0&login_sig=0IHP3T5GHFoOnsSLE-98x9hy4UaQmPVu*8*OdGl5vyereLcB8Fk-y3TS6C3*7E8-&u1=http%3A%2F%2Fweb2.qq.com%2Floginproxy.html&r=0.17657850333489478'
        req = urllib2.Request(self.check_url, )
        cookies = 'chkuin=1063918489; ptcz=7ad41d29d64ef54136bddfb56d284fb924727d4a50e5dcf46658243119e345de; uikey=bc342ce0ebff88ac6b134591016e6fd7239fa56553e63e59542281c7ad027551; ptvfsession=579d4a0c554d235514f55f544d14673adce3f96931cb27b7b600a09d612b19b473bfa273d520d904648969080526e5b2; confirmuin=1063918489;verifysession=h00944004bc43ce0585685c5db1a0b8b8e900bf8a1083594a50567b5292b6b06c2481a6ee230960f4c3852f2fe07dd7eae0; ptui_loginuin=1063918489@qq.com; pt2gguin=o1063918489; uin=o1063918489; skey=@fmTaos21G; ETK=; ptuserinfo=4841434b4552; qm_sid=d7a9fc6253cdd0b60c5856f705e21cbc,1QGZtVGFvczIxRw..; qm_username=1063918489; ptisp=edu; pgv_pvid=9552673461; pgv_info=pgvReferrer=&ssid=s4396479120'
        req.add_header("Cookie", cookies)
        req = urllib2.urlopen(req)
        verifycode = re.search(r"'(\d)','(.+)','(.+)'", req.read())
        self.verifycode1 = verifycode.group(2)
        self.verifycode2 = verifycode.group(3)
        print self.verifycode1, self.verifycode2
        cookies = 'chkuin=1063918489; ptcz=7ad41d29d64ef54136bddfb56d284fb924727d4a50e5dcf46658243119e345de; uikey=bc342ce0ebff88ac6b134591016e6fd7239fa56553e63e59542281c7ad027551; verifysession=h00944004bc43ce0585685c5db1a0b8b8e900bf8a1083594a50567b5292b6b06c2481a6ee230960f4c3852f2fe07dd7eae0; pt2gguin=o1063918489; uin=o1063918489; skey=@fmTaos21G; ETK=; ptuserinfo=4841434b4552; qm_sid=d7a9fc6253cdd0b60c5856f705e21cbc,1QGZtVGFvczIxRw..; qm_username=1063918489;ptisp=edu; pgv_pvid=9552673461; pgv_info=pgvReferrer=&ssid=s4396479120; chkuin=1063918489; ptcz=7ad41d29d64ef54136bddfb56d284fb924727d4a50e5dcf46658243119e345de; uikey=bc342ce0ebff88ac6b134591016e6fd7239fa56553e63e59542281c7ad027551; verifysession=h00944004bc43ce0585685c5db1a0b8b8e900bf8a1083594a50567b5292b6b06c2481a6ee230960f4c3852f2fe07dd7eae0; pt2gguin=o1063918489; uin=o1063918489; skey=@fmTaos21G; ETK=; ptuserinfo=4841434b4552;qm_sid=d7a9fc6253cdd0b60c5856f705e21cbc,1QGZtVGFvczIxRw..; qm_username=1063918489; ptisp=edu; pgv_pvid=9552673461; pgv_info=pgvReferrer=&ssid=s4396479120; '
        cs = ['%s=%s' %  (c.name, c.value) for c in self.cookies]
        cookies += ";" "; ".join(cs)
        print cs

        login_url = 'https://ssl.ptlogin2.qq.com/login?u=1063918489@qq.com&p=' + str(QQmd5().md5_2('密码', self.verifycode1, self.verifycode2)) + '&verifycode=' + self.verifycode1 + '&webqq_type=10&remember_uin=1&login2qq=1&aid=1003903&u1=http%3A%2F%2Fweb.qq.com%2Floginproxy.html%3Flogin2qq%3D1%26webqq_type%3D10&h=1&ptredirect=0&ptlang=2052&from_ui=1&pttype=1&dumy=&fp=loginerroralert&action=2-14-32487&mibao_css=m_webqq&t=1&g=1&js_type=0&js_ver=10015&login_sig=0IHP3T5GHFoOnsSLE-98x9hy4UaQmPVu*8*OdGl5vyereLcB8Fk-y3TS6C3*7E8-'
        req = urllib2.Request(login_url)
        req.add_header("Referer", "https://ui.ptlogin2.qq.com/cgi-bin/login?target=self&style=5&mibao_css=m_webqq&appid=1003903&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fweb.qq.com%2Floginproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20121029001")
        req.add_header("Cookie", cookies)
        self.opener.addheaders.append(("Cookie", cookies))
        req = urllib2.urlopen(req)
        #req = s.get(login_url, cookies = req.cookies)
        print req.read()
        for cookie in self.cookies:
            print cookie.name, ":",  cookie.value

        print urllib2.urlopen('http://web2.qq.com/web2/get_msg_tip?uin=&tp=1&id=0&retype=1&rc=0&lv=3&t=1358252543124').read()

if __name__ == "__main__":
    qq = webqq()

