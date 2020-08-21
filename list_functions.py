#list_functions.py

def number_of_odds(nums):
    counter = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            counter += 1
    return counter
    

def first_or_last(nums, value):
    if value == (nums[0] or nums[-1]):
        return True
    else:
        return False

def mult(nums):
    mult = 1
    for i in range(len(nums)):
        mult = nums[i] * mult
    return mult

def sort_and_square():
    lists = []
    squares = []
    for i in range(10):
        num = int(input("Give me a number: "))
        lists.append(num)
    for i in range(len(lists)):
        squares.append(lists[i] ** 2)
    return squares