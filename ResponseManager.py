import fileinput
class ResponseManager:
    def __init__(self):
        self.filename=" "

    def getBlockedUserPage(self):
       f=open("BlockedIP.html","r")
       str= f.read()
       return str;
    def getBlockedKeyword(self):
        f = open("blockedkeyword.html", "r")
        str = f.read()
        return str;
    def getBlockedWebsite(self):
        f = open("blockedwebsite.html", "r")
        str = f.read()
        return str;
