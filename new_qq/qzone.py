
import urllib
import qq.encryp_and_hash.getACSRFToken as getACSRFToken

class qzone():
    def __init__(self, qq):
        self.qq = qq

    def dispose_shuoshuo(self, content):
        url = 'http://qz.qq.com/cgi-bin/mobile_update_mood'
        gt = getACSRFToken.getACSRFToken(self.qq)
        gt_k = 'g_tk=' + str(gt.getACSRFToken('skey')) + '&g_ltk=' + str(gt.getACSRFToken('lskey'))
        url += '?' + gt_k
        referer = 'http://qz.qq.com/'+'1063918489'+'/fic/'
        data = 'con='+urllib.quote(content)+'&suin='+'1063918489'+'&reply=0&' + gt_k
        return self.qq.request(url, referer = referer, data = data)

    def comment_shuoshuo(self, uin, content):
        param = 't1_source=1&t1_uin=639431633&t1_tid=d1f31c26f97a6e51ca210700&signin=0&sceneid=0'
        param = 't1_source=1&t1_uin=1063918489&t1_tid=991b6a3f49ce70519f5a0100&signin=0&sceneid=0'
        param = 't1_source=1&t1_uin=2426400798&t1_tid=1ef09f904dce7051ad9b0c00&signin=0&sceneid=0'
        param = urllib.quote(param)
        gt = getACSRFToken.getACSRFToken(self.qq)
        url = 'http://taotao.qq.com/cgi-bin/emotion_cgi_re_feeds?g_tk=' + str(gt.getACSRFToken('skey'))
        data = 'ouin=1063918489\
                &content='+urllib.quote(content)+'\
                &param='+param+'\
                &reqref=feeds\
                &feedversion=1\
                &g_tk='+str(gt.getACSRFToken('skey'))+'\
                &qzreferrer=http%3A%2F%2Fqz.qq.com%2F1063918489%2Ffic%2F'
        return self.qq.request(url, data = data)


