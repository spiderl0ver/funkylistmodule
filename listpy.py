#!/usr/bin/env python3
"""Funky List time"""
# my discord is boots
# apache 2.0
# who in their right mind would use this module
# bruh the .sort function is faster
import random


def bogosort(self):
    while self != sorted(self):
        random.shuffle(self)
    return self


def bubblesort(self):
    while self != sorted(self):
        for i in range(len(self) - 1):
            if self[i] > self[i + 1]:
                nself = self
                self = []
                for x in range(len(nself)):
                    if x == i:
                        self.append(nself[x + 1])
                    elif x == i + 1:
                        self.append(nself[x - 1])
                    else:
                        self.append(nself[x])
    return self


def quicksort(nums, l=0, r="i"):
    if r == "i":
        r = len(nums) - 2
    if len(nums) == 1:  # from geeks for geeks.org
        return nums  # this function was modified to work with one param
    if l < r:
        pivot, ptr = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        nums[ptr], nums[r] = nums[r], nums[ptr]
        quicksort(nums, l, ptr - 1)
        quicksort(nums, ptr + 1, r)
    return nums


def insertsort(self):
    for x in range(1, len(self)):
        minuser = x - 1
        decider = self[x]
        while minuser >= 0 and decider < self[minuser]:
            self[minuser + 1] = self[minuser]
            minuser -= 1
        self[minuser + 1] = decider
    return self


def selectsort(nself):
    subarray = []
    self = nself
    while subarray != sorted(nself):
        bottom = self[0]
        bottomindex = 0
        for x in range(len(self)):
            if self[x] < bottom:
                bottomindex = x
                bottom = self[x]
        subarray.append(bottom)
        self = [self[x] for x in range(len(self)) if x != bottomindex]
    return subarray


def heapsort(self):
    g = 0 # slightly modified for pythonic integration from what it should be
    while self != sorted(self):
        g = (g+1)%2
        for i in range(1, len(self)):
            if i % 2 == g:
                if self[i] <= self[i - 2]:
                    x = self[i-2]
                    y = self[i]
                    self[i-2] = y
                    self[i] = x

            else:
                if self[i] <= self[i - 1]:
                    x = self[i - 1]
                    y = self[i]
                    self[i - 1] = y
                    self[i] = x
    return self


def shellsort(self): # got this from geeks for geeks
    length = len(self)
    gap = length // 2
    while gap > 0:
        m = gap
        while m < length:
            i = m - gap
            while i >= 0:
                if self[i + gap] > self[i]:
                    break
                else:
                    x = self[i + gap]
                    y = self[i]
                    self[i+gap] = y
                    self[i] = x
                i = i - gap
            m += 1
        gap = gap //2
    return self
