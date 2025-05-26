class Solution(object):
    def largestPathValue(self, colors, edges):
        n = len(colors)
        al = [[] for _ in range(n)]
        cnt = [[0] * 26 for _ in range(n)]
        indegrees = [0] * n
        
        for e in edges:
            al[e[0]].append(e[1])
            indegrees[e[1]] += 1
            
        q = []
        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)
        
        res, processed = 0, 0
        while q:
            q1 = []
            for i in q:
                processed += 1
                res = max(res, cnt[i][ord(colors[i]) - ord('a')] + 1)
                cnt[i][ord(colors[i]) - ord('a')] += 1
                for j in al[i]:
                    for k in range(26):
                        cnt[j][k] = max(cnt[j][k], cnt[i][k])
                    indegrees[j] -= 1
                    if indegrees[j] == 0:
                        q1.append(j)
            q = q1
        
        return res if processed == n else -1