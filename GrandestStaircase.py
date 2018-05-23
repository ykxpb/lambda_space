#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 yuanyang <enulex@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The Grandest Staircase Of Them All
==================================

With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options. 

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31
 
But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called answer(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!
"""

"""
f(n, m): n，待分解的数，m：最大数, 分解的数不能相同

回归条件:
- n = 1, 无论m的值为多少，只有一种划分 {1};
- m = 1, 无论n的值为多少，只有一种划分 {n};

特殊情况:
- n = m 
    - 划分中包含n，只有一个 {n};
    - 划分中不包含n，这时划分中最大的数字一定比n小，即n的所有(n-1)划分；
    故：f(n,n) = 1 + f(n, n-1)
- n < m: = f(n, n)

通用情况:
- n > m: 
    - 划分中包含m，{m, {x1, x2, xi}}，不能再次出现m，因此是（n-m) 的 m-1划分：f(n-m, m-1)
    - 划分中不包含m的情况，即划分中所有值都比m小，即n的(m-1)划分，个数为f(n, m-1)
    故：f(n,m) = f(n-m, m-1) + f(n, m-1)

f(n, m) = {
    n = 1, m = 1        : 1
    n < m               : q(n, n)
    n = m               : 1 + f(n, n-1)
    n > m > 1           : f(n-m, m-1) + f(n, m-1)
}
"""

def answer1(n):
    size = n + 1
    matrix = {}
    for i in range(size+1):
        matrix[i] = {}

    matrix[0][0] = 1
    for prev in range(1, size+1):
        for left in range(size+1):
            matrix[prev][left] = matrix[prev-1].get(left) or 0
            if left >= prev:
                matrix[prev][left] = (matrix[prev].get(left) or 0) + (matrix[prev - 1].get(left - prev) or 0)
    return matrix[n][n] - 1

def answer(n):
    result = {}
    for i in range(n+1):
        result[i] = {}

    for i in range(n+1):
        for j in range(n+1):
            if j == 0:
                result[i][j] = 1
            elif i == 0:
                result[i][j] = 0
            elif i > j:
                result[i][j] = result[j][j]
            else:
                result[i][j] = result[i-1][j] + result[i-1][j-i]

    return result[n][n] - 1
