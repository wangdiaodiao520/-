# -*- coding: utf-8 -*-
'''
请求模块
'''
import requests
from settings import HEADERS,TIMEOUT
from proxy import get_proxy
from db import Redis


#请求类
class Get():
    def __init__(self,url):
        self.head = HEADERS
        self.timeout = TIMEOUT
        self.url = url

    def get(self):
        proxy = Redis().get()
        while not proxy:
            get_proxy()
            proxy = Redis().get()
        proxy_request = {'http': proxy}
        try:
            response = requests.get(self.url,headers=self.head,proxies=proxy_request,timeout=self.timeout)
            if response.status_code == 200:
                return response
            elif response.status_code == 404:
                return '页面资源无法请求到或不存在'
            else:
                print('请求失败，更换代理重新请求')
                #Redis().remove(proxy)
                get_proxy()
                return self.get()
        except:
            print('请求失败，更换代理重新请求')
            #Redis().remove(proxy)
            get_proxy()
            return self.get()
