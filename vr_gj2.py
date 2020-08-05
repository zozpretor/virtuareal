import sqlite3
import requests
import time

vrinf = [{'name':"Eine", 'uid':421267475, 'fan_uid':"Eine_fan_uid", 'fan_name':"Eine_fan_name"},
         {'name':"Ruki", 'uid':420249427, 'fan_uid':"Ruki_fan_uid", 'fan_name':"Ruki_fan_name"},
         {'name':"Ichigo", 'uid':434341786, 'fan_uid':"Ichigo_fan_uid", 'fan_name':"Ichigo_fan_name"},
         {'name':"Nana7mi", 'uid':434334701, 'fan_uid':"Nana7mi_fan_uid", 'fan_name':"Nana7mi_fan_name"},
         {'name':"Guangyi", 'uid':434401868, 'fan_uid':"Guangyi_fan_uid", 'fan_name':"Guangyi_fan_name"},
         {'name':"Muri", 'uid':455916618, 'fan_uid':"Muri_fan_uid", 'fan_name':"Muri_fan_name"},
         {'name':"Hano", 'uid':455965041, 'fan_uid':"Hano_fan_uid", 'fan_name':"Hano_fan_name"},
         {'name':"Waku", 'uid':472877684, 'fan_uid':"Waku_fan_uid", 'fan_name':"Waku_fan_name"},
         {'name':"nyatsuki", 'uid':472821519, 'fan_uid':"nyatsuki_fan_uid", 'fan_name':"nyatsuki_fan_name"},
         {'name':"plus", 'uid':472845978, 'fan_uid':"plus_fan_uid", 'fan_name':"plus_fan_name"},
         {'name':"miki", 'uid':477317922, 'fan_uid':"miki_fan_uid", 'fan_name':"miki_fan_name"},
         {'name':"Hoshimi", 'uid':477342747, 'fan_uid':"Hoshimi_fan_uid", 'fan_name':"Hoshimi_fan_name"},
         {'name':"mahiru", 'uid':477306079, 'fan_uid':"mahiru_fan_uid", 'fan_name':"mahiru_fan_name"},
         {'name':"Aza", 'uid':480680646, 'fan_uid':"Aza_fan_uid", 'fan_name':"Aza_fan_name"},
         {'name':"bamu", 'uid':480675481, 'fan_uid':"bamu_fan_uid", 'fan_name':"bamu_fan_name"},
         {'name':"Tabibito", 'uid':474369808, 'fan_uid':"Tabibito_fan_uid", 'fan_name':"Tabibito_fan_name"},
         {'name':"Roi", 'uid':480745939, 'fan_uid':"Roi_fan_uid", 'fan_name':"Roi_fan_name"},
         {'name':"seiya", 'uid':319810877, 'fan_uid':"seiya_fan_uid", 'fan_name':"seiya_fan_name"},
         {'name':"Saya", 'uid':490331391, 'fan_uid':"Saya_fan_uid", 'fan_name':"Saya_fan_name"},
         {'name':"Yukie", 'uid':56748733, 'fan_uid':"Yukie_fan_uid", 'fan_name':"Yukie_fan_name"},
         {'name':"Karu", 'uid':370687588, 'fan_uid':"Karu_fan_uid", 'fan_name':"karu_fan_name"},
         {'name':"Shiki", 'uid':370687372, 'fan_uid':"Shiki_fan_uid", 'fan_name':"Shiki_fan_name"},
         {'name':"Pax", 'uid':370688671, 'fan_uid':"Pax_fan_uid", 'fan_name':"Pax_fan_name"},
         {'name':"Samael", 'uid':370689210, 'fan_uid':"Samael_fan_uid", 'fan_name':"Samamel_fan_name"},
         {'name':"Chaos", 'uid':628292881, 'fan_uid':"Chaos_fan_uid", 'fan_name':"Chaos_fan_name"},
         {'name':"Kiyaro", 'uid':558070436, 'fan_uid':"Kiyaro_fan_uid", 'fan_name':"Kiyaro_fan_name"},
         {'name':"Chiharu", 'uid':558070433, 'fan_uid':"Chiharu_fan_uid", 'fan_name':"Chiharu_fan_name"}]

def start():
    global conn
    conn = sqlite3.connect('vr2.db')

def creatup(upinf={}):
    global conn
    command = "create table if not exists "+upinf['name']+"(" +upinf['fan_uid']+" int UNIQUE, "+\
    upinf['fan_name']+" varchar)"
    conn.execute(command)
    conn.commit()

def funcup(upinf={}):
    if upinf == {}:
        return
    fan_list = []
    i = 0
    ref_url = "https://space.bilibili.com/" + str(upinf['uid']) + "/fans/fans"
    head = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'api.bilibili.com',
        'Pragma': 'no-cache',
        'referer': ref_url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                      'Chrome/84.0.4147.105 Safari/537.36'
    }
    while 1:
        i += 1
        if i >= 6:
            break
        url = "https://api.bilibili.com/x/relation/followers?vmid=" + str(upinf['uid']) + \
              "&pn=" + str(i) + "&ps=20&order=desc&jsonp=jsonp&callback=__jp16"
        try:
            r = requests.get(url, headers=head, timeout=10).text
            r2 = eval(r[6:].replace('null', 'None'))
            list1 = r2['data']['list']
            if list1 == []:
                break
            else:
                for fan in list1:
                    fan_list.append([fan["mid"], fan["uname"]])
        except Exception as e:
            print(e)
    if fan_list != []:
        saveup(fan_list, upinf)

def saveup(fan_list=[],upinf={}):
    global conn
    if fan_list == [] or upinf == {}:
        print("save error!")
        return
    command1 = "insert into "+upinf['name']+"("\
               + upinf['fan_uid']+","+upinf['fan_name']+") values (?,?)"
    for row in fan_list:
        try:
            conn.execute(command1, row)
        except Exception as e:
            print(e)
            print("insert error!")
            conn.rollback()
    conn.commit()

if __name__ == "__main__":
    start()
    for row in vrinf:
        creatup(row)
        funcup(row)
    conn.close()