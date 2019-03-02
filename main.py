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

# 下载根目录  当前路径\download\
DOWNLOAD_PATH = os.path.dirname(os.path.realpath(__file__)) + "\\Download\\"
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

    if(stockName != name):
        print("注意： 输入名称为" + stockName + "，检索名称为" + name)

    # 获取pdf链接
    pl = PdfListGet(orgId, code, name)
    pdfList = pl.getPdfList(keys)

    # 下载pdf
    fileDownloadPath = DOWNLOAD_PATH + time.strftime("%Y-%m-%d %H-%M-%S  ", time.localtime(time.time())) + name +"\\"
    if not os.path.exists(fileDownloadPath):
        os.mkdir(fileDownloadPath)
    for info in pdfList:
        url = "http://static.cninfo.com.cn/" + info[0]
        filename = time.strftime("%Y-%m-%d %H-%M-%S  ", time.localtime(info[1]/1000)) + info[2] + ".pdf"
        print("正在下载：" + filename)
        FileDownload(url, fileDownloadPath, filename)