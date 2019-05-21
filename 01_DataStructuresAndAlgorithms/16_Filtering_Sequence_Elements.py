# 시퀀스 필터링

my_list = [1, 4, -5, 10, -7, 2, 3, -1]

# 가장 간단한 방범: list comprehension
bigger_then_zero = [n for n in my_list if 0 < n]
print(bigger_then_zero)
smaller_then_zero = [n for n in my_list if n < 0]
print(smaller_then_zero)

# 결과로 생성되는 리스트가 너무 크면 메모리나 시간 측면에서 한번에 리스트로 반환받기가 부담스러울 수가 있다.
# 그럴땐 list comprehensions 대신 Generator expressions을 쓰자.
bigger_generator = (n for n in my_list if 0 < n)
print(bigger_generator)
for item in bigger_generator:
    print(item)

print()

smaller_generator = (n for n in my_list if n < 0)
print(smaller_generator)
for item in smaller_generator:
    print(item)

print()

# 필터링 도중에 예외 처리를 해야 한다거나 복잡한 내용이 들어갈 땐
# 필터링 로직을 구현한 함수를 만들고 filter()를 쓰자
value_list = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(value):
    try:
        _ = int(value)
        return True
    except ValueError:
        return False


int_value = filter(is_int, value_list)
print(int_value)
int_value_list = list(int_value)
print(int_value_list)

print()

# list comprehension의 데이터 변형 기능 1: 조건에 맞는 값만 골라 변형하기
my_list_2 = [1, 4, -5, 10, -7, 2, 3, -1]
import math

square_root_list = [math.sqrt(n) for n in my_list_2 if 0 < n]
print(square_root_list)

# list comprehension의 데이터 변형 기능 2: 조건에 맞지 않는 값은 치환하여 변형하기
clip_neg = [n if 0 < n else 0 for n in my_list_2]
print(clip_neg)
clip_pos = [n if n < 0 else 0 for n in my_list_2]
print(clip_pos)

print()
print('compress')
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',  # bigger than 5
    '2122 N CLARK'
    
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',  # bigger than 5
    '4801 N BROADWAY',  # bigger than 5
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4,
          1, 7, 6, 1]

from itertools import compress

bigger_than_5 = [5 < n for n in counts]
print(bigger_than_5)
bigger_than_5_compress = compress(addresses, bigger_than_5)
print(bigger_than_5_compress)
bigger_than_5_compress_list = list(bigger_than_5_compress)
print(bigger_than_5_compress_list)
