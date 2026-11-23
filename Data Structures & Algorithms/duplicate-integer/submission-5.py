class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return self._solve_set(nums)

    def _solve_set(self, nums: List[int]) -> bool:
        dups = set()
        for i in nums:
            if i in dups:
                return True
            dups.add(i)
        
        return False
            
    def _solve_dict(self, nums: List[int]) -> bool:
        nmap = {}
        for i in nums:
            if nmap.get(i) is None:
                nmap[i] = True
            else:
                return True
        return False
    

    def _solve_brute_force(self, nums: List[int]) -> bool:
        # brute force don't work for big length.
        duplicate = False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    duplicate = True
                    
            if duplicate:
                return True
        
        return False



