class TimeMap:

    def __init__(self):    
        self.data=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        keyStore = self.data.get(key,[])
        if keyStore:
            for time,val in keyStore[::-1]:
                if time<=timestamp:
                    return val
        return ""