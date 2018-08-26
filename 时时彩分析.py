import re
import urllib.request
proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
url = "http://chart.cp.360.cn/kaijiang/kaijiang?lotId=255401&spanType=2&span="
get=urllib.request.urlopen(url).read()
get=get.decode("gbk","ignore")
ge=re.findall(r'<td class=\'red big\'>(.*?)</td>',get)
s=ge[-1]+ge[-2]+ge[-3]+ge[-4]+ge[-5]
w=""
for j in ge:
    w=w+j
w=re.sub("\D","",w)
for i in set(w):
    if w.count(i) >= 1:
        print('%s 今天总计出现了%d 次!'%(i, w.count(i)))
a={
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    0:0,
}
c={
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    0:0,
}
for i in ge:
    for b in range(10):
        if(b == int(i[4])):
            c[b]+=1
for i in ge:
    for b in range(10):
        if(b == int(i[3])):
            a[b]+=1
print("一星")
print(c)
print("二星")
print(a)
for i in range(10):
    if str(i) in s:
        ++1
    else:
        print("推荐购买%s",i)
print("当前开奖号码",ge[-1])














