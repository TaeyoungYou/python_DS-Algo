def print_items01(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

print_items01(10, 10)
"""
O(a) + O(b) = O(a + b)
"""

def print_items02(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)

print_items02(10,10)
"""
O(a) * O(b) = O(a * b)
"""