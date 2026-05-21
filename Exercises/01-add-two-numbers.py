"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


class Solution(object):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    def revers_li(self, li):
        num = ""
        for i in li[::-1]:
            num += ''.join(str(i))
        return int(num)

    def add_two_numbers(self, l1, l2):
        l3 = []
        num1 = self.reverse_li(l1)
        num2 = self.reverse_li(l2)

        total = int(num1) + int(num2)
        string_total = str(total)

        return [l3.append(int(i)) for i in string_total]



li1 = [2, 4, 3]
li2 = [5, 6, 4]
# l3 = []
# n1 = ""
# n2 = ""
#
# for i in l1[::-1]:
#     n1 += ''.join(str(i))
#
# for i in l2[::-1]:
#     n2 += ''.join(str(i))
#
# total = int(n1) + int(n2)
# string_total = str(total)
#
# [l3.append(int(i)) for i in string_total]
# print(l3)

print(Solution().add_two_numbers(li1, li2))










