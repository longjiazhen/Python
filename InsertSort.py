import random

"""
整体思想类似扑克牌的整牌
左边是已经有序的，然后每来一个新的数，从右往左遍历，找到它刚好可以插进去的位置
冒泡排序、选择排序的时间复杂度总是O(N^2)
插入排序最好的情况是O(N)，最坏的情况是O(N^2)
通常说时间复杂度说的都是最坏情况
"""

def InsertSort(list):
    print(list)
    if len(list) < 2:
        pass
    # i是新来的数的下标
    for i in range(len(list)):
        # j是左边已有的有序数的下标
        for j in range(i):
            if list[i] < list[j]:
                swap(list, i, j)
    print(list)

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def CreateRandomList():
    list = []
    list_len = random.randint(0, 20)
    for i in range(list_len):
        list.append(random.randint(-100, 100))
    return list

list = CreateRandomList()
# list = [6, 3, 2, 4]
InsertSort(list)
