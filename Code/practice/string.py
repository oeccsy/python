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


a = "aaaaabbbccd"
print(a.count('aa'))                        # 2
# string.count(string) : 문자열에 어떤 문자열이 몇개 있는지를 반환


a = "aaaaabbbccd"
print(a.find('b'))
# string.find(string) : 문자열에서 어떤 문자열이 처음 등장하는 위치를 반환


a = ','.join('12345')
print(a)
# string1.join(string2) : string2 사이사이에 string1 삽입


a = '        HI       ~'                    #HI       ~
print(a.strip())
# string.strip() : 공백 제거 (문자열의 앞부분만 없어지는것 같다.)


a = 'I love Icecream'
print(a.replace('Icecream', 'pizza'))
# string.replace(string, string) : 문자열 교체


a = "a b c d e fg"
print(a.split())
# string1.split(string2) : string1을 string2를 기준으로 구분하여 list로 만든다. (string2가 없을 경우 공백)