# -*- coding: utf-8 -*-
'''
主程序
'''
from requester import *
from settings import URLS_START,CZW,QCTSW
from parse import Parse
from db import Sql
import datetime



sql = Sql
#定义抓取日期界限
def day():
    judge_date = (datetime.date.today()+datetime.timedelta(-3)).strftime("%Y-%m-%d")
    return judge_date
    #return '2019-06-01'

#主程序类
class Spider():
    def __init__(self,url):
        self.url = url

    def spider(self):
        try:
            response = Get(self.url).get()
            result = Parse(response).parse()
            for ts in result:
                if ts[6].strip() == day():
                    ts[7] = Parse(Get(ts[7]).get()).parse()
                    sql().insert(ts)
                    sql().close()
                elif ts[6].strip() > day():
                    ts[7] = Parse(Get(ts[7]).get()).parse()
                    sql().insert(ts)
                    sql().close()
                elif ts[6].strip() < day():
                    break
                else:
                    pass
            return result[-1][6].strip()
        except IndexError:
            with open('log.txt','a') as f:
                f.write(self.url + '\n')
            return '2099-12-31'



if __name__ == "__main__":
    for url_start in URLS_START:
        if CZW in url_start:
            OFFSET = 1
        elif QCTSW in url_start:
            OFFSET = 0
        else:pass
        result = Spider(url_start.format(str(OFFSET))).spider()
        while result >= day():
            OFFSET += 1
            result = Spider(url_start.format(OFFSET)).spider()
