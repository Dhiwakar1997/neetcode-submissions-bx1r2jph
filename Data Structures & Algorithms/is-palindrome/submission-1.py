class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"([^a-zA-Z0-9])","", s).lower()
        return s.lower() == s.lower()[::-1]