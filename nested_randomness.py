# https://community.topcoder.com/stat?c=problem_statement&pm=1771&rd=4570

# Consider a function randomInt(integer N) that takes an integer N and returns
# an integer uniformly at random in the range 0 to N-1. If that function is
# nested, as in randomInt(randomInt(N)), the probability distribution
# changes, and some numbers are more likely than others. Given an int
# nestings defining the number of times the function is nested (1 indicates
# randomInt(N), 2 indicates randomInt(randomInt(N)), and so on), an int
# N and an int target, return the probability that the result of nestings
# nested calls to randomInt with the parameter N will result in target.

def nested_randomness(N, nestings, target):
    if N - nestings < target:
        return 0
    elif nestings == 1:
        return 1. / N
    else:
        return (1. / N) * sum([nested_randomness(k, nestings - 1, target)
                        for k in range(target + nestings - 1, N)])

if __name__ == '__main__':
    print nested_randomness(5, 2, 1) # 0.21666666666666667
    print nested_randomness(10, 4, 0) # 0.19942680776014104
    print nested_randomness(1000, 10, 990) # 1.0461776397050886E-30
