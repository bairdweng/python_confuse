# -*- coding: UTF-8 -*-
import json
import os
with open("./temple/cihui.txt") as f:
    list = f.read().split('\n')
    newlist = []
    for w in list:
        if w.isalpha():
            newlist.insert(0, w)

    jsonStr = json.dumps(newlist)

    with open("./temple/dc.json", 'w') as ff:

        ff.write(jsonStr)
