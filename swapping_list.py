def swap(list):
    temp_val=list[0]
    list[0]=list[len(list)-1]
    list[len(list)-1]=temp_val
    return list
list=[1,2,3,4,5,6]
print(swap(list))