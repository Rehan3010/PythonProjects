class RequestParser:
    def __init__(self,requestString):
        lines= str(requestString).splitlines();
        #print("lines[0]"+lines[0]);
        self.reqMethod= lines[0].split(" ")[0]
        self.reqUrl= lines[0].split(" ")[1]
        self.reqHost=lines[1].split(" ")[1]
       # print("method: "+self.reqMethod)

    def getReqMethod(self):
        return self.reqMethod

    def getReqUrl(self):
        return self.reqUrl

    def getReqHost(self):
        return self.reqHost
