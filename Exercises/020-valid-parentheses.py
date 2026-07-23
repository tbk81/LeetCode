"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
"""

def is_valid(s: str) -> bool:
    # A stack to keep track of opening brackets
    stack = []

    # Map closing brackets to their corresponding opening brackets
    matching_bracket = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in matching_bracket:
            # If the character is a closing bracket, check the stack
            top_element = stack.pop() if stack else "#"

            # If the popped element doesn't match the corresponding opening bracket, it's invalid
            if matching_bracket[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were properly matched
    return not stack









