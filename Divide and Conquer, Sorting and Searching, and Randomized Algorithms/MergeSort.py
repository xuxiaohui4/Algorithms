# -*- coding: utf-8 -*-

import pdb
import sys

def MergeSort(list_sort: list):
    list_length = len(list_sort)

    if list_length == 1:
        return list_sort
    else:
        result = []
        first_half = MergeSort(list_sort[:list_length // 2])
        second_half = MergeSort(list_sort[list_length // 2 :])
        loop_num = max(len(first_half), len(second_half))

        j, k = (0, 0)
        for i in range(list_length):
            if j == len(first_half):
                result.append(second_half[k])
                k += 1
                continue
            if k == len(second_half):
                result.append(first_half[j])
                j += 1
                continue
            if first_half[j] < second_half[k]:
                result.append(first_half[j])
                j += 1
            else:
                result.append(second_half[k])
                k += 1
        print(result)
        return result

def Sort_And_Count(list_sort_count: list):
    if len(list_sort_count) == 1:
        return list_sort_count,0
    else:
        result = []
        index = len(list_sort_count) // 2
        first_half, x = Sort_And_Count(list_sort_count[:index])
        second_half, y = Sort_And_Count(list_sort_count[index:])
        loop_num = max(len(first_half), len(second_half))

        j, k = (0, 0)
        z = 0
        for i in range(len(list_sort_count)):
            if j == len(first_half):
                result.append(second_half[k])
                k += 1
                continue
            if k == len(second_half):
                result.append(first_half[j])
                j += 1
                continue
            if first_half[j] < second_half[k]:
                result.append(first_half[j])
                j += 1
            else:
                result.append(second_half[k])
                z += len(first_half) - j
                k += 1
        #pdb.set_trace()
        print(list_sort_count, first_half, second_half, x + y + z)
        return result, x + y + z

def Count_Inv_BF(list_count: list):
    i, j = 0, 0
    count = 0
    for i in range(len(list_count)):
        for j in range(i, len(list_count)):
            if list_count[i] > list_count[j]:
                count += 1
                print(list_count[i], ">", list_count[j])
    return count


if __name__ == "__main__":
    list_sort = [10, 2, 4, 5, 11, 33, 8, 6, 7, 9, 14, 25, 73, 64, 1, 0, 33, 27]
    print(list_sort)
    list_sorted, inversion_num = Sort_And_Count(list_sort)
    print(list_sorted, inversion_num)
    print(Count_Inv_BF(list_sort))
