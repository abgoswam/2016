# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:39:57 2016

@author: agoswami
"""

class Solution(object):
        
    def __init__(self):
        self.words = {}
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        
        if s is None:
            return []

        if s in self.words:
            return self.words[s]
            
        interSet = set()
        if s in wordDict:
            interSet.add(s)
            
        for i in range(1, len(s)):
            s1 = s[:i]
            s2 = s[i:]
            
            if s1 in wordDict:
#                do domething with s2
                s2_wordBreakList = self.wordBreak(s2, wordDict)
                
                for item in s2_wordBreakList:
                    interSet.add(s1 + " " + item)

        self.words[s] = []        
        for item in interSet:
            self.words[s].append(item)
                    
        return self.words[s]
            
        
mysol = Solution()

s = "leetcode"
wordDict = {"leet", "code"}
retlist = mysol.wordBreak(s, wordDict)
for item in retlist:
    print item

        
s = "ilike"
wordDict = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
retlist = mysol.wordBreak(s, wordDict)
for item in retlist:
    print item


s = "catsanddog"
wordDict = {"cat", "cats", "and", "sand", "dog"}
retlist = mysol.wordBreak(s, wordDict)
for item in retlist:
    print item
    
s = "aaa"
wordDict = {"aaaa", "aa", "a"}
retlist = mysol.wordBreak(s, wordDict)

print "-" * 20
for item in retlist:
    print item
    