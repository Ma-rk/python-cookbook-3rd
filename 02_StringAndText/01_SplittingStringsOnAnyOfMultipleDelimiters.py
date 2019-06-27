import re

# 여러 구분자로 문자열 나누기


line = 'asdf fjdk; afed, fjek,asdf,            foo'
split_list = re.split(r'[;,\s]\s*', line)
print(split_list)

# re.split()을 사용할 때, 정규표현식에 괄호-()를 사용하면 캡처 그룹이 된다.
# 캡처 그룹을 사용하면 re.split()가 리스트를 생성할 때 구분자도 포함해서 생성한다.
split_list2 = re.split(r'(;|,|\s)\s*', line)
print(split_list2)
print()
print('values')
print(split_list2[::2])
print('delimiters')
print(split_list2[1::2])

print()
# 정규표현식에 괄호를 사용해야 하지만 구분자를 포함하지 않고 결과를 생성하고 싶을 땐
# 논캡처그룹을 사용해야 한다. (?: ...) 와 같은 형태로 정규표현식을 작성한다.
split_list3 = re.split(r'(?:;|,|\s)\s*', line)
print(split_list3)
