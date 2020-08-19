# -*- coding: UTF-8 -*-
import os
import re
import shutil
import sys

import helper
import InstercodeToFile
import InstercodeToFunc
import MyAES

# 读取目录
ys_pro_dir = '../confusionExample'
if len(sys.argv) == 2:
   ys_pro_dir = sys.argv[1]
pro_root_dir = ''

# 前缀。
pro_qz_str = helper.getRandomStrWithOption(2, -1).upper()

# 过滤的类。
filterClassNames = ['AppDelegate', 'main']

# 过滤的目录。
filterClassDirs = ['Pods','OpenSource','Controllers']


# 获取类名
def getClassName(name):
    # 类名长度小于4，直接加前缀
    if len(name) < 4:
        return pro_qz_str + name
    # 截取类的前4个字符串    
    else:
        # 截取字符串前两位后的字符串
        str1 = name[2:len(name)]
        str2 = helper.getJsonFileRandomString().lower().capitalize()
        return pro_qz_str + str2 + str1
# 获取函数名称
def getFuncName(name):

    # 移除hx_
    str1 = name[3:len(name)]
    str2 = helper.getRandomStrWithOption(2, -1)
    return str2 + str1


# 获取路径当前的目录名称
def getPathLastDir(path):
    s_dirs = path.split('/')
    last_dir = s_dirs[len(s_dirs) - 1]
    return last_dir


# 开始执行
def start(rootDir):
    global pro_root_dir
    if (os.path.exists(rootDir) == False):
        return
    new_dir = '../templeDir/'
    if (os.path.exists(new_dir)):
        shutil.rmtree(new_dir)

    os.makedirs(new_dir)
    last_dir = getPathLastDir(rootDir)

    shutil.copytree(rootDir, '../templeDir/' + last_dir)

    pro_root_dir = '../templeDir/' + last_dir + '/'
    # AES 加密
    try:
       MyAES.run(pro_root_dir)
    except:
        print("AES加密异常")

    runTask(pro_root_dir)
    # 归档。
    print('==========完成=========')

def runTask(rootDir):
    if (os.path.exists(rootDir) == False):
        return
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        # 判断目录下是否是文件
        if (os.path.isfile(pathname)):
            # .swift的处理
            if '.swift' in filename:
                # 过滤器处理
                isNext = True
                for fix in filterClassNames:
                    if filename == fix + '.swift':
                        isNext = False

                # 过滤加号命名的文件名
                if "+" in filename:
                    isNext = False

                if isNext == False:
                    continue
                # 当前的根目录。        
                rootDir = os.path.dirname(pathname)
                oldFileName = filename.replace('.swift', '')

                newFileName = getClassName(oldFileName)

                # 往函数插入代码
                # InstercodeToFunc.start(pathname)

                # 往类插入代码
                # InstercodeToFile.start(pathname)

                # 更改类名。
                changeClassName(pathname, oldFileName, newFileName)

                # 更改工程。
                changeXcodepro(getXcodeprojPath(pro_root_dir),
                               oldFileName, newFileName)
                # 更改其它类的调用。
                changeFeference(pro_root_dir, oldFileName, newFileName)

                # 混淆后插入swift类路径
                classPath = rootDir + '/' + newFileName + '.swift'

                # 函数混淆
                changeFuncName(pro_root_dir, classPath)

            # .h 跟 .m的处理
            if '.m' in filename:
                # 过滤
                isNext = True
                for fix in filterClassNames:
                    if filename == fix + '.m':
                        isNext = False
                # 过滤加号命名的文件名
                if "+" in filename:
                    isNext = False      
                # 当前的根目录。        
                rootDir = os.path.dirname(pathname)
                # print("file_name",filename)
                # 旧的名称
                oldFileName = filename.replace('.m', '')
                # 判断.h文件是否存在，只有h，m同时存在方可下一步
                h_file_path = rootDir + '/' + oldFileName + '.h'
                if os.path.isfile(h_file_path) == False:
                    isNext = False           

                if isNext == False:
                    continue                         
                # 新的名称
                newFileName = getClassName(oldFileName)
                # 更改类名
                changeClassName(pathname, oldFileName, newFileName)
                # 更改工程
                changeXcodepro(getXcodeprojPath(pro_root_dir),
                               oldFileName, newFileName) 
                # 更改其它类的调用。
                changeFeference(pro_root_dir, oldFileName, newFileName)

                # 混淆后插入OC类路径
                classPath_h = rootDir + '/' + newFileName + '.h'
                classPath_m = rootDir + '/' + newFileName + '.m'
                # 函数名混淆OC
                changeOCFuncName(pro_root_dir, classPath_h)                    
                changeOCFuncName(pro_root_dir, classPath_m)

            # .png 跟 jpg的处理
            if '.png' in filename or '.jpg' in filename or '.jpeg' in filename:
                print("更改图片md5："+filename)
                changeMd5(pathname)
              
        # 重新便利
        else:
            if canNextTastByPath(pathname) == False:
                continue
            runTask(pathname)


# 根据过滤的目录是否继续执行
def canNextTastByPath(pathName):
    isNext = True
    last_dir = getPathLastDir(pathName)
    for dir in filterClassDirs:
        # 过滤目录下的文件
        if dir == last_dir:
            isNext = False
    return isNext

# 修改文件的md5
def changeMd5(path):
    with open(path, "rb") as f:
        # 随机字符串，md5值
        subContent = bytes(helper.getRandomStrWithOption(13, -1),encoding="utf-8")
        fileContent = f.read()
        fileContent = fileContent + subContent
        
    with open(path, "wb") as f:
        f.write(fileContent)


# 更改类名。
def changeClassName(pathname, oldFileName, newFileName):
    # 根目录
    rootDir = os.path.dirname(pathname)
    oldPath = rootDir + '/' + oldFileName
    newPath = rootDir + '/' + newFileName
    if os.path.exists(oldPath + '.h'):
        os.rename(oldPath + '.h', newPath + '.h')
    if os.path.exists(oldPath + '.m'):
        os.rename(oldPath + '.m', newPath + '.m')
    if os.path.exists(oldPath + '.swift'):
        os.rename(oldPath + '.swift', newPath + '.swift')
    if os.path.exists(oldPath + '.xib'):
        os.rename(oldPath + '.xib', newPath + '.xib')    


# 更改工程依赖 
def changeXcodepro(proj_path, oldName, newName):
    with open(proj_path, "r", encoding="utf-8") as f:
        xcontent = f.read()
        xcontent = re.sub(r'\b' + oldName + r'.h\b', newName + '.h', xcontent)
        xcontent = re.sub(r'\b' + oldName + r'.m\b', newName + '.m', xcontent)
        xcontent = re.sub(r'\b' + oldName + r'.xib\b', newName + '.xib', xcontent)
        xcontent = re.sub(r'\b' + oldName + r'.swift\b',
                          newName + '.swift', xcontent)
        # print('混淆:' + oldName + '------------>' + newName)
    with open(proj_path, "w", encoding="utf-8") as f:
        f.write(xcontent)


# 混淆函数名
def changeFuncName(rootDir, filePath):
    with open(filePath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for str in lines:
            try:
                # 函数混淆
                if 'hx_' in str and 'func' in str:
                    funcName = getmidstring(str,'h','(')
                    newFuncName = getFuncName(funcName)
                    # print('函数混淆:' + funcName + '------------>' + newFuncName)
                    changeFuncNameByPro(rootDir, funcName, newFuncName)
                # 变量混淆    
                elif 'hx_' in str and ('var' in str or 'let' in str or 'typealias' in str):
                    if ':' in str:
                        funcName = getmidstring(str,'h',':')
                    else:
                        funcName = getmidstring(str,'h','=')
                    # funcName = getmidstring(str,'h',':')
                    newFuncName = getFuncName(funcName)
                    print('变量混淆:' + funcName + '------------>' + newFuncName)
                    changeFuncNameByPro(rootDir, funcName, newFuncName)
            except:
                  print("异常======",str)   

# 混淆函数名OC
def changeOCFuncName(rootDir, filePath):
    try:  
        with open(filePath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for str in lines:
                try:
                    # 函数混淆
                    if 'hx_' in str and ('-'  in str or '+' in str) and '{':
                        # 截取OC的函数名
                        if ':' in str:
                            funcName = getmidstring(str,'h',':')
                        else:
                            funcName = getmidstring(str,'h','{')
                        # 移除字符串空格
                        funcName = funcName.strip()
                        newFuncName = getFuncName(funcName)
                        # print('函数混淆:' + funcName + '------------>' + newFuncName)
                        changeFuncNameByPro(rootDir, funcName, newFuncName)
                    # 变量混淆  判断行是否是属性或者变量  
                    elif '@property' in str and 'hx_' in str:
                        funcName = getmidstring(str,'h',';')
                        newFuncName = getFuncName(funcName)
                        print('变量混淆:' + funcName + '------------>' + newFuncName)
                        changeFuncNameByPro(rootDir, funcName, newFuncName)
                except:
                    print("异常======",str)  
    except:
        print("无法打开文件")                 


def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start-1:end].strip()
        
# 便利工程目录，混淆函数名
def changeFuncNameByPro(rootDir, funcName, newFuncName):
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if (os.path.isfile(pathname)):
            if '.swift' in pathname or ".xib" in pathname or ".h" in pathname or ".m" in pathname:
                content = ""
                with open(pathname, "r", encoding="utf-8") as f:
                    content = f.read()
                    content = re.sub(r'\b' + funcName +
                                     r'\b', newFuncName, content)
                with open(pathname, "w", encoding="utf-8") as f:
                    f.write(content)
        else:
            if canNextTastByPath(pathname) == False:
                continue
            changeFuncNameByPro(pathname, funcName, newFuncName)


# 更改工程其它类的引用。\b是单词边界 例如 example exampleTest文本，替换example 为 test 最终是 test exampleTest 而不是test testTest
def changeFeference(rootDir, oldName, newName):
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if (os.path.isfile(pathname)):
            # 后缀名
            extName = os.path.splitext(filename)[-1]
            if (extName == '.h') or (extName == '.m') or (extName == '.pch') or (extName == '.swift') or (extName == '.xib'):
                content = ""
                with open(pathname, "r", encoding="utf-8") as f:
                    content = f.read()
                    content = re.sub(r'\b' + oldName + r'\b', newName, content)
                    #OC中.h的处理
                    content = re.sub(r'\b' + oldName + '.h"' + r'\b', '"' + newName + '.h"', content)
                    content = re.sub(r'\b_' + oldName, '_' + newName, content)
                    # content = re.sub('','%s.h ' ,content)
                    #OC中全局变量的处理例如属性example _example
                    # content = re.sub('\\b%s\\b'%oldName,'\\b%s\\b'%newName,content)
                    # content = re.sub('\\b_%s\\b'%oldName,'\\b_%s\\b'%newName,content)
                with open(pathname, "w", encoding="utf-8") as f:
                    f.write(content)
        else:
            # 这里过滤podfile
            last_dir = getPathLastDir(pathname)
            if last_dir == 'Pods':
                continue
            changeFeference(pathname, oldName, newName)


# 获取xcodeproj路径。
def getXcodeprojPath(rootDir):
    x_path = ""
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if '.xcodeproj' in pathname:
            x_path = pathname

    if (len(x_path) > 0):
        x_path = x_path + '/project.pbxproj'
    return x_path


start(ys_pro_dir)
