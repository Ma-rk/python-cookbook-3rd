# 문자열의 처음이나 마지막에 파일 확장자, URL스킴 등
# 특정 텍스트 패턴이 포함되었는지 검사하고 싶다

file_name = 'sample.txt'
print(file_name.endswith('.txt'))

url = 'http://www.python.org'
print(url.startswith('http:'))

# 다음과 같이 사용할 수 있지만 위 방법보다 더 느리고 코드도 복잡하다

print(file_name[-4:] == '.txt')

print(url[:5] == 'http:' or url[:6] == 'https:')
