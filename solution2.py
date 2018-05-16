#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 yuanyang <enulex@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Power Hungry
============

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. You and your team of henchmen have been assigned to repair the solar panels, but you'd rather not take down all of the panels at once if you can help it, since they do help power the space station and all!

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is. Write a function answer(xs) that takes a list of integers representing the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  So answer([2,-3,1,0,-5]) will be "30".

Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the answer as a string representation of the number.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) xs = [2, 0, 2, 2, 0]
Output:
    (string) "8"

Inputs:
    (int list) xs = [-2, -3, 4, -5]
Output:
    (string) "60"

"""

def answer(xs):
    xss = sorted(xs)
    presult = None
    nresult = None
    zresult = None
    npending = None
    for x in xss:
        if x > 0:
            presult = (presult or 1) * x
        elif x < 0:
            npending = x
            nresult = (nresult or 1) * x
        else:
            zresult = 0

    if nresult != npending and nresult < 0:
        nresult = nresult / npending

    result = []
    result.append(presult)
    result.append(nresult)
    result.append(zresult)
    result.append(presult and nresult and presult * nresult)
    result.append(presult and zresult and presult * zresult)
    result.append(nresult and zresult and nresult * zresult)
    result.append(presult and nresult and zresult and presult * nresult * zresult)
    return max(result)

answer = answer2

assert(answer([2, 0, 2, 2, 0]) == 8)
assert(answer([-2, -3, 4, -5]) == 60)
assert(answer([-1, 0, -2, -2, 0]) == 4)
assert(answer([-2, 4, -5, -3, 0]) == 60)
assert(answer([2]) == 2)
assert(answer([0, 0]) == 0)
assert(answer([2, -3, 1, 0, -5]) == 30)
assert(answer([-2]) == -2)
assert(answer([-2, 0]) == 0)

print('ok')
