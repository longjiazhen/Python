import random

""" 对比选择排序和冒泡排序 
相同点：
1. O(N^2)
2. 每轮之后都确定一个全局最大/最小值的位置
不同点：
1. 选择排序每一轮非max/min的元素不需要交换位置，冒泡排序的需要
2. 冒泡排序具有稳定性，选择排序具有不稳定性（数组中有相同元素时，排序前排序后，相同元素的位置是否发生变化叫做是否具有稳定性）
例如：         5a  8   5b  2   9 （这里有5a和5b表示两个5）
选择第一轮：     2  8   5b  5a  9
冒泡第一轮第一步：5a 5b  8   2   9 
"""

def SelectSort(list):
    print(list)
    if len(list) < 2:
        pass
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
                # print("min = " + str(min))
                # print("i = " + str(i))
        if min != i:
            # print(list[i], list[min])
            # 方法一没有交换成功
            # swap1(list[i], list[min])
            # 方法二交换成功
            swap2(list, i, min)
            # 方法三交换成功
            # temp = list[min]
            # list[min] = list[i]
            # list[i] = temp
            # print(list[i], list[min])
        # print(list)
        # print("="*20)
    print(list)

def swap1(a, b):
    temp = a
    a = b
    b = temp

def swap2(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

# 上述swap1没有交换成功，swap2交换成功，应该是传值和传址的区别
# 那么，可以传指针么？试了swap1(*a, *b)不行，还是说传址就是swap2这种写法？


def CreateRandomArray():
    list = []
    arr_len = random.randint(5, 10)
    for i in range(arr_len):
        list.append(random.randint(1, 50))
    return list

list = CreateRandomArray()
# list = [2, 6, 5, 3, 1]
SelectSort(list)
