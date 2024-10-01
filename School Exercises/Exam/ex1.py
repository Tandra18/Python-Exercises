#merge and sort lists
def merge_and_sort(list1,list2):
    merged_list = list1 + list2

    sorted_list = sorted(set(merged_list))
    return sorted_list

list1 = [3,1,4,2]
list2 = [4,5,6,1]
print(merge_and_sort(list1,list2))