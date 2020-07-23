# encoding=utf8
import os
import helper


# 插入垃圾代码
def start(pathname):
    if (os.path.exists(pathname) == False):
        return

    if ('.swift' in pathname):

        cleanCode(pathname, '//---code_s---', '//---code_e---')
        cleanCode(pathname, '//---import_s---', '//---import_e---')
        # 判断类是否已经存在init方法。
        # isInit = classHasInit(pathname)
        isInit = False
        # 读取模板内容
        with open('./temple/temple.swift') as f:
            temples = f.readlines()
            if isInit == True:
                temples = removeCodeWithAry(
                    temples, '---init_s---', '---init_e---')

            data = ""
            for str in temples:
                data = data + str

        newData = replaceInputData(data, "th_1")
        newData = replaceInputData(newData, "th_2")

        insertCodeToFile(pathname, newData)


# 替换字符串。
def replaceInputData(data, str):
    return data.replace(str, helper.getJsonFileRandomString())


def classHasInit(path):
    if '+' in path:
        return True
    with open(path, "r", encoding="utf-8") as f:
        has = False
        f_list = f.readlines()
        for ll in f_list:
            if ("instancetype" in ll) \
                    or ("(id)init" in ll) \
                    or (")load" in ll) \
                    or ("runtime" in ll) \
                    or ("runtime" in ll) \
                    or "initialize" in ll:
                has = True
                break
    return has


# 移除上一次插入的垃圾代码
def cleanCode(path, tag1, tag2):
    with open(path, "r", encoding="utf-8") as f:
        f_list = f.readlines()
        f_list = removeCodeWithAry(f_list, tag1, tag2)
        # 清除换行符。
        e_index = 0
        b_index = 0
        for i in range(len(f_list) - 1, -1, -1):
            # print(f_list[i])
            str = f_list[i]
            if "@end" in str:
                e_index = i
            if ("}" in str) or ("*/" in str) or ("//" in str) or (len(str) > 0):
                b_index = i
                break

        del f_list[b_index + 1:e_index]
        newstr = ""
        for nl in f_list:
            newstr = newstr + nl

        with open(path, 'w', encoding="utf-8") as f:
            f.write(newstr)


# 插入代码到文件。
def insertCodeToFile(path, code):

    if (os.path.exists(path) == False):
        return
    with open(path, "r", encoding="utf-8") as f:
        fileList = f.readlines()

        # 寻找插入的行数，以 swift以 } 结尾
        getline = 0
        line = 0
        for l in fileList:
            line = line + 1
            if "}" in l:
                getline = line

        if getline == 0:
            return
        fileList.insert(getline - 1, code)
        newstr = ""
        for nl in fileList:
            newstr = newstr + nl

    with open(path, 'w', encoding="utf-8") as f:
        f.write(newstr)


# 根据标识，移除数组中的元素。
def removeCodeWithAry(ary, tag1, tag2):
    # 开始的下标
    s_index = 0
    # 结束的下标
    e_index = 0
    for i in range(0, len(ary), 1):
        str = ary[i]

        if tag1 in str:
            s_index = i
        if tag2 in str:
            e_index = i
            break

    # print(s_index, e_index)
    if e_index != 0:
        del ary[s_index:e_index + 1]

    return ary
