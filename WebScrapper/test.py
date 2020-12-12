from urllib.request import urlopen
import os
class WebScrapper():
    def __init__(self):
        self.url = "https://www.internetdownloadmanager.com/download.html"
    
    def writefile(self,data):
        with open(os.path.join(os.sys.path[0], "content.txt"),'w') as file:
            file.write(data)

    def scrapper(self):
        page = urlopen(self.url)
        htmlbyte = page.read()
        htmlcode = htmlbyte.decode("utf-8")
        self.writefile(htmlcode)

if __name__ == "__main__":
    obj = WebScrapper()
    obj.scrapper()