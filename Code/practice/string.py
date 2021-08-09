a= """
Hello 

World
"""
print(a)
# 3줄에 걸쳐서 출력, " ~ " 에서는 불가능한 기능


b = "test"
print (a+b)
# 문자열 덧셈 -> 문자열 연결

print(a[0])
print(a[5])
print(a[10])
print(a[-1])
# 문자열 인덱싱, 음수의 경우 뒤에서 부터 카운트

a = "0123456789"
print(a[4:7])
print(a[::-1])
print(a[::-2])
print(a[::1])
print(a[::2])
# 슬라이싱, a 슬라이싱 예시 a[이상:미만:간격]

num = 7
a = "num is %d %s" % (num, "Wow!")          # num is 7 Wow!
b = "num is {} {}".format(num, "Wow!")      # num is 7 Wow!
c = f"num is {num}"                         # num is 7
d = "%0.4f" % 0.123456789                   # 0.1234
print(a)
print(b)
print(c)
print(d)
# 문자열 포매팅, %d:정수 %f:실수 %s:문자열 %c:문자