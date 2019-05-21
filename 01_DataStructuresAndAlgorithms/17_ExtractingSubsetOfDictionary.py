# 딕셔너리의 부분 추출

# dictionary comprehension 을 사용하면 간단하게 해결 가능
price_dict = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

up_200_dict = {key: value for key, value in price_dict.items() if 200 < value}

print('up_200')
print(up_200_dict)

tech_name_list = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
tech_name_dict = {key: value for key, value in price_dict.items() if key in tech_name_list}
print('tech_name_dict')
print(tech_name_dict)
