import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        default_m = [0 for i in range(26)]
        for s in strs:
            m = copy.copy(default_m)
            for i in s:
                m[ord(i) - 97] += 1

            res[tuple(m)].append(s)

        return list(res.values())