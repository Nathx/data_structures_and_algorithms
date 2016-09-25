# https://www.hackerrank.com/challenges/poisonous-plants

class Plant(object):
    def __init__(self, value, days):
        self.value = value
        self.days = days

def find_max_days(lst):
    max_days = 0
    stack = []

    for pest in lst:
        days = 0
        while stack and stack[-1].value >= pest:
            days = max(days, stack.pop().days)

        if not stack:
            days = 0
        else:
            days += 1

        stack.append(Plant(pest, days))
        max_days = max(max_days, days)

    return max_days

if __name__ == '__main__':
    n = int(raw_input())
    lst = map(int, raw_input().split())
    print find_max_days(lst)
