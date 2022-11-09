import os, time
input = []
a = 0
depth = 0
horizontal = 0
aim = 0

with open("moves.txt", "r") as file:
    for line in file:
        input.append((line).strip())


for i in input:
    instruct = []
    instruct = i.split(" ")

    act = instruct[0]
    move = int(instruct[1])
    print(instruct)

    if act[0] == "f":
            horizontal = horizontal + move
            depth = depth + (aim * move)
    elif act[0] == "u":
            aim = aim - move
    elif act[0] == "d":
            aim = aim + move
            print("d", depth)
    a += 1

print(depth)
print(horizontal)

mult = depth * horizontal

file.close()

print(f"The answer is {mult}")
