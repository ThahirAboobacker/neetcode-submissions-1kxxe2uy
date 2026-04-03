class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_a=Counter(s)
        count_b=Counter(t)

        return count_a==count_b
