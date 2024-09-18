"""
Bubble Sort
4 2 6 5 1 3
(2 4) 6 5 1 3
2 (4 6) 5 1 3
2 4 (5 6) 1 3
2 4 5 (1 6) 3
2 4 5 1 (3 6)     sorted: 6

(2 4) 5 1 3 6
2 (4 5) 1 3 6
2 4 (1 5) 3 6
2 4 1 (3 5) 6     sorted: 5 6

(2 4) 1 3 5 6
2 (1 4) 3 5 6
2 1 (3 4) 5 6     sorted: 4 5 6

(1 2) 3 4 5 6
1 (2 3) 4 5 6     sorted: 3 4 5 6

(1 2) 3 4 5 6     sorted: 2 3 4 5 6

1 2 3 4 5 6       sorted completely
"""

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp

tmp_list = [4,2,6,5,1,3]
bubble_sort(tmp_list)
print(tmp_list)