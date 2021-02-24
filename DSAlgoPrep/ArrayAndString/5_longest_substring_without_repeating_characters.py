strn= 'geeksforgeeks'
"""
sliding wondow technique
"""
class Solution:
    def lengthOfLongestSubstring_On2(self, s: str) -> int:
        strn_len = len(s)
        max_len = 0
        for i in range(strn_len):
            visited_stat = [0] * 256
            for j in range(i, strn_len):
                if visited_stat[ord(s[j])] == True:
                    break
                else:
                    max_len = max(max_len, j + 1 - i)
                    visited_stat[ord(s[j])] = True

            visited_stat[ord(s[i])] = False
        return max_len

    def lengthOfLongestSubstring_On(self, s: str) -> int:
        seen_map={}
        start=0
        strn_len= len(s)
        max_len= 0
        for end in range(strn_len):
            if s[end] in seen_map:
                start= max(start, seen_map[s[end]]+1)
            seen_map[s[end]]=end
            max_len= max(max_len, end-start+1)
        return max_len

sol= Solution()
print(sol.lengthOfLongestSubstring_On2(strn))
print(sol.lengthOfLongestSubstring_On(strn))