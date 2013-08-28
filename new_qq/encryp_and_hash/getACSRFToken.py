'''
	getACSRFToken: function(type) {
		var hash = 5381,
			str = QFM.cookie.get(type);
		for (var i = 0, len = str.length; i < len; ++i) {
			hash += (hash << 5) + str.charAt(i).charCodeAt();
		}
		return hash & 0x7fffffff;
	},
'''

class getACSRFToken:
    def __init__(self, qq):
        self.qq = qq

    def getACSRFToken(self, name):
        ret = 5381
        string = self.qq.getCookie(name)
        if string is None:
            return ret & 0x7fffffff

        for i in xrange(len(string)):
            ret += (ret << 5) + ord(string[i])
        return ret & 0x7fffffff
