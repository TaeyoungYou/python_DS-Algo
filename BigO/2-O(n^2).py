def print_items(n):
    # nested for loop
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)

"""
O(n*n) = O(n^2)
"""