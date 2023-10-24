"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
class Solution:
    def isAnagram(self, s: str, t: str)-> bool:
        s_map={}
        t_map={}
        for char in s:
            if char not in s_map:
                s_map[char]=1
            else:
                s_map[char]+=1
        # print(s_map)
        for char in t:
            if char not in t_map:
                t_map[char]=1
            else:
                t_map[char]+=1
        anagrag_flag= True
        for s_key in s_map:
            if s_key not in t_map or s_map[s_key]!= t_map[s_key]:
                anagrag_flag= False
                break
        for t_key in t_map:
            if t_key not in s_map or s_map[t_key]!= t_map[t_key]:
                anagrag_flag= False
                break
        return anagrag_flag==True

sol= Solution()
print(sol.isAnagram("anagram","nagaram"))


