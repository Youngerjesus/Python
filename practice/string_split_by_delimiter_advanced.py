import re

with open("text.txt") as file:
    count = 0

    for line in file.readlines():
        replaceLine = line.replace(",", " ")
        split = replaceLine.split(" ")
        count += len(split)

    print(f"count: {count}")

with open("text.txt") as file:
    txt = file.read()

txt = txt.replace(",", ' ')
split = txt.split(' ')
count2 = len(split)

print(f"count: {count2}")
