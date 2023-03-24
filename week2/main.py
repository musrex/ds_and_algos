s = []

data = open("Lopez_Family_Farm.csv", "r")

for line in data:
    line = line.split(',')
    print(line)