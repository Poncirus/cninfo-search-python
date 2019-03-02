#!/usr/bin/python3

from StockInfoGet import StockInfoGet
from PdfListGet import PdfListGet

si = StockInfoGet("贵州茅台")
orgId, code, name = si.getInfo()
pl = PdfListGet(orgId, code, name)
pdfList = pl.getPdfList()