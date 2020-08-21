import random

min = random.randint(1, 10)
max = random.randint(90, 100)
rando = random.randint(min, max)
picked = False
counter = 0
while picked == False:
    num = int(input("Pick an number that you think is in range. "))
    if num != rando:
        counter = counter + 1
    if num < rando:
        print("Too low")
    if num > rando:
        print("Too high")
    if num == rando:
        picked = True
print("You got the number!")
print("It took you", str(counter), "tries!")
