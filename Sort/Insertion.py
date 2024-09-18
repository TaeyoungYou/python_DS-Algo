def my_insertion_sort(my_list):
    for i in range(1, len(my_list)):
        for j in range(i-1, -1, -1):
            if my_list[i] < my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list
print(my_insertion_sort([2,1,4,3,5,6]))

"""
Insertion Sort
항상 인덱스 1부터 시작
현재 인덱스 - 1부터 0으로 이동
이동 도중 자신의 값이 작으면 스왑
앞에 값이 자신보다 작으면 스탑
"""

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list
print(insertion_sort([3,5,1,2,6,4]))