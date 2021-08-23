set1 = set("HELLO world")
print(set1) # {'H', ' ', 'L', 'd', 'l', 'E', 'o', 'w', 'r', 'O'}
# 대소문자를 구별하고, 중복인 원소가 없다. 순서도 없다.
# 순서가 없기 때문에 set 자료형에 인덱싱으로 접근하기 위해서는 list()나 tuple() 로 변환해야한다.

set1 = set( [1, 2, 3])
set2 = set( [2, 3, 4])

print(set1 & set2)
print(set1.intersection(set2))  # {2, 3}
# 교집합

print(set1 | set2)
print(set1.union(set2))         # {1, 2, 3, 4}
# 합집합

print(set1 - set2)
print(set1.difference(set2))    # {1}
# 차집합


set1.add(4)
print(set1)
# 값 1개 추가

set1.update([5,6])
print(set1)
# 값 2개 이상 추가

set1.remove(6)
print(set1)
# 값 제거
