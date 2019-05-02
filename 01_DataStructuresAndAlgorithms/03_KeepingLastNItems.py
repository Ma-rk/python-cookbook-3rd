from collections import deque


# 마지막 N개 아이템 유지
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('exam_file.txt') as f:
        for line, prev_lines in search(f, 'python', 5):
            for pline in prev_lines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
