import requests,re,os
while True:
    kyword=input("输入歌曲名或歌手***回车确认：")
    url="http://songsearch.kugou.com/song_search_v2?callback=jQuery1124006980366032059648_151857518932&keyword="+kyword
    content=requests.get(url).text
    songname=re.findall('"SongName":"(.*?)"',content)
    k=0
    for i in songname:
        k+=1
        print('{0}：{1}'.format(k,i))
    if len(songname)==0:
        print("没有搜索到歌曲，请重新输入")
        content
    else:
        choice=int(input("输入想要下载歌曲前编号***回车确认："))
        files=re.findall('"FileHash":"(.*?)"',content)[choice-1]
        hashurl="http://www.kugou.com/yy/index.php?r=play/getdata&hash="+files
        ha=requests.get(hashurl).text
        play=re.findall('"play_url":"(.*?)"',ha)
        play=''.join(play)
        dow=play.replace("\\","")
        if os.path.exists("d:/music/"):
            pass
        else:
            print("D盘没有music文件，现在已创建用于保存歌曲")
            os.makedirs("d:\\music\\")
        with open("d:\\music\\"+songname[choice-1]+".mp3","wb")as fp:
            try:
                fp.write(requests.get(dow).content)
                print('歌曲：{} 下载成功'.format(songname[choice - 1]))
            except:
                print(songname[choice-1]+" 下载失败")
            fp.close()
        choice=input('是否继续下载（Y/N）：')
        if choice.lower()=='y':
            content
        else:
            break

