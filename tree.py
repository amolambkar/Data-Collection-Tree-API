"""
Author - Amol Ambkar
Program - Backend Assignment for GreedyGame

"""

class Tree():

    def __init__(self) -> None:
        self.data = {}
        self.total = {
            "WebReq" : 0,
            "TimeSpent":0
        }
        self.newMetrics = {
            "WebReq" : 0,
            "TimeSpent":0
        }

    def insert(self,newData):
        for i in range(len(newData["dim"])):
        
            if newData["dim"][i]["key"] == "device":
                device = newData["dim"][i]["val"]
            else:
                country = newData["dim"][i]["val"]
        
        webreq = 0
        timespent = 0
        try:
            for i in range(len(newData["metrics"])):
                if newData["metrics"][i]["key"] == "webreq":
                    webreq = newData["metrics"][i]["val"]
                else:
                    timespent = newData["metrics"][i]["val"]
        except:
            pass
    
        


        if country in self.data:
            if device in self.data[country]:
                self.data[country][device]["WebReq"] += webreq
                self.data[country][device]["TimeSpent"] += timespent

            else:
                self.data[country][device] = self.newMetrics.copy()

                self.data[country][device]["WebReq"] = webreq
                self.data[country][device]["TimeSpent"] = timespent

            self.total["WebReq"] += webreq
            self.total["TimeSpent"] += timespent

        else:
            
            self.data[country] = {
                device: self.newMetrics.copy()
            }
            
            self.data[country][device]["WebReq"] = webreq
            self.data[country][device]["TimeSpent"] = timespent

            self.total["WebReq"] += webreq
            self.total["TimeSpent"] += timespent

    def get(self,query):
        
        country = query["dim"][0]["val"]       
        webreq = 0
        timespent = 0

        for i in self.data[country]:
            webreq += self.data[country][i]["WebReq"]
            timespent += self.data[country][i]["TimeSpent"]

        result ={
            "dim":query["dim"][0],
            "metrics":[
                {
                    "key":"webreq",
                    "val":webreq
                },
                {
                    "key":"timespent",
                    "val": timespent
                }
            ]
        }

        return result
