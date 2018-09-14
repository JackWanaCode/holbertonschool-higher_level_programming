#!/usr/bin/env python3
def magic_calculation(a, b, c):
    if b < a:
        return c
    elif b > a:
        return a + b
    return a * b - c
