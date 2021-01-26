listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

oddElements = listOne[1::2]
print("Elements at odd-index positions from list one")
print(oddElements)

evenElements = listTwo[0::2]
print("Elements at even-index positions from list two")
print(evenElements)

List = [54, 44, 27, 79, 91, 41]

element = List.pop(4)
List.insert(2, element)
List.append(element)

List = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print(List[:3])
print(List[3:6])
chunk3 = List[6:9]
print(chunk3)
chunk3.reverse()
print(chunk3)

list1 = [2, 4, 6]
list2 = [1, 3, 5]

for i in list1:
    list2.append(i)
print(list2)

