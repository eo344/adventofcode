import os, time

print (f"{'Sonar Sweep Report':^35}")

input = []

with open("input.txt", "r") as file:
    for line in file:
        input.append(int(line))

a = 0
b = 0
for i in range(len(input)-1):
    if input[i] < input[i+1]:
        a += 1
    elif input[i] > input[i+1]:
        b += 1
    


print (f"The number of increases is: {a}")
print (f"The number of decreases is: {b}")
