# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:39:57 2016

@author: agoswami
"""

class Solution(object):
    def __init__(self):
        self.notbreakable = set()
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        
        if s is None:        
            return False
            
        if s in wordDict:
            return True
        
        for i in range(1, len(s)):
            s1 = s[:i]

            if s1 in wordDict:
                s2 = s[i:]
                if s2 not in self.notbreakable:
                    wb2 = self.wordBreak(s2, wordDict)
                    if (wb2 is True):
                        return True
        
        self.notbreakable.add(s)
        return False


mysol = Solution()

s = "leetcode"
wordDict = {"leet", "code"}
print mysol.wordBreak(s, wordDict)
        
s = "ilike"
wordDict = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
print mysol.wordBreak(s, wordDict)