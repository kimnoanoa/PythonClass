# 리스트 연산

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)  # [1, 2, 3, 4, 5, 6]
print(a * 3)
print('len(a) = ', len(a))

# print(a + 'hi')
# print(a[2] + 'hi')
print(str(a[2]) + 'hi')

print()
print("-----리스트 수정과 삭제-----")
a = [1, 2, 3]
a[2] = 4
print(a)  # [1, 2, 4]
del a[1]
print(a)  # [1, 4]

print()
a = [1, 2, 3, 4, 5]
del a[2:]
print(a) # [1, 2]

print()
print("-----리스트 관련 함수-----")

# append
a = [1, 2, 3]
a.append(100)
print(a)
a.append([7, 9])
print(a)
print()

# sort
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'b', 'c']
a.sort()
print(a)

# reverse
a = ['a', 'c', 'b']
a.reverse()
print(a)  # b c a
print()

# index
a = [5, 6, 7]
print(a.index(6))
# print(a.index(8))  -- ValueError: 8 is not in list
print()

# insert
a = [1, 2, 3]
a.insert(0, 4)
print(a)  # [4, 1, 2, 3]
a.insert(3, 5)
print(a)  # [4, 1, 2, 5, 3]
print()

# remove
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)  # [1, 2, 1, 2, 3]
a.remove(3)
print(a)  # [1, 2, 1, 2]
print()

# pop
a = [1, 2, 3]
print(a.pop())
print(a)

a = [1, 2, 3]
print(a.pop(1))
print(a)
print()

# count
a = [1, 2, 3, 1]
print(a.count(1))

# extend
a = [1, 2, 3]
a.extend([4, 5])
print(a)

a = [1, 2, 3]
a = a + [4, 5]
print(a)
b = [6, 7]
a.extend(b)
print(a)


