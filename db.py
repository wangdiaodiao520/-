# -*- coding: utf-8 -*-
'''
数据库模块
'''
import pymysql
import redis
from settings import HOST,PORT_SQL,PORT_REDIS,USER_SQL,PD_SQL,PD_REDIS,TEXT,DB_SQL,SHEET_ONE,SHEET_TWO
from czwjson import CZWJSON
from warnings import filterwarnings
filterwarnings("error",category=pymysql.Warning)



class Sql():
    def __init__(self):
        self.db = pymysql.connect(host=HOST, port=PORT_SQL, user=USER_SQL, password=PD_SQL, db=DB_SQL, charset='utf8')
        self.cursor = self.db.cursor()

    def trans(self,data):
        bqs = data[5].strip(',').split(',')
        wts = []
        for bq in bqs:
            if len(bq) > 0:
                for i in CZWJSON:
                    if i['value'] == bq[0]:
                        name = i['name']
                        for item in i['items']:
                            if item['id'] == int(bq[1:]):
                                wt = item['title']
                                wts.append(name + '#' + wt)
                            else:pass
                    else:pass
            else:pass
        data[5] = ','.join(wts)
        return data

    def insert(self,data):
        if 'QT' in data[0]:
            sheet = SHEET_ONE
        elif 'czw' in data[0]:
            sheet = SHEET_TWO
        else:pass
        if 'QT' in data[0]:
            data_parse = data[7].split('###')
            data[7] = data_parse[0]
            data[3] = data_parse[1]
            data[1] = data_parse[2]
            data[2] = data_parse[3]
            print('保存id为' + data[0] + '汽车投诉网的数据')
        else:
            data = self.trans(data)
            print('保存id为' + data[0] + '车质网的数据')
        SQL = TEXT.format(sheet,data[0], data[1], data[2], data[3], pymysql.escape_string(data[4]), pymysql.escape_string(data[5]), data[6],
                          pymysql.escape_string(data[7]))
        SQL_T = TEXT.format(sheet,data[0], data[1], data[2], data[3], pymysql.escape_string(data[4]), pymysql.escape_string(data[5]), data[6], data[7])
        try:
            self.cursor.execute(SQL)
            self.db.commit()
        except pymysql.Warning:
            print('id为'+data[0]+'的数据已存在')
        except:
            self.cursor.execute(SQL_T)
            self.db.commit()

    def close(self):
        return self.db.close()




class Redis():
    def __init__(self):
        self.redis = redis.StrictRedis(host=HOST,port=PORT_REDIS,password=PD_REDIS,decode_responses=True)

    def remove(self,proxy):
        self.redis.zrem('proxies', proxy)

    def insert(self,proxy):
        return self.redis.set('proxy',proxy)

    def get(self):
        return self.redis.get('proxy')