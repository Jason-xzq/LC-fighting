from collections import defaultdict

dict = {1: "apple", 2: "pear", 3: "banana"}
list = ["apple", "pear", "banana"]
list.sort(key = lambda s:len(s))
print(list)

name = "abcdef"
print(name[:2])
print(name[2:])
print(name[:])

dict= defaultdict(int)
print(dict[1])
print(dict[2])
print(dict)

word = "s"
print(word[:1])
# print(type(dict.keys()))
# for i in dict.keys():
#     print(type(i))
#     print(i)

print(5//2)