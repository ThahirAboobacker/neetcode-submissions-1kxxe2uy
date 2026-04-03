

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Count the frequency of characters in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Check if both dictionaries are equal
        return count_s == count_t
