# -*- coding: utf-8 -*-
'''
代理模块
'''
from settings import DL_URL,TEST_CZW,TEST_QCTSW,TIMEOUT,HEADERS
from db import Redis
import requests


def get_proxy():
    try:
        proxys = get_proxy_text(DL_URL)
        proxy_request = {'http': proxys}

        response_czw = test_czw(proxy_request)
        response_qctsw = test_qctsw(proxy_request)
        if response_czw == '200' or response_qctsw == '200':
            print('代理：申请→测试→可用')
            return Redis().insert(proxys)
        else:
            print('代理：申请→测试→重新申请')
            Redis().remove('proxies',proxys)
            return get_proxy()
    except:
        return get_proxy()

def test_czw(proxys):
    try:
        response = requests.get(TEST_CZW, headers=HEADERS, proxies=proxys, timeout=TIMEOUT)
        if response.status_code == 200:
            return '200'
        else:
            return 'error'
    except:
        return 'error'

def test_qctsw(proxys):
    try:
        response = requests.get(TEST_QCTSW, headers=HEADERS, proxies=proxys, timeout=TIMEOUT)
        if response.status_code == 200:
            return '200'
        else:
            return 'error'
    except:
        return 'error'

def get_proxy_text(url):
    try:
        response = requests.get(url,timeout=TIMEOUT)
        if response.status_code == 200:
            return response.text
        else:
            return get_proxy_text(url)
    except:
        return get_proxy_text(url)