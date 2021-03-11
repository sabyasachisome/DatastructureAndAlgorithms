"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Input: num = 3
Output: "III"

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Constraints:

1 <= num <= 3999
"""
import math

class Solution:
    def intToRoman(self, num: int) -> str:
        romansDict = \
            {
                1: "I",
                5: "V",
                10: "X",
                50: "L",
                100: "C",
                500: "D",
                1000: "M",
                5000: "G",
                10000: "H"
            }

        div = 1
        while num >= div:
            div *= 10

        div /= 10

        res = ""

        while num:

            # main significant digit extracted
            # into lastNum
            lastNum = int(num / div)

            if lastNum <= 3:
                res += (romansDict[div] * lastNum)
            elif lastNum == 4:
                res += (romansDict[div] +
                        romansDict[div * 5])
            elif 5 <= lastNum <= 8:
                res += (romansDict[div * 5] +
                        (romansDict[div] * (lastNum - 5)))
            elif lastNum == 9:
                res += (romansDict[div] +
                        romansDict[div * 10])

            num = math.floor(num % div)
            div /= 10

        return res

sol= Solution()
print(sol.intToRoman(35))