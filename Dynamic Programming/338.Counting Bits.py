class Solution:
   def countBits(self, num: int) -> List[int]:
      counter = [0]
      for i in range(1, num+1):
          counter.append(counter[i >> 1] + i % 2)
      return counter

    
#2nd method but 1st is having less space 
# def countBits(self,n):
#   l=[]
#   for i in range(n+1):
#       d={}
#       d={'0':0,'1':0}
#       s=bin(i)[2:]
#       for i in range(len(s)):
#           d[s[i]]=d[s[i]]+1
#       l.append(d['1'])
#       # print(bin(i).replace("0b", ""))
#   return l
