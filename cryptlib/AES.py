# coding: utf-8

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class AESCrypt(object):
    def __init__(self, key):
        count = len(key)
        if count < 16:
            add = (16-count)
            #\0 backspace
            key = key + ('\0' * add)
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self,text):
        print "aaaaaaa", self.key, len(self.key)
        cryptor = AES.new(self.key,self.mode)
        #这里密钥key 长度必须为16（AES-128）,
        #24（AES-192）,或者32 （AES-256）Bytes 长度
        #目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length-count)
            #\0 backspace
            text = text + ('\0' * add)
        elif count > length:
            add = (length-(count % length))
            text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    def decrypt(self,text):
        cryptor = AES.new(self.key,self.mode)
        plain_text  = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')

