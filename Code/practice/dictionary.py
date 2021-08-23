# dictionary : key와 value가 있는 자료구조 (주로 API에 자주 활용)
# key는 중복되면 안된다


a = {
    'name': 'Eric',
    'age': 15
}
print(a['name'])    #Eric
# dictionary 형식은 key값으로 value에 접근 가능


print(a.get('naaaame')) #None
# dict.get(key) 를 사용하면 dictionary에 해당 key가 없을 경우 None 출력


a = {
    'name': 'Eric',
    'age': 15
}
a['phone'] = "01011112222"
print(a)    # {'name': 'Eric', 'age': 15, 'phone': '01011112222'}
# dictionary에 항목 추가


del a['name']
print(a)    # {'age': 15, 'phone': '01011112222'}
# dictionary 항목 삭제


print(a.keys())     # dict_keys(['age', 'phone'])
print(a.values())   # dict_values([15, '01011112222'])
print(a.items())    # dict_items([('age', 15), ('phone', '01011112222')])
# key값들 출력 / value값들 출력 / key,value 쌍을 튜플 형태로 출력


a.clear()
print(a)    # {}
# dictionary의 모든 key, value 값들 삭제


print('age' in a)   # False
a = { 'age' : 15 }
print('age' in a)   # True
# dictionary안에 어떤 Key가 있는지 조사