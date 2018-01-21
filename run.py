# -*- coding=utf-8 -*-
from init import login, select_ticket_info
from wechat import *

select = select_ticket_info.Select(file_helper, friend)
command = """command:
1 停止抢票
2 开始抢票
3 [from station, to station] 增加站点
4 [from station, to station] 删除站点
5 [K012, G10]  增加车次
6 [K012, G10] 移除车次
7 [2018-01-01] 增加日期
8 [2018-01-01] 删除日期
9 显示所订站点
10 显示所订日期
11 显示所订车次
12 显示已查询多少次
"""


@bot.register(friend, TEXT)
def wechat_command(msg):

    if msg.text == "1":
        select.stop = True
    elif msg.text == "2":
        select.stop = False
    elif msg.text == "12":
        friend.send("已经查询 {0} 次".format(select.total_num))
    elif msg.text == "9":
        friend.send("from: {0}, to: {1}".format(" ".join(select.from_station), " ".join(select.to_station)))
    elif msg.text == "10":
        friend.send("{0}".format(",".join(select.station_date)))
    elif msg.text == "11":
        friend.send("{0}".format(",".join(select.station_trains)))
    elif msg.text.startswith("3"):
        st = msg.text.lstrip("3", "").replace("[", "").replace("]", "").strip().split(",")
        if len(st) == 2:
            f_st = st[0].strip()
            t_st = st[1].strip()
            select.from_station.append(f_st)
            select.to_station.append(t_st)
            friend.send("from: {0}, to: {1}".format(" ".join(select.from_station), " ".join(select.to_station)))
    elif msg.text.startswith("4"):
        st = msg.text.lstrip("4", "").replace("[", "").replace("]", "").strip().split(",")
        if len(st) == 2:
            f_st = st[0].strip()
            t_st = st[1].strip()
            select.from_station.remove(f_st)
            select.to_station.remove(t_st)
            friend.send("from: {0}, to: {1}".format(" ".join(select.from_station), " ".join(select.to_station)))
    elif msg.text.startswith("5"):
        map(lambda x: select.station_trains.append(x.strip()),
            msg.text.lstrip("5", "").replace("[", "").replace("]", "").strip().split(","))
        friend.send("{0}".format(",".join(select.station_trains)))
    elif msg.text.startswith("6"):
        map(lambda x: select.station_trains.remove(x.strip()),
            msg.text.lstrip("6", "").replace("[", "").replace("]", "").strip().split(","))
        friend.send("{0}".format(",".join(select.station_trains)))
    elif msg.text.startswith("7"):
        map(lambda x: select.station_date.append(x.strip()),
            msg.text.lstrip("7", "").replace("[", "").replace("]", "").strip().split(","))
        friend.send("{0}".format(",".join(select.station_date)))
    elif msg.text.startswith("8"):
        map(lambda x: select.station_date.remove(x.strip()),
            msg.text.lstrip("8", "").replace("[", "").replace("]", "").strip().split(","))
        friend.send("{0}".format(",".join(select.station_date)))
    else:
        friend.send(command)

def run():

    login.main()
    select.main()

run()