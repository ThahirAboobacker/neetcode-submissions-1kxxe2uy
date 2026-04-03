class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s1=s[::-1]
        return ''.join(char for char in s if char.isalnum())==''.join(char for char in s1 if char.isalnum())


        