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

    def add_two_numbers(self, l1, l2):
        num1 = ""
        num2 = ""
        l3 = []

        for i in l1[::-1]:
            num1 += ''.join(str(i))
        for i in l2[::-1]:
            num2 += ''.join(str(i))

        total = int(num1) + int(num2)
        string_total = str(total)

        return [int(i) for i in string_total]



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


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         # Create a dummy node to act as the starting point of our new list
#         dummy_head = ListNode(0)
#         current = dummy_head
#         carry = 0
#
#         # Loop as long as there are nodes in l1, l2, or a leftover carry
#         while l1 is not None or l2 is not None or carry != 0:
#             # Get the values from the current nodes (use 0 if the node is empty)
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
#
#             # Calculate the total and the new carry
#             total = val1 + val2 + carry
#             carry = total // 10  # Floor division extracts the tens digit (e.g., 15 // 10 = 1)
#             new_digit = total % 10  # Modulo extracts the ones digit (e.g., 15 % 10 = 5)
#
#             # Create the new node with the single digit and attach it
#             current.next = ListNode(new_digit)
#             current = current.next
#
#             # Move l1 and l2 to their next nodes
#             if l1: l1 = l1.next
#             if l2: l2 = l2.next
#
#         # Return the next node after dummy_head, which is the actual start of our result
#         return dummy_head.next





