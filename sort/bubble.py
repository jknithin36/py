# def bubbleSort(list):
#     for i in range(len(list)-1):
#         for j in range(len(list)-i-1):
#             if list[j] > list[j+1]:
#                 list[j] , list[j+1] = list[j+1], list[j]
#     print(list)



# bubbleSort([9,8,7,4,1,2,5])




# Implement Bubble Sort

# Optimize Bubble Sort

# Compare Bubble Sort with Insertion/Selection Sort

# Time & space complexity analysis

# Trace Bubble Sort on an input (dry run)

# Modify it to sort in descending order








# Implement bubble sort


def bubbleSort(list):
    if not list:
        return 
    for i in range(len(list)-1):
        for j in range(len(list) - i -1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    print(list)




bubbleSort([2,4,6,1,3])


# Optimize Bubble Sort


def OptimizeBubbleSort(list):
    for i in range(len(list)-1):
        swapped = False
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
        if not swapped: # if swap happens it will be always Trur True opposite is fale if false break never run
            break
    print(list)
            




