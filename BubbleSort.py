import random
import copy
import string

def BubbleSort(list):
    print("Bofore Sorted:", end=" ")
    print(list)
    # 异常处理
    if (list == None) or (len(list) < 2):
        pass
    # 冒泡排序
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[j] < list[i]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
    print("After Sorted:", end=" ")
    print(list)

def RightMethod(list):
    print("Bofore Sorted:", end=" ")
    print(list)
    # 只有列表才能用sort()
    # list.sort() # 从小到大排序
    # list.sort(reverse=True) # 从大到小排序
    # 字典之类的也能用sorted()
    sorted(list)  # 从小到大排序
    # sorted(list, reverse=True) # 从大到小排序
    print("After Sorted:", end=" ")
    print(list)

# 生成随机列表
def CreateRandomArray():
    array = []
    array_len = random.randint(0, 20)
    for i in range(array_len):
        # 元素类型为整型
        array.append(random.randint(-100, 100))
    print(array)
    return array
# CreateRandomArray()

def CreateRandomString():
    str_len = random.randint(1, 20)
    # 元素类型为小写字母
    # str = "".join(random.sample(string.ascii_lowercase, str_len))
    # 元素类型为大写字母
    # str = "".join(random.sample(string.ascii_uppercase, str_len))
    # 元素类型为大写字母加小写字母
    # str = "".join(random.sample(string.ascii_letters, str_len))
    # 元素类型为字母加数字
    str = "".join(random.sample(string.ascii_letters + string.digits, str_len))
    print(str)
CreateRandomString()

# list = [6, 5, 1, 7, 0, 3]
# list = [6, 5, 1, 2, 4, 3]
# list = []
# list = [9]
# list = CreateRandomArray()
# BubbleSort(list)
# Q：python里2个内容相同的数组指向的是同一块内存，所以这里BubbleSort改了list的内容
# RightMethod 接收到的数组就已经是有序的里，没法验证2个排序算法的效果是不是相同
# 能不能有一个方法，强行让数组指向不同内存，list2 = list 不可行, copy.copy()和copy.deepcopy(）也不可行
# RightMethod(list2)

# list1 = [1, 2, 3, [4, 5]]
# list2 = copy.copy(list1)
# list1.append(6)
# print(list1)
# print(list2)
# # 结果是：
# # [1, 2, 3, [4, 5], 6]
# # [1, 2, 3, [4, 5]]


# list1 = [1, 2, 3, [4, 5]]
# list2 = copy.copy(list1)
# list1[3].append(6)
# print(list1)
# print(list2)
# # 结果是：
# # [1, 2, 3, [4, 5, 6]]
# # [1, 2, 3, [4, 5, 6]]

# list1 = [1, 2, 3, [4, 5]]
# list2 = copy.deepcopy(list1)
# list1[3].append(6)
# print(list1)
# print(list2)
# # 结果是：
# # [1, 2, 3, [4, 5, 6]]
# # [1, 2, 3, [4, 5]]

# def main():
#     for i in range(3):
#         list = CreateRandomArray()
#         BubbleSort(list)
#
# if __name__ == '__main__':
#     main()

