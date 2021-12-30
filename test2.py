from collections import defaultdict

# dict = {1: "apple", 2: "pear", 3: "banana"}
# list = ["apple", "pear", "banana"]
# list.sort(key = lambda s:len(s))
# print(list)
#
# name = "abcdef"
# print(name[:2])
# print(name[2:])
# print(name[:])
#
# dict= defaultdict(int)
# print(dict[1])
# print(dict[2])
# print(dict)
#
# word = "s"
# print(word[:1])
# # print(type(dict.keys()))
# # for i in dict.keys():
# #     print(type(i))
# #     print(i)
#
# print(5//2)
#
#
# index = 0
# for i in range(5):
#     index += i
#     print(i)
#
# print(index)
# print(i)

# print(float('inf'))
# print(type(float('inf')))
# print(float('INF'))
# dp = [0] * 5
# print(dp)

# dp = [[0]*2 for i in range(3)]
# print(dp)

# dict = {}
# dict[1] = 1
# if 1 in dict:
#     print("bingo!")

#
# a = 3
# b = 2
# a, b = b, max(a, b)
# print("a: " + str(a))
# print("b: " + str(b))

# s = "0123"
# if s[0] == "0":
#     print(int(s[0:]))
#     print(type(int(s[0:])))

# m, n = 3, 7
# dp = [[0]*(n+1) for _ in range(m+1)]
# print(dp)

# from collections import deque
# q = deque([1])
# print(len(q))
# q.append(3)
# print(len(q))
# q.append(None)
# print(len(q))
# print(q)

levels = []
level = 0
levels.append([])
levels[level].append(1)
levels[level].append(2)
print(levels)