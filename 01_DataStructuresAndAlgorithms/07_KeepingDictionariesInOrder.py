from collections import OrderedDict

# 딕셔너리 순서 유지

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

e = OrderedDict()
e['fooo'] = 1
e['barr'] = 2
e['spamm'] = 3
e['grokk'] = 4

for key in e:
    print(key, e[key])
