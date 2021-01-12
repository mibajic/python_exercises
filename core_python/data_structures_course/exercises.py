# def sum_list():
#     items_list = [1, 2, 3, 4, 5]
#     sum_numbers = 0
#     for i in items_list:
#         sum_numbers += i
#     return sum_numbers
#
#
# print(sum_list())
#
#
# def multiply_list():
#     items_list = [1, 2, 3]
#     multiply = 1
#     for i in items_list:
#         multiply *= i
#     return multiply
#
#
# print(multiply_list())
#
# largest_number_list = [7, -2, 89, 2, 4]
# print(max(largest_number_list))
#
#
# def match_words(words):
#     string = 0
#
#     for word in words:
#         if len(word) > 1 and word[0] == word[-1]:
#             string += 1
#     return string
#
#
# my_list = ['abc', 'xyz', 'aba', '1221', 'ab']
# print(match_words(my_list))
#
# unsorted_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# sorted_list = sorted(unsorted_list, key=lambda x: x[1])
# print(sorted_list)


# def without(duplicate_list):
#     list_without_duplicates = []
#     for i in duplicate_list:
#         if i not in list_without_duplicates:
#             list_without_duplicates.append(i)
#     return list_without_duplicates
#
#
# list_with_duplicates = [1, 1, 2, 3, 4, 4, 5]
# print(without(list_with_duplicates))
#
# my_list = []
# if not my_list:
#     print("Empty")
# else:
#     print("Not empty")

# list_one = [1, 2, 3, 4, 5]
# list_two = [5, 6, 7, 8, 9]
#
# for i in list_one:
#     if i in list_two:
#         print(i, "True")


my_list = [16, 17, 18, 19, 20]
for i, j in enumerate(my_list):
    print(i)





















