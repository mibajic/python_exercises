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



































