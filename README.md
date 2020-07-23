# python混淆

* 功能说明

  > * 对类，函数，变量进行自动混淆。
  > * 自动往函数插入垃圾代码，往类插入垃圾代码
  > * 垃圾代码更加自然，仿佛不是那么垃圾。
  > * 对字符串自动进行AES加密。

* 注意事项

  > 所有需要混淆的函数以及变量增加hx_

* 开始混淆

  > ```js
  > python3 index.py xcode项目路径
  > ```

* AES字符串加密

  ```python
  # 字符串的AES加密    
  def runAes():
      # 获取16位的加密key 
      ivKey = helper.getRandomStrWithOption(16, -1)
      # 指定需要进行AES加密的类
      filePath = pro_root_dir + 'BoxConfusion/Box/BxKeyManage.Swift'
      # 所有需要加密的字符串
      enStrs = [
          "idfa",
          "idfv",
          "imei",
          "oaid",
          "androidid",
          "model",
          "device_id",
          "os_type",
          "app_version",
          "os_version",
          "sdk_version",
          "pid",
          "token",
          "appkey",
          "log",
          "ts"
          ]
      # 加密的类
      pr = MyAES.aescrypt(ivKey,'ECB','','utf-8')
      with open(filePath, "r", encoding="utf-8") as f:
          content = f.read()
          # 将类中的key使用16位随机key替换，确保每次生成的字符串都不一样。
          content = re.sub(r'\b' + "aaaaaaaaaaaaaaaa" + r'\b', ivKey, content)
          # 加密列表的字符串
          for str in enStrs:
              enStr = pr.aesencrypt(str)
              content = re.sub(r'\b' + str + r'\b', enStr, content)
   
                                       
      with open(filePath, "w", encoding="utf-8") as f:
          f.write(content)
      
      for str in enStrs:
          enStr = pr.aesencrypt(str)
          print("加密前："+str,"加密后："+enStr)
          
      return
      
  ```

  

  