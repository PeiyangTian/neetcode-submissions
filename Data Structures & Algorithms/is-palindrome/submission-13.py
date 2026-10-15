import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub(r'[^\w]', '', s)
        new1_s = new_s.lower()
        i = 0
        j = len(new1_s)-1
        while i<j:
            if new1_s[i] != new1_s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
