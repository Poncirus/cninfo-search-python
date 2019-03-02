#!/usr/bin/python3

import os
import time

from StockInfoGet import StockInfoGet
from PdfListGet import PdfListGet
from FileDownload import FileDownload

# 搜索关键字  当前路径\keyword_list.txt
COMPANY_CONFIG_FILE = os.path.dirname(os.path.realpath(__file__)) + "\\keyword_list.txt"
keyFile = open(COMPANY_CONFIG_FILE)
keyList = keyFile.readlines()
keys = []
for key in keyList:
    key = key.rstrip('\n')  # 去除右边的换行符
    if(key == ""):
        break
    keys.append(key)

# 禁用关键字  当前路径\banword_list.txt
COMPANY_CONFIG_FILE = os.path.dirname(os.path.realpath(__file__)) + "\\banword_list.txt"
banFile = open(COMPANY_CONFIG_FILE)
banList = banFile.readlines()
bans = []
for ban in banList:
    ban = ban.rstrip('\n')  # 去除右边的换行符
    if(ban == ""):
        break
    bans.append(ban)

# 下载根目录  当前路径\download\
DOWNLOAD_PATH = os.path.dirname(os.path.realpath(__file__)) + "\\download\\"
if not os.path.exists(DOWNLOAD_PATH):
    os.mkdir(DOWNLOAD_PATH)

# 读取公司目录  当前路径\company_list.txt
COMPANY_CONFIG_FILE = os.path.dirname(os.path.realpath(__file__)) + "\\company_list.txt"
companyFile = open(COMPANY_CONFIG_FILE)
companyList = companyFile.readlines()

# 获取股票信息
for stockName in companyList:
    stockName = stockName.rstrip('\n')  # 去除右边的换行符
    if(stockName == ""):
        break
    si = StockInfoGet(stockName)
    orgId, code, name = si.getInfo()

    if(orgId == None):
        print("注意： 没有检索到" + stockName + "的信息")
        os.system("pause")
        continue

    if(stockName != name):
        print("注意： 输入名称为" + stockName + "，检索名称为" + name)
        os.system("pause")

    # 获取pdf链接
    pl = PdfListGet(orgId, code, name)
    pdfList = pl.getPdfList(keys, bans)

    # 下载pdf
    fileDownloadPath = DOWNLOAD_PATH + time.strftime("%Y-%m-%d %H-%M-%S  ", time.localtime(time.time())) + name +"\\"
    if not os.path.exists(fileDownloadPath):
        os.mkdir(fileDownloadPath)
    for info in pdfList:
        url = "http://static.cninfo.com.cn/" + info[0]
        extention = info[0][info[0].rfind('.'):].lower()  #截取文件后缀
        filename = time.strftime("%Y-%m-%d %H-%M-%S  ", time.localtime(info[1]/1000)) + info[2] + extention
        print("正在下载：" + filename)
        FileDownload(url, fileDownloadPath, filename)