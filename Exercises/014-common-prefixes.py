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

# max_word = max(li1, key=len)
#
# print(li1[2])
# for i in range(len(max_word)-2):
#     print(max_word[0:i+2])
#     for j in range(len(li1)):
#         if max_word[0:i+2] in li1[j]:
#             print("TRUE")

def longest_common_prefix(strs: list[str]) -> str:
    # Edge case: empty list returns an empty string
    if not strs:
        return ""

    # Iterate through each character position of the first word
    for i in range(len(strs[0])):
        char = strs[0][i]

        # Compare this character with the same index across all other strings
        for word in strs[1:]:
            # If the current word is shorter than 'i' OR character doesn't match
            if i == len(word) or word[i] != char:
                return strs[0][:i]

    return strs[0]


# --- Testing the Examples ---
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))  # Output: ""





