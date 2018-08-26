import requests
import urllib
import json
import os
word = input("请输入歌曲名或者歌手名：")
n=input("请输入希望下载歌曲排行榜多少首:")
res1 = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n='+n+'&w='+word)

jm1 = json.loads(res1.text.strip('callback()[]'))
jm1 = jm1['data']['song']['list']
mids = []
srcs = []
songnames = []
singers = []
for j in jm1:

    try:
        mids.append(j['media_mid'])
        songnames.append(j['songname'])
        singers.append(j['singer'][0]['name'])
    except:
        print('wrong')


for n in range(0,len(mids)):
    res2 = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&jsonpCallback=MusicJsonCallback&cid=205361747&songmid='+mids[n]+'&filename=C400'+mids[n]+'.m4a&guid=6612300644')
    jm2 = json.loads(res2.text)
    vkey = jm2['data']['items'][0]['vkey']
    srcs.append('http://dl.stream.qqmusic.qq.com/C400'+mids[n]+'.m4a?vkey='+vkey+'&guid=6612300644&uin=0&fromtag=66')
print('For '+word+' Start download...')
x = len(srcs)
if os.path.exists("d:/music/"):
    pass
else:
    print("D盘没有music文件，现在已创建用于保存歌曲")
    os.makedirs("d:\\music\\")
for m in range(0,x):
    print(str(m)+'***** '+songnames[m]+' - '+singers[m]+'.m4a *****'+' 正在下载...')
    try:
        print(srcs[m])
        #urllib.request.urlretrieve(srcs[m],'d:/music/'+songnames[m]+' - '+singers[m]+'.m4a')

    except:
        x = x - 1
        print('下载完成~')
print('For ['+word+'] 已下载 '+str(x)+'首歌曲 !保存在D盘music文件夹中')



