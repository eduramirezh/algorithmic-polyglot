#!/bin/python3

import sys

n, k = input().strip().split(' ')
n, k = [int(n),int(k)]
number = [int(x) for x in input().strip()]
length = len(number)
changed_indexes = set()
if k >= n:
    print('9'*n)
else:
    for i in range(len(number)//2):
        left = number[i]
        right = number[length - 1 - i]
        if left != right:
            changed_indexes.add(i)
            k -= 1
            if left < right:
                number[i] = right
            else:
                number[length - 1 - i] = left
    if k < 0:
        print(-1)
    else:
        i = 0
        while i < length//2:
            changeable = (k >= 2) or (i in changed_indexes and k >= 1)
            if number[i] != 9 and changeable:
                number[i] = 9
                number[length - 1 - i] = 9
                if i in changed_indexes:
                    k -= 1
                else:
                    k -= 2
            i += 1
        if k == 1 and length%2 == 1:
            number[length//2] = 9
            k -= 1
        print("".join(str(x) for x in number))
