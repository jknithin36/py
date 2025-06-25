# # in case of selecion sort we repeatedly find the minimum element and move it the sorted art of arrat and 


# # 2 parts 


# # sorted and unsorted 


# # minimum element for unsorted and add that to sorted array


# # swaps with first elemnet 


# # def SelectionSort(list):
# #     for i in range(len(list)):
# #         min_index = i
# #         for j in range(i+1, len(list)):
# #             if list[min_index] > list[j]:
# #                 min_index= j

# #         list[i], list[min_index] = list[min_index], list[i]
# #     print(list)



# # SelectionSort([2,4,6,1,3])


# # def SelectionSort(list):
# #     for i in range(len(list)):
# #         min_index = i
# #         for j in range(i+1, len(list)):
# #             if list[min_index] > list[j]:
# #                 min_index = list[j]
# #             list[i], list[min_index] = list[min_index], list[i] 




# def InsertionSort(list):
#     for i in range(1,len(list)):
#         key = list[i]
#         j = i-1
#         while j >=0 and key < list[j]:
#             list[j+1] = list[j]
#         list[j+1] = key
#     print(list)



# #

# import math

# def bucketSort(list):
#     numOfBuckets = round(math.sqrt(len(list)))
#     maxValue = max(list)
#     arr =[]
#     for i in range(numOfBuckets):
#         arr.append([]) # nested list

#     for j in list:
#         index_b = math.ceil(j * numOfBuckets/ maxValue)
#         arr[index_b-1].append(j)
    
#     for i in range(numOfBuckets):
#         arr[i]  = InsertionSort(arr[i])

#     k =0
#     for i in range(numOfBuckets):
#         for j in range(len(arr[i])):
#             list[k] = arr[i][j]
    
#     return list






# merge sort 



def mergeSort(list, l,m,r):
    n1 = m-1+1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2

    for i in range(0,n1)
    pass