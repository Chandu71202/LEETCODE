class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        
        m,n=len(maze),len(maze[0])
        exit=set()
        for i in range(m):
            if maze[i][0]=="." and [i,0]!=entrance:
                exit.add((i,0))
            if maze[i][n-1]=="." and [i,n-1]!=entrance:
                exit.add((i,n-1))
        for i in range(n):
            if maze[0][i]=="." and [0,i]!=entrance:
                exit.add((0,i))
            if maze[m-1][i]=="." and [m-1,i]!=entrance:
                exit.add((m-1,i))
        
        def bfs(maze,i,j):
            nonlocal exit,m,n
            seen=set()
            seen.add((i,j))
            q=[(i,j)]
            ans=0
            while q:
                for i in range(len(q)):
                    x,y=q.pop(0)
                    if (x,y) in exit:
                        return ans 
                    for cx,cy in [(1,0),(0,1),(-1,0),(0,-1)]:
                        nx,ny=x+cx,y+cy
                        if 0<=nx<m and 0<=ny<n and maze[nx][ny]=="." and (nx,ny) not in seen:
                            q.append((nx,ny))
                            seen.add((nx,ny))
                ans+=1

            return -1 

        return bfs(maze,entrance[0],entrance[1])
         

