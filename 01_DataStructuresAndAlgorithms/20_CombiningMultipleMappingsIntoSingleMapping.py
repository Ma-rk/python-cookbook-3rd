from collections import ChainMap

# 딕셔너리나 매핑이 여러개 있고, 자료 검색이나 데이터 확인을 위해 하나의 매핑으로 합치고 싶다.

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c['x'])
print(c['y'])  # a 와 b 양쪽에 있는 키일땐 c를 만들 때 앞에 명시한 a의 값이 이용된다
print(c['z'])

print(len(c))  # 3
print(list(c.keys()))  # ['x', 'y', 'z']
print(list(c.values()))  # [1, 2, 3]

c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y']

# update()를 이용해 딕셔너리를 하나로 합칠 수도 있다.
aa = {'x': 11, 'z': 33}
bb = {'y': 22, 'z': 44}
merged_dict = dict(bb) # merged_dict 는 완전히 새로운 객체이기 때문에 merged_dict의 변경과 aa, bb의 변경은 서로 영향을 주지 않는다.
merged_dict.update(aa)

print(merged_dict['x'])
print(merged_dict['y'])
print(merged_dict['z'])

merged_dict['x'] = 111
print(merged_dict['x'])
print(aa['x'])
