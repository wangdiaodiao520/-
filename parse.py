# -*- coding: utf-8 -*-
'''
解析模块
'''
from lxml import etree
from settings import QCTSW,CZW_T,CZW,QCTSW_T


class Parse():
    def __init__(self,response):
        self.response = response

    def parse(self):
        if type(self.response).__name__ == 'str':
            return self.response
        else:pass
        if CZW in self.response.text:
                result = self.czw()
                return result
        elif QCTSW in self.response.text:
            result = self.qctsw()
            return result


    def czw(self):
        html = etree.HTML(self.response.text)
        if CZW_T in ''.join(html.xpath('//head/title/text()')):
            trs = html.xpath('//table/tr')[1:]
            tss_list = []
            for tr in trs:
                ts = tr.xpath('td//text()')
                ts[7] = ''.join(tr.xpath('td[@class="tsjs"]/a/@href'))
                ts[0] = 'czw' + ts[0]
                tss_list.append(ts)
            return tss_list
        else:
            html = etree.HTML(self.response.content.decode('gb2312', 'ignore'))
            ms = ''.join(html.xpath('//div[@class="tsnr"]/p[last()]/text()')).replace('\r\n','')
            return ms

    def qctsw(self):
        html = etree.HTML(self.response.text)
        if QCTSW_T in ''.join(html.xpath('//head/title/text()')):
            trs = html.xpath('//table/tr')[1:]
            tss_list = []
            for tr in trs:
                cj_id = ''.join(tr.xpath('td[position()=1]/text()'))
                js = ''.join(tr.xpath('td[position()=2]/@title')).replace("'","")
                cj = ''
                cx = ''
                nk = ''
                bqs = []
                fixs = tr.xpath('td[position()=3]//span[@class="fix"]')
                for fix in fixs:
                    if fix.xpath('a[@class="problemTypeName"]'):
                        bq = ''.join(fix.xpath('a[@class="problemType"]/text()')) + '#' +''.join(fix.xpath('a[@class="problemTypeName"]/text()'))
                    else:
                        bq = '服务问题' + '#' +''.join(fix.xpath('a[@class="problemType"]/text()'))
                    bqs.append(bq)
                bqs = ','.join(bqs)
                sj = ''.join(tr.xpath('td[position()=4]/text()')).split(' ')[0]
                url = 'http://www.qctsw.com' + ''.join(tr.xpath('td[position()=2]/a/@href'))
                tss_list.append([cj_id,cj,cx,nk,js,bqs,sj,url])
            return tss_list
        else:
            ms = ''.join(html.xpath('//div[@class="articleContent"]/p//text()')).replace('\r\n','').replace('\t','')
            nk = ''.join(html.xpath('//table/tr[position()=2]/td[position()=2]/text()')).replace('\r\n','').replace('\t','')
            cj = ''.join(html.xpath('//table/tr[position()=1]/td[position()=2]/a[position()=1]/text()')).replace('\r\n','').replace('\t','')
            cx = ''.join(html.xpath('//table/tr[position()=1]/td[position()=2]/a[position()=2]/text()')).replace('\r\n','').replace('\t','')
            return ms + '###' + nk + '###' + cj + '###' + cx




