from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.max = 0
        self.previous = SortedList()

    def book(self, start: int, end: int) -> int:
        self.previous.add((start,1))
        self.previous.add((end,-1))
        count = 0
        for x, y in self.previous:
            count+=y
            self.max = max(self.max,count)
        print(count,self.max)
        return self.max


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
