class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        res1, res2 = [], []
        for log in logs:
            if (log.split()[1]).isdigit():
                res2.append(log)
            else:
                res1.append(log.split())
        res1.sort(key=lambda x: x[0])
        res1.sort(key=lambda x: x[1:])
        for i in range(len(res1)):
            res1[i] = (" ").join(res1[i])
        res1.extend(res2)
        return res1
s=Solution()
logs=["digi1 8 5 1","let1 art can","dig2 3 6","let2 own kit dig"]
res=s.reorderLogFiles(logs)
print(res)