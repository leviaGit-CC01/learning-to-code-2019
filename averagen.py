#!/usr/bin/env python3
N = int(input("Enter numbers you want to get average: "))
count = 0
sums = 0
while count < N:
    number = float(input("number you want to calculate: "))
    sums = sums + number
    count += 1
average = sums/N
print("N= {}, sums = {}".format(N,sums))
print("average = {:.2f}".format(average))

