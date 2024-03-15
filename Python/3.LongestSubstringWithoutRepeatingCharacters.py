# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = []
        l = []

        for i in range(len(s)):
            t = []
            t.append(s[i])
            for j in range(i+1, len(s)):
                if s[j] in t:
                    l.append(len(t))
                    break
                t.append(s[j])
            l.append(len(t))
        return max(l) if l else 0