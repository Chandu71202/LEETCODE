class TimeMap:

    def __init__(self):
        self.d={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        x = [timestamp,value]
        if self.d.get(key,-1)==-1:
            self.d[key]=[x]
        else:
            self.d[key].append(x)
        
    def get(self, key: str, timestamp: int) -> str:
        try:
            l = self.d[key]
        except:
            return ''
        
        left, right = 0, len(l)- 1
        while left < right:
            mid = (left+ right+ 1) //2
            time, value = l[mid]
            if time > timestamp:
                right = mid - 1
            else:
                left = mid
                
        return l[left][1] if l[left][0] <= timestamp else ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
