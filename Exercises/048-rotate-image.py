"""
https://leetcode.com/problems/rotate-image/description/
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],
                [4,5,6],
                [7,8,9]]
Output: [[7,4,1],
        [8,5,2],
        [9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],
                [2,4,8,10],
                [13,3,6,7],
                [15,14,12,16]]
Output: [[15,13,2,5],
        [14,3,4,1],
        [12,6,8,9],
        [16,7,10,11]]
"""

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

# print(matrix1[0][0])
li1 = [matrix1[2][0], matrix1[1][0], matrix1[0][0]]
li2 = [matrix1[2][1], matrix1[1][1], matrix1[0][1]]
li3 = [matrix1[2][2], matrix1[1][2], matrix1[0][2]]
# print(len(matrix1))
# for l in matrix1:
#     print(l)
# print("\n")
# print(li1)
# print(li2)
# print(li3)

# for i in range(len(matrix1) - 1, -1, -1):
#     for j in range(len(matrix1)):
#         print(matrix1[i][j])
    # print(matrix1[i][1])
    # print(matrix1[i][2])
for j in range(len(matrix1)):
    for i in range(len(matrix1) - 1, -1, -1):
        print(matrix1[i][j])
# help(range)

