#!/usr/bin/python3

import os
from StockInfoGet import StockInfoGet
from PdfListGet import PdfListGet
from FileDownload import FileDownload

DOWNLOAD_PATH = os.path.dirname(os.path.realpath(__file__)) + "\\download\\"
if not os.path.exists(DOWNLOAD_PATH):
    os.mkdir(DOWNLOAD_PATH)

stockName = "贵州茅台"
si = StockInfoGet(stockName)
orgId, code, name = si.getInfo()

if(stockName != name):
    print("注意： 输入名称为" + stockName + "，检索名称为" + name)

pl = PdfListGet(orgId, code, name)
pdfList = pl.getPdfList()
fileDownloadPath = DOWNLOAD_PATH + name + "\\"
if not os.path.exists(fileDownloadPath):
    os.mkdir(fileDownloadPath)
for shortUrl in pdfList:
    url = "http://static.cninfo.com.cn/" + shortUrl
    filename = url[url.rfind("/") + 1:]
    print(filename)
    FileDownload(url, fileDownloadPath, filename)