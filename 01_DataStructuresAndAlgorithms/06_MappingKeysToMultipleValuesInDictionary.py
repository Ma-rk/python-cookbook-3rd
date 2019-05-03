from collections import defaultdict

# 딕셔너리의 키를 여러 값에 매핑하기

a = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

b = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['b'].append(4)
print(d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e[''].add(4)
e[''].add(4)
print(e)

pairs = []

# 딕셔너리로 다음 작업을 수행할 때 일반 딕셔너리일때의 예제 코드
f = {}
for key, value in pairs:
    if key not in f:
        d[key] = []
    d[key].append()

# 딕셔너리로 다음 작업을 수행할 때 defaultdict 를 이용할 때의 예제 코드
# (if 체크를 안해도 됨)
g = defaultdict(list)
for key, value in pairs:
    d[key].append()
