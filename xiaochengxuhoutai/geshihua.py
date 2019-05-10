#-*- coding: utf8 -*-
lists=[]
with open(r'C:\Users\houxianzhi\Desktop\新建文本文档1(2).txt','r') as fb:
    data=fb.readlines()
for i in data:
    st=i.strip()
    lists.append(st)
srr='\''+'\',\''.join(lists)+'\''
print(srr)


# sss='陆蓝波/沉诗为骨/懒花噩梦/朝朝捕云草/长歌门班吉拉/满弦/牛牛被踩了'
# ssl=sss.split('/')
# print(ssl)
# sst=','.join(ssl)
# print(sst)
