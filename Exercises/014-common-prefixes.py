"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix amongst the input strings.
"""

li1 = ["flower", "flow", "flight"]
li2 = ["dog", "racecar", "car"]

l = 0
for word in li1:
    while l < len(word):
        print(word[l:l+2])
        print(word[l:l+3])

        l += 1





