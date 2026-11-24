class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = [{}, {}]

        for idx, input in enumerate([s, t]):
            for i in input: 
                if i in s_map[idx]:
                    s_map[idx][i] += 1
                else:
                    s_map[idx][i] = 1
            
        return s_map[0] == s_map[1]