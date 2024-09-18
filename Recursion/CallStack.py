def funcThree():
    print("Three")

def funcTwo():
    funcThree()
    print("Two")

def funcOne():
    funcTwo()
    print("One")

funcOne()

"""
작동 방식: 
    1. call funcOne()
    2. call funcTwo()
    3. call funcThree()
    4. print "Three"
    5. return funcThree()
    6. back to funcTwo()
    7. print "Two"
    8. return funcTwo()
    9. back to funcOne()
    10. print "One"
    11. return funcOne()
    12. Done
"""