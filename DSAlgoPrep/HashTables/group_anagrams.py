from typing import List
from collections import defaultdict

class Solution:

    def hashed(self, strn):
        return ''.join(sorted(strn))

    def group_anagrams(self, word_list: List[str])-> List[list]:
        hash_map=defaultdict(list)
        list_of_anagrams= []
        for word in word_list:
            hashed_word= self.hashed(word)
            hash_map[hashed_word].append(word)
        hash_map= {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[0])}
        for val in hash_map.values():
            list_of_anagrams.append(val)
        return list_of_anagrams

sol= Solution()
print(sol.group_anagrams(["eat","tea","tan","ate","nat","bat"]))