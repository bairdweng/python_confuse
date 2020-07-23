# python混淆

### 功能说明

 * 对类，函数，变量进行自动混淆。
 * 自动往函数插入垃圾代码，往类插入垃圾代码
 * 垃圾代码更加自然，仿佛不是那么垃圾。
 * 对字符串自动进行AES加密。
* 注意事项
* 所有需要混淆的函数以及变量增加hx_

### 开始

```js
python3 index.py xcode项目路径
```

### AES字符串加密

在项目的根目录下创建文件 aes_config.json

```js
[{
    "filePath": "BoxConfusion/Box/BxKeyManage.swift",// 类的相对路径
    "ivkey": "aaaaaaaaaaaaaaaa",// 原本加密的key，python将自动替换
     // 所有需要加密的字符串列表
    "keys": [
        "key1",
        "key2"
    ]
}]
```





