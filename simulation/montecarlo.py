#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import random

# initialization
a, b = 1, math.e
N = 1000
f = lambda x:-math.cos(math.pi*math.log(x))
accumulation = 0

# monte carlo method
for i in range(1, N+1):
    x = random.uniform(a, b)
    accumulation += f(x)
    print((b-a)*accumulation/i)
