import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        default_m = [0 for i in range(26)]
        for s in strs:
            m = copy.copy(default_m)
            for i in s:
                idx = ord(i) - 97
                if m[idx] > 0:
                    m[idx] += 1
                else:
                    m[idx] = 1
            if tuple(m) in res:
                res[tuple(m)].append(s)
            else:
                res[tuple(m)] = [s]

        return [res[r] for r in res]
