class Solution:
    def scoreOfString(self, s: str) -> int:
        diff = 0
        l = len(s)
        for i in range (l-1):
            diff += abs(ord(s[i]) - ord(s[i+1]))
        return diff