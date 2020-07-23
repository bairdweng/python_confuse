from Crypto.Cipher import AES
import base64
import helper
import re
import json
class aescrypt():
    def __init__(self,key,model,iv,encode_):
        self.encode_ = encode_
        self.model =  {'ECB':AES.MODE_ECB,'CBC':AES.MODE_CBC}[model]
        self.key = self.add_16(key)
        if model == 'ECB':
            self.aes = AES.new(self.key,self.model) #创建一个aes对象
        elif model == 'CBC':
            self.aes = AES.new(self.key,self.model,iv) #创建一个aes对象

        #这里的密钥长度必须是16、24或32，目前16位的就够用了

    def add_16(self,par):
        par = par.encode(self.encode_)
        while len(par) % 16 != 0:
            par += b'\x00'
        return par

    def aesencrypt(self,text):
        text = self.add_16(text)
        self.encrypt_text = self.aes.encrypt(text)
        return base64.encodebytes(self.encrypt_text).decode().strip()

    def aesdecrypt(self,text):
        text = base64.decodebytes(text.encode(self.encode_))
        self.decrypt_text = self.aes.decrypt(text)
        return self.decrypt_text.decode(self.encode_).strip('\0')

# 字符串的AES加密    
def run(pro_root_dir):

    with open (pro_root_dir + 'aes_config.json') as f:
        list = json.loads(f.read())
        for config in list:
            runConfig(pro_root_dir,config)
 



def runConfig(pro_root_dir,dic):
    # 获取16位的加密key 
    ivKey = helper.getRandomStrWithOption(16, -1)
    with open (pro_root_dir + 'aes_config.json') as f:
        filePath = pro_root_dir + dic["filePath"]
        enStrs = dic["keys"]
        oldIvKey = dic["ivkey"]
        print(oldIvKey)
    # 加密的类
    pr = aescrypt(ivKey,'ECB','','utf-8')
    with open(filePath, "r", encoding="utf-8") as f:
        content = f.read()
        # 替换key
        content = re.sub(r'\b' + oldIvKey + r'\b', ivKey, content)
        # 加密列表的字符串
        for str in enStrs:
            enStr = pr.aesencrypt(str)
            content = re.sub(r'\b' + str + r'\b', enStr, content)                           
    with open(filePath, "w", encoding="utf-8") as f:
        f.write(content)
    
    for str in enStrs:
        enStr = pr.aesencrypt(str)
        print("加密前："+str,"加密后："+enStr)   
