#  Project yo is developed by Fahad Ahammed on 4/22/21, 11:57 PM.
#
#  Last modified at 4/22/21, 11:57 PM.
#
#  Github: fahadahammed
#  Email: obak.krondon@gmail.com
#
#  Copyright (c) 2021. All rights reserved.

import datetime
import os
import sys


def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result