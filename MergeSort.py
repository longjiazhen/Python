import random

# 递归求列表中最大值
# def  getMax(list, L, R):
#     if L == R: # base case，停止递归的地方
#         return list[L]
#     mid = int((L+R)/2)  # 如果要防溢出，可以写成 L + ((R-L)/2)
#     maxLeft = getMax(list, L, mid)
#     maxRight = getMax(list, mid+1, R)
#     return max(maxLeft, maxRight)
#
#
# list = [3, 5, 7, 1, 0 ]
# maxItem = getMax(list, 0, len(list)-1)
# print(maxItem)

# 外排
def Merge(list, L, mid, R):
    # print(list)
    list2 = []
    i = L
    j = mid + 1
    # 两个都没有越界时
    while(i<=mid and j<=R):
        # print("list[" + str(i) + "]=" + str(list[i]) + " list[" + str(j) + "]=" + str(list[j]))
        if list[i] < list[j]:
            list2.append(list[i])
            i += 1
        else:
            list2.append(list[j])
            j += 1
    # 有且只有一个会越界
    # 如果左边越界
    while(j <= R):
        list2.append(list[j])
        j += 1
    # 如果右边越界
    while(i <= mid):
        list2.append(list[i])
        i += 1
    for i in range(0, len(list2)):
        list[L + i] = list2[i]
    # 注意这里list2的i位置拷贝回list的L+i位置，而不是简单地赋值list=list2
    # print(list)
    return list

def MergeSort(list, L, R):
    # print("Before:", end=" ")
    # print(list, end=" ")
    # print("L = " + str(L) + " R = " + str(R))
    if len(list) <= 1:
        return list
    if L == R:
        return
    mid = int((L+R)/2)
    MergeSort(list, L, mid)
    MergeSort(list, mid+1, R)
    list = Merge(list, L, mid, R)
    # print("After:", end=" ")
    # print(list)
    # print("L = " + str(L) + " R = " + str(R))
    return list



def CreateRandomList():
    list = []
    list_len = random.randint(0, 10)
    for i in range(list_len):
        list.append(random.randint(-100, 100))
    return list

list = CreateRandomList()
print(list)
# list = [3, 7, 2, 9]
# Merge(list, 0, 1, 3)
# list = [7, 3, 9, 2]
MergeSort(list, 0, len(list)-1)
print(list)
