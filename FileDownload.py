#!/usr/bin/python3

import requests 

class FileDownload:
    def __init__(self, url, path, filename):
        self.url = url
        self.path = path
        self.filename = filename
        self.download()

    def download(self):
        r = requests.get(self.url)
        with open(self.path + self.filename, "wb") as code:
            code.write(r.content)
