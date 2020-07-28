categories = {}
with open("Training_01.txt", "r") as f:
    for line in f:
        words = line.split('/')
        if words[2] in categories:
            categories[words[2]] += 1
        else:
            categories[words[2]] = 1
print(categories)
for key in categories.keys():
    print(f"{key}: {categories[key]}")
