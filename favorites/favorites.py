import csv

with open('favorites.csv', 'r') as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["problem"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

favorite = input('Favorite: ')
if favorite in counts:
    print(f"{favorite}: {counts[favorite]}")


# CLARIFY
# 2 ways to do the same
# def get_value(language):
#     return counts[language]

# lambda language: counts[language]

# for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
#     print(f"{favorite}: {counts[favorite]}")
