class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return self._solve_dict(nums)

    def _solve_dict(self, nums: List[int]) -> bool:
        nmap = {}
        for i in nums:
            if nmap.get(i) is None:
                nmap[i] = True
            else:
                return True
        return False
    
