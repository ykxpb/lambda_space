#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called answer(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) src = 19
    (int) dest = 36
Output:
    (int) 1

Inputs:
    (int) src = 0
    (int) dest = 1
Output:
    (int) 3
"""

from collections import deque

def is_valid(src, pos):
    return pos >= 0 and pos <= 63 and (
        (abs((src % 8) - (pos % 8)) == 1 and abs((src // 8) - (pos // 8)) == 2) or
        (abs((src % 8) - (pos % 8)) == 2 and abs((src // 8) - (pos // 8)) == 1)
    )

def get_next_steps(src, stack, parents, dest):
    for move in [-15, -6, 10, 17, 15, 6, -10, -17]:
        nstep = src + move
        if is_valid(src, nstep) and (parents.get(nstep) == None):
            stack.append(nstep)
            parents[nstep] = src

            if dest == nstep:
                return True

def locate_dest(stack, parents, dest):
    while len(stack) > 0:
        node = stack.popleft()
        if get_next_steps(node, stack, parents, dest):
            return

def answer(src, dest):
    if src < 0 or src > 63:
        return
    if dest < 0 or dest > 63:
        return
    if src == dest:
        return 0

    parents = {}
    stack = deque([src])
    locate_dest(stack, parents, dest)

    n = 0
    node = dest
    while True:
        node = parents[node]
        n = n + 1
        if src == node:
            return n

# assert(answer(19, 36) == 1)
# assert(answer(0, 1) == 3)
print(answer(0, 63))
#print(answer(-1, -10))
#print(answer(0, 60))

print('ok')
