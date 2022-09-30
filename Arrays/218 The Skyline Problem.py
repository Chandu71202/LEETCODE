class Solution(object):
    def getSkyline(self, buildings):
        def addsky(pos, hei):
            if sky[-1][1] != hei:
                sky.append([pos, hei])

        sky = [[-1,0]]
        position = set([b[0] for b in buildings] + [b[1] for b in buildings])
        live = []
        i = 0
        for t in sorted(position):
            while i < len(buildings) and buildings[i][0] <= t:
                heappush(live, (-buildings[i][2], buildings[i][1]))
                i += 1
            while live and live[0][1] <= t:
                heappop(live)
            h = -live[0][0] if live else 0
            addsky(t, h)
        return sky[1:]
