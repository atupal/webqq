#coding=utf-8

import hashlib

class QQmd5:
    def __init__(self):
        pass
    def md5(self, password = None, verifycode = None):
        return hashlib.md5( (self.__md5_3((password).encode('utf-8')) + (verifycode).upper()).encode('utf-8') ).hexdigest().upper()

    def __md5_3(self, s):
        return hashlib.md5(hashlib.md5(hashlib.md5(s).digest()).digest()).hexdigest().upper()

    def hex_md5hash(self, s):
        return hashlib.md5(s).hexdigest().upper()

    def hexchar2bin(self, uin):
        uin_final = ""
        uin = uin.split('\\x')
        for i in uin[1:]:
            uin_final += chr(int(i, 16))
        return uin_final

    def md5_2(self, pwd, verifyCode1, verifyCode2):
        pwd_1 = hashlib.md5(pwd).digest()
        pwd_2 = self.hex_md5hash(pwd_1 + self.hexchar2bin(verifyCode2))
        pwd_final = self.hex_md5hash(pwd_2 + verifyCode1.upper())
        return pwd_final

if __name__ == '__main__':
    qqmd5 = QQmd5()
    verifycode1 = raw_input("1:")
    verifycode2 = raw_input("2:")
    print qqmd5.md5_2("atupal@qq.com", verifycode1, verifycode2)
