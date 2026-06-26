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

max_word = max(li1, key=len)

for i in range(len(max_word)-2):
    print(max_word[0:i+2])






