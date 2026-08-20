class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        start = 0
        end = 0
        
        for i in range(len(s)):
            # Odd length palindromes (e.g., "aba")
            len1 = self.expandAroundCenter(s, i, i)
            # Even length palindromes (e.g., "abba")
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            max_len = max(len1, len2)
            
            # Update the start and end indices if a longer palindrome is found
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length of the palindrome found
        return right - left - 1