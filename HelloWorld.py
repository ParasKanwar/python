name = input("Enter any String :: ")


def count(name):
    collection = {}
    inverse = {}
    max1 = 0
    for char in name:
        if char not in collection:
            collection[char] = 1
        elif char in collection:
            collection[char] += 1
        if collection[char] > max1:
            max1 = collection[char]
            inverse.clear()
            inverse[collection[char]] = char

    return inverse, max1


# collection1 = count(name)
# max = 0
# character = ""
# for key in collection1:
#     if(collection1[key] > max):
#         max = collection1[key]
#         character = key


# print(character)
x, y = count(name)
z = x[y]
print(z)

# objects = [("chaddi", 800),
#            ("banyan", 801), ("shirt", 810), ("tshirt", 890), ("jeans", 850)]
# # objects.sort(key=lambda item: item[1])
# # print(objects)

# # x = filter(lambda items: items[1] >= 801, objects)
# # print(*x)

# map = [item for item in objects if item[1] > 801]
# print(map)
