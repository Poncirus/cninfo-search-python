#!/usr/bin/python3

from urllib import parse
import http.client
import json

class PdfListGet:
    def __init__(self, orgId, code, name):
        self.orgId = orgId
        self.code = code
        self.name = name
        self.data = []

    def getPdfList(self):
        print("Start get pdf list: " + self.name + " in ShangHai")
        self.httpConnect("sse", "shmb")
        self.jsonDecode()
        print("Start get pdf list: " + self.name + " in ShenZhen")
        self.httpConnect("szse", "sz")
        self.jsonDecode()
        return self.data

    def jsonDecode(self):
        if(self.jsonMessage != None):
            data = json.loads(self.jsonMessage)
            if(data["totalAnnouncement"] > 30):
                print("Warning: totalAnnouncement > 30")
            announ = data["announcements"]
            for a in announ:
                self.data.append(a["adjunctUrl"])


    # 创建http连接  获取Json字符串
    # ！ 去掉 'accept-encoding': "gzip, deflate", 解除加密
    def httpConnect(self, column, plate):
        conn = http.client.HTTPConnection("www.cninfo.com.cn")

        payload = "pageNum=1&pageSize=30&tabName=fulltext&column=" + column + "&stock=" + self.code + "%2C" + self.orgId + "&searchkey=%E9%87%8D%E5%A4%A7%E4%BA%8B%E9%A1%B9%3B&secid=&plate=" + plate + "&category=&trade=&seDate=2000-01-01+~+2099-03-01"

        headers = {
            'accept': "application/json, text/javascript, */*; q=0.01",
            'accept-language': "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
            'connection': "keep-alive",
            'content-length': "192",
            'host': "www.cninfo.com.cn",
            'origin': "http://www.cninfo.com.cn",
            'referer': "http://www.cninfo.com.cn/new/disclosure/stock?orgId=" + self.orgId + "&stockCode=" + self.code,
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
            'x-requested-with': "XMLHttpRequest",
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            }
        
        conn.request("POST", "/new/hisAnnouncement/query", payload, headers)
        try:
            res = conn.getresponse()
            data = res.read()
            self.jsonMessage = data.decode("utf-8")
        except ConnectionResetError:
            print("ConnectionResetError: " + self.name +", " + column)
            self.jsonMessage = None

        