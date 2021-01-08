# x = 'frog'
# print(x[3])
#
# x = ['pig', 'cow', 'horse']
# print(x[1])
#
# x = ('Kevin', 'Niklas', 'Jenny', 'Craig')
# print(x[0])
# print(x[1:3:2])
#
# # slicing
# # [start : end+1 : step]
# # start inclusive, end non-inclusive, step is by default 1
# x = 'computer'
# print(x[1:1])
# print(x[1:6:2])
# print(x[-3:])
# print(x[:5])
# print(x[:-2])

# x = 'horse' + 'shoe'
# print(x)
#
# y = ['pig', 'cow'] + ['horse']
# print(y)
#
# # to be 'Craig' considered a tupple , has to be included
# z = ('Kevin', 'Niklas', 'Jenny') + ('Craig',)
# print(z)

# x = 'bug' * 3
# print(x)
# y = [8, 5] * 3
# print(y)
# z = (2, 4) * 3
# print(z)

# x = 'bug'
# print('u' in x)
#
# y = ['pig', 'cow', 'horse']
# print('cow' not in y)
#
# z = ('Kevin', 'Nikklas')
# print('Kevin' in z)

# x = [7, 8, 3]
# for item in x:
#     print(item)
#
# y = [7, 8, 3]
# # enumerate returns index and item
# for index, item in enumerate(y):
#     print(index, item)

# count - len function
# x = 'bug'
# print(len(x))
#
# y = ['pig', 'cow', 'horse']
# print(len(y))
#
# z = ('Kevin', 'Niklas')
# print(len(z))

# # find minimum item in a sequence lexicographically - min function
# # find maximum item in a sequence lexicographically - max function
# x = 'bug'
# print(min(x))
#
# y = ['pig', 'cow', 'horse']
# print(min(y))
#
# z = ('Kevin', 'Nikklas')
# print(min(z))

# y = [2, 5, 8, 12]
# print(sum(y))
# # sum only last 2 items
# print(sum(y[-2:]))
#
# # sorted function returns a new list - it does not sort the originl list
# y = ['pig', 'cow', 'horse']
# print(sorted(y))

# z = ('Kevin', 'Niklas', 'Craig', 'Jenny')
# print(sorted(z, key=lambda  k: k[0]))

# z = ('Kevin', 'Nikklas')
# print(z.count('Kevin'))

# # index of the first occurence of an item
# x = 'hippo'
# print(x.index('p'))

# # unpacking
# x = ['pig', 'cow', 'horse']
# a, b, c = x
# print(a, b, c)
# print(b)

# empty list, no parameters
# x = list()
# y = ['a', '25', 'dog', 8.43]
#
# tuple1 = (10, 20)
# z = list(tuple1)
#
# # list comprehension
# a = [m for m in range(8)]
# print(a)
#
# b = [i**2 for i in range(10) if i>4]
# print(b)

# x = [5, 3, 8, 6]
# del(x[1])
# del(x) # delete the entire list
# # x.append(7)
#
# # extend - combine 2 lists into 1
# a = [5, 4, 3]
# b = [1, 2, 3]
# a.extend(b)
# print(a)

# # insert - insert an item at a given index
# x = [5, 3, 8, 6]
# x.insert(1, 7)
# print(x)

# # pop - pops last item off list and returns item
# x = [5, 3, 8, 6]
# x.pop()
# print(x)
# print(x.pop())

# # remove - remove first instance of an item
# x = [5, 3, 8, 6, 3]
# x.remove(3)
# print(x)

# # reverse - reverse the order of the list
# x = [5, 3, 8, 6]
# x.reverse()
# print(x)

# # sort the list in place
# x = [5, 3, 8, 6]
# x.sort()
# print(x)
#
# # descending sort
# y = [5, 3, 8, 6]
# y.sort(reverse=True)
# print(y)


# x = ()
# y = (1, 2, 3)
# # parenthesis are optional
# z = 1, 2, 3
# a = 2,
#
# list1 = [2, 4, 6]
# j = tuple(list1)

# y = ([1, 2], 3)
# # take the 0th item and delete the first item in it (number 2)
# # if you have a list in a tupple, you can change it
# del(y[0][1])
#
# # merge two tupples into one
# y += (4, )
# print(y)

# sets store non-duplicate items
# fast access vs lists
# math set ops (union, intersect)
# unordered

# few ways to create a new set
# x = {3, 5, 3, 5}
# print(x)
#
# y = set()
#
# list1 = [2, 3, 4]
# z = set(list1)
#
# x = {3, 8, 5}
# x.add(3)
# x.remove(4)
# print(len(x))
# print(5 in x)
# # pop random item from set x, returns a random item and set
# print(x.pop(), x)
# # delete all items
# x.clear()

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
#
# # intersection (AND): set1 & set2
# print(s1 & s2)
# # union(OR): set1 | set2
# print(s1 | s2)
# # symmetric difference (XOR):
# # set1 ^ set2 difference (in set1 but not in set2): set1 - set2
# print(s1 ^ s2)
# # subset (set2 contains set1): set1 <= set2
# print(s1 <= s2)
# # superset (set1 contains set2): set1 >= set2
# print(s1 >= s2)

# # dictionary
# # in Java HashMap, associative array
# # unordered
x = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
# # passing tupples to dictionary
# y = dict([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)])
# z = dict(pork=25.3, beef=33.8, chicken=22.7)

# # add or update
# x['shrimp'] = 38.2
# del(x['shrimp'])
# print(len(x))
# # delete all items
# x.clear()
# # delete dict x
# del(x)

# y = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
# print(y.keys())
# print(y.values())
# print(y.items())
#
# # check membershp in y_keys (only keys, not values)
# print('beef' in y)
#
# # check membership in y_values
# print('clams' in y.values())
#
# # iterating a dict
# for key in y:
#     print(key, y[key])
#
# for k, v in y.items():
#     print(k, v)































