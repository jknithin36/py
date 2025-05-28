def budgeting_tool(items, target):
    items.sort()
    i , j = 0 , len(items) -1 

    while i>j:
        sum = items[i] + items[j]
        if sum == target:
            return (items[i]+ items[j])
        elif sum < target:
             i+=1
        else:
             j-=1

    return "Not Found"


f = budgeting_tool([5, 20, 35, 40, 60], 60)
print(f)


    


            
            





