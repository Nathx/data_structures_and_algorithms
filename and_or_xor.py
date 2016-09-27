# https://www.hackerrank.com/challenges/and-xor-or

def max_xor(seq):
    stack = []
    max_xor = 0
    for elem in seq:
        while stack:
            prev = stack[-1]
            max_xor = max(max_xor, elem ^ prev)
            if prev >= elem:
                stack.pop()
            else:
                break
        stack.append(elem)
    return max_xor


if __name__ == '__main__':
    n = int(raw_input())
    seq = map(int, raw_input().split())
    print max_xor(seq)
