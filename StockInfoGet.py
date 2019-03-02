#!/usr/bin/python3

from urllib import parse
import http.client
import json

class StockInfoGet:
    def __init__(self, stockName):
        self.stockName = stockName
        self.parseName = parse.quote(stockName)

    def getInfo(self):
        print("正在获取股票信息 --- " + self.stockName)
        self.httpConnect()
        self.jsonDecode()
        if(self.orgId == None):
            return None, None, None
        return self.orgId, self.code, self.name

    def jsonDecode(self):
        data = json.loads(self.jsonMessage)
        if(len(data) == 0):
            self.orgId = None
            return
        self.orgId = data[0]['orgId']
        self.code = data[0]['code']
        self.name = data[0]['zwjc']

    # 创建http连接  获取Json字符串
    # ！ 去掉 'accept-encoding': "gzip, deflate", 解除加密
    def httpConnect(self):
        conn = http.client.HTTPConnection("www.cninfo.com.cn")

        
        payload = "keyWord=" + self.parseName.lower() + "&maxNum=11"  # 英文字符转换为小写

        headers = {
            'host': "www.cninfo.com.cn",
            'connection': "keep-alive",
            'accept': "application/json, text/javascript, */*; q=0.01",
            'origin': "http://www.cninfo.com.cn",
            'x-requested-with': "XMLHttpRequest",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
            'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
            'referer': "http://www.cninfo.com.cn/new/fulltextSearch?keyWord=" + self.parseName,
            'accept-language': "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
            'cache-control': "no-cache",
            'postman-token': "86fe2d06-4956-66a1-a41d-270e03463692"
            }

        conn.request("POST", "/new/information/topSearch/query", payload, headers)

        res = conn.getresponse()
        data = res.read()
        self.jsonMessage = data.decode("utf-8")

