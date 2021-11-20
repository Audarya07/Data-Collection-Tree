

class Tree:

    def __init__(self):
        self.data = {}
        self.total_metrics = {
            "WebReq" : 0,
            "TimeSpent":0
        }
        self.new_metrics = {
            "WebReq" : 0,
            "TimeSpent":0
        }

    def insert(self, request):
        webreq = 0
        timespent = 0

        for i in range(len(request["dim"])):

            if request["dim"][i]["key"] == "device":
                device = request["dim"][i]["val"]
            else:
                country = request["dim"][i]["val"]

        try:
            for i in range(len(request["metrics"])):
                if request["metrics"][i]["key"] == "WebReq":
                    webreq = request["metrics"][i]["val"]
                else:
                    timespent = request["metrics"][i]["val"]
        except:
            pass

        if country in self.data:
            if device in self.data[country]:
                self.data[country][device]["WebReq"] += webreq
                self.data[country][device]["TimeSpent"] += timespent
            else:
                self.data[country][device] = self.new_metrics.copy()
                self.data[country][device]["WebReq"] = webreq
                self.data[country][device]["TimeSpent"] = timespent

            self.total_metrics["WebReq"] += webreq
            self.total_metrics["TimeSpent"] += timespent
        else:
            self.data[country] = {
                device: self.new_metrics.copy()
            }
            self.data[country][device]["WebReq"] = webreq
            self.data[country][device]["TimeSpent"] = timespent
            self.total_metrics["WebReq"] += webreq
            self.total_metrics["TimeSpent"] += timespent

    def get(self, request):
        webreq = 0
        timespent = 0
        if request["dim"][0]["key"] == "country":
            country = request["dim"][0]["val"]
            for i in self.data[country]:
                webreq += self.data[country][i]["WebReq"]
                timespent += self.data[country][i]["TimeSpent"]
        else:
            return {
                "status": "Error",
                "message": "Invalid dims !!"
            }

        response ={
            "dim":request["dim"][0],
            "metrics":[
                {
                    "key":"WebReq",
                    "val":webreq
                },
                {
                    "key":"TimeSpent",
                    "val": timespent
                }
            ]
        }

        return response
