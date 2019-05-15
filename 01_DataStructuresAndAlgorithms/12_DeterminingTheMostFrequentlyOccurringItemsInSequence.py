from collections import Counter

# 시퀀스에 가장 많은 아이템 찾기

word_list = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

more_word_list = [
    'look', 'into', 'my', 'eyes'
]

word_counts = Counter(word_list)
print('before update')
print(type(word_counts))
print(word_counts)
print(word_counts['eyes'])

print('after update')
word_counts.update(more_word_list)
print(type(word_counts))
print(word_counts)
print(word_counts['eyes'])

top_three = word_counts.most_common(3)
print(type(top_three))
print(type(top_three[0]))
print(top_three)

# Counter 인스턴스에는 수식도 사용 가능하다
a = Counter(word_list)
b = Counter(more_word_list)
print(a)
print(b)
c = a + b
print(c)
d = a - b
print(d)
e = b - a
print(e)
