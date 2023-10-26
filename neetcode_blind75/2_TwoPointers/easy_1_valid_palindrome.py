"""
125. Valid Palindrome
Easy
company
Facebook
Yandex
Adobe

A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s: str)-> bool:
        left=0
        right= len(s)-1
        while left<right:
            if ((ord('a')<=ord(s[left].lower())<=ord('z')) or (ord('0')<=ord(s[left].lower())<=ord('9'))) and \
                ((ord('a')<=ord(s[right].lower())<=ord('z')) or (ord('0')<=ord(s[right].lower())<=ord('9'))) and \
                s[left].lower()==s[right].lower():
                left+=1
                right-=1
            elif not ((ord('a')<=ord(s[left].lower())<=ord('z')) or (ord('0')<=ord(s[left].lower())<=ord('9'))):
                left+=1
            elif not ((ord('a')<=ord(s[right].lower())<=ord('z')) or (ord('0')<=ord(s[right].lower())<=ord('9'))):
                right-=1
            else:
                return False
        return True
    
sol= Solution()
print(sol.isPalindrome("race a car"))