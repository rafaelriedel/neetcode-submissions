class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self._solve_sort(s, t)

    def _solve_sort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def _solve_brute_force_map(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        stat = [dict(), dict()]
            
        for idx, target in enumerate([s, t]):
            for i in range(len(s)):
                if target[i] in stat[idx]:
                    stat[idx][target[i]] += stat[idx][target[i]]
                else:
                    stat[idx][target[i]] = 1
        
        return stat[0] == stat[1]

