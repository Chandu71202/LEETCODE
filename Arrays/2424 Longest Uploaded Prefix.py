class LUPrefix:

    def __init__(self, n: int):
        self.data=set()
        self.res=1
        
    def upload(self, video: int) -> None:
        self.data.add(video)
        if video==self.res:
            while(self.res in self.data):
                self.res+=1

    def longest(self) -> int:
        return self.res-1



# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
