def my_selection_sort(my_list):
    for i in range(len(my_list)):
        min = i
        for j in range(i,len(my_list)):
            if my_list[min] > my_list[j]:
                min = j
        
        temp = my_list[i]
        my_list[i] = my_list[min]
        my_list[min] = temp

need_to_sort = [2,1,5,6,4,3]
my_selection_sort(need_to_sort)
print(need_to_sort)

"""
먼저 가장 작은 값의 인덱스를 순회를 해서 찾는다
그리고 나중에 첫번째 인덱스와 자리를 바꾼다
"""

def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list
print(selection_sort([3,5,1,6,2,4]))