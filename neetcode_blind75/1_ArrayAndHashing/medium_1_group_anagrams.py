"""
49. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str])-> List[List[str]]:
        all_word_map={}
        final_anagram_list=[]
        for word in strs:
            word_list= [0]*26
            for char in word:
                word_list[ord(char)-ord('a')]+=1
            if tuple(word_list) not in all_word_map:
                all_word_map[tuple(word_list)]= [word]
            else:
                all_word_map[tuple(word_list)].append(word)
        for key, val_list in all_word_map.items():
            final_anagram_list.append(val_list)
        return final_anagram_list

sol= Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))