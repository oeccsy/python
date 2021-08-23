tuple1 = (1, 2, 3, 4)
# tuple1[0] = 2 # Error!
# 한번 정하면 지우거나 변경할 수 없다!
# 하지만 같은 이름을 다른 튜플로 정의는 가능하다 ex) tuple1 = (1,2,3,4,5)

print(tuple1[1])    # 2
# tuple 인덱싱

print(tuple1[0:2])  # (1, 2)
# tuple 슬라이싱

tuple2 = tuple1 + tuple1
print(tuple2)       # (1, 2, 3, 4, 1, 2, 3, 4)
# tuple 더하기

tuple2 = tuple1 * 3 # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
print(tuple2)
# tuple 곱하기

print(len(tuple2))  # 12
# tuple 길이 구하기