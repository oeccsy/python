a = []
b = [a]
c = ['a']
d = [1, 2, 'three', [4, 5]]
print(a)    # []
print(b)    # [[]]
print(c)    # ['a']
print(d)    # [1, 2, three, [4, 5]]
# list의 표현

a = [0, 1, 2, 3, 4, 5]
print(a[0:3])
# list도 슬라이싱 가능


a.append("추가")
print(a)
# list.append(value) : list에 항목 추가


a = ['a', 'eb', 'cd', 'd1']
a.sort()
print(a)
# list.sort() : list 정렬, int형 str형을 혼합한 경우는 에러 발생


a.reverse()
print(a)
# list.reverse() : 뒤집기


print(a.index('a'))
# list.index(value) : list에 어떤 값이 있는지 확인하여 해당 인덱스 반환



a.insert(0, 'asdf')
print(a)
# list.insert(int, value) : list의 int번째 인덱스에 value 삽입 (해당 인덱스 이후는 한칸씩 뒤로 밀림)


a.remove('asdf')
print(a)
# list.remove(value) : list에서 어떤 값이 처음 등장하는 항을 제거


a.pop()
print(a)
# list.pop() : list의 마지막 항 제거


print(a.count('cd'))
# list.count(value) : list에 어떤 값이 몇개 있는지 반환


a = [1,2,3]
b = [1,2,3]
c = [1,2,3]

a = a + a
b.extend(b)
c.extend([1,2,3])

print(a)
print(b)
print(c)
# list.extend(list) : list와 다른 list를 연결 (list + list)