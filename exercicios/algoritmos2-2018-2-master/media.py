#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def media(n1, n2):
    return (n1 + n2) / 2


def maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


if __name__ == '__main__':
    med = media(5, 3)
    print("Media {}".format(med))
