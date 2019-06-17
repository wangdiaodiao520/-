# -*- coding: utf-8 -*-
'''
程序配置信息
'''
#请求头信息
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}
#超时设置
TIMEOUT = 3
#代理地址
DL_URL = 'http://localhost:5555/random'
#测试代理地址
TEST_CZW = 'http://www.12365auto.com'
TEST_QCTSW = 'http://www.qctsw.com'
#采集网站开始url
URLS_START = ['http://www.qctsw.com/tousu/tsSearch/0_0_0_0_0_0,0,0,0,0,0_{}.html','http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-{}.shtml']
url = 'http://www.qctsw.com/tousu/tsSearch/0_0_0_0_0_0,0,0,0,0,0_{}.html',
#判断因子
CZW = '12365auto'
QCTSW = 'qctsw'
CZW_T = '汽车质量投诉'
QCTSW_T = '投诉条件查询'
#地址、端口信息
HOST = 'localhost'
PORT_SQL = 3306
PORT_REDIS = 6379
USER_SQL = 'root'
PD_SQL = 'wangyunlong'
PD_REDIS = None
DB_SQL = 'web_test'
#插入语句
TEXT = "INSERT IGNORE INTO {}(ts_id,cj,cx,nk,js,wt,time,ms) VALUES('{}','{}','{}','{}','{}','{}','{}','{}');"
#数据表
SHEET_ONE = 'Complaint'
SHEET_TWO = 'Complaint'
