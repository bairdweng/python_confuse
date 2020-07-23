import os
import helper
import random

def start(pathname):
    if (os.path.exists(pathname) == False):
        return
    if ('.swift' in pathname):
        # 判断是否是方法。
        with open(pathname) as f:
            temples = f.readlines()
                 # 寻找插入的行数，以 swift以 } 结尾
            getline = 0
            line = 0
            for ll in temples:
                line = line + 1
                # 匹配函数
                if "func" in ll and "{" in ll and ("}" in ll) == False:
                    getline = line
                    temples.insert(getline,getCode())
                    print("--------",ll)
            newstr = ""
            for nl in temples:
               newstr = newstr + nl

        with open(pathname, 'w', encoding="utf-8") as f:
             f.write(newstr)       



def getCode():
      index = random.randint(1, 6)
      indexStr = '%d'%index
      fileName = './temple/func/funcTemple'+indexStr+'.swift'
      with open(fileName) as f:
          temples = f.readlines()
          data = ""
          for str in temples:
            data = data + str
          newData = replaceInputData(data, "str1")
          newData = replaceInputData(newData, "str2")
          newData = replaceInputData(newData, "str3")
          newData = replaceInputData(newData, "str4")
          newData = replaceInputData(newData, "str5")
          newData = replaceInputData(newData, "str6")
      return newData

# 替换字符串。
def replaceInputData(data, str):
    return data.replace(str, helper.getJsonFileRandomString())