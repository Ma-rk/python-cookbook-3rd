# 딕셔너리 계산
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# prices.values()를 key로, prices.keys()를 value로(=key와 value를 뒤집어서)
# 새로운 딕셔너리를 생성하자
zip_result = zip(prices.values(), prices.keys())
for z in zip_result:
    print(z)

# key와 value를 뒤집어 만든 zip 클래스의 객체로 min() 실행
min_price = min(zip(prices.values(), prices.keys()))
print('-> tuple of min price: {}'.format(min_price))

# key와 value를 뒤집어 만든 zip 클래스의 객체로 max() 실행
max_price = max(zip(prices.values(), prices.keys()))
print('-> tuple of max price: {}'.format(max_price))

# 다음 방법은 value만 얻거나 key만 얻거나
# 혹은 key를 얻어낸 뒤 다시 value를 얻어내야 하는 방법들이다.

# min/max 함수에 딕셔너리를 그대로 넣으면 최대/최소 키를 출력한다.
print(min(prices))
print(max(prices))

# .values()를 이용하면 최대/최소에 해당하는 값만 얻을 수 있고, 키는 제외된다.
print(min(prices.values()))
print(max(prices.values()))

# prices의 원소중 최소의 prices[k](=가격 최소) 를 가지는 원소를 출력
print('min prices[k]: {}'.format(min(prices, key=lambda k: prices[k])))
# prices의 원소중 최소의 k 를 가지는 원소(=오름차순으로 1번 순번의 key)를 출력
print('min k: {}'.format(min(prices, key=lambda k: k)))

# prices의 원소중 최대의 prices[k](=가격 최대) 를 가지는 원소를 출력
print('max prices[k]: {}'.format(max(prices, key=lambda k: prices[k])))
# prices의 원소중 최대의 k 를 가지는 원소(=오름차순으로 마지막 순번의 key)를 출력
print('max k: {}'.format(max(prices, key=lambda k: k)))
