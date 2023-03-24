import random

data = []
for i in range(16):
    i = random.randint(0,99)
    if i not in data:
        data.append(i)

print(data)