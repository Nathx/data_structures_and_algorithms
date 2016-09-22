# https://community.topcoder.com/stat?c=problem_statement&pm=1889&rd=4709

# In the city, roads are arranged in a grid pattern. Each point on the grid represents a corner where two blocks meet. The points are connected by line segments which represent the various street blocks. Using the cartesian coordinate system, we can assign a pair of integers to each corner as shown below.
#
# You are standing at the corner with coordinates 0,0. Your destination is at corner width,height. You will return the number of distinct paths that lead to your destination. Each path must use exactly width+height blocks. In addition, the city has declared certain street blocks untraversable. These blocks may not be a part of any path. You will be given a String[] bad describing which blocks are bad. If (quotes for clarity) "a b c d" is an element of bad, it means the block from corner a,b to corner c,d is untraversable.
#
# Constraints
# -	width will be between 1 and 100 inclusive.
# -	height will be between 1 and 100 inclusive.
# -	bad will contain between 0 and 50 elements inclusive.
# -	Each element of bad will contain between 7 and 14 characters inclusive.
# -	Each element of the bad will be in the format "a b c d" where,
# a,b,c,d are integers with no extra leading zeros,
# a and c are between 0 and width inclusive,
# b and d are between 0 and height inclusive,
# and a,b is one block away from c,d.
# -	The return value will be between 0 and 2^63-1 inclusive.
#
# Examples
# 0)
#
# 6
# 6
# {"0 0 0 1","6 6 5 6"}
# Returns: 252
# 1)
#
# 1
# 1
# {}
# Returns: 2
# Four blocks aranged in a square. Only 2 paths allowed.
# 2)
#
# 35
# 31
# {}
# Returns: 6406484391866534976
# Big number.
# 3)
#
# 2
# 2
# {"0 0 1 0", "1 2 2 2", "1 1 2 1"}
# Returns: 0



from collections import defaultdict

def avoid_roads(w, h, blocked):
    path_cnt = [[0]*(w+1) for _ in range(h+1)]

    blck_dict = defaultdict(list)

    for blck in blocked:
        a, b, c, d = map(int, blck.split())
        blck_dict[(c, d)].append((a, b))
        blck_dict[(a, b)].append((c, d))

    path_cnt[0][0] = 1

    n = max(w, h) + 1
    for i in range(n):
        for j in range(i, n):
            if j > 0:
                if j <= w and i <= h and \
                    not (i, j-1) in blck_dict[(i, j)]:
                    path_cnt[i][j] += path_cnt[i][j-1]
                if j <= h and i <= w and \
                    not (j-1, i) in blck_dict[(j, i)]:
                    path_cnt[j][i] += path_cnt[j-1][i]
            if i > 0 and i != j:
                if j <= w and i <= h and \
                    not (i-1, j) in blck_dict[(i, j)]:
                    path_cnt[i][j] += path_cnt[i-1][j]
                if j <= h and i <= w and \
                    not (j, i-1) in blck_dict[(j, i)]:
                    path_cnt[j][i] += path_cnt[j][i-1]
    print '\n'.join(['   '.join(map(str, row)) for row in path_cnt[::-1]])

    return path_cnt[h][w]

if __name__ == '__main__':
    test_args = [
        (6, 6, ["0 0 0 1","6 6 5 6"]),
        (1,1,[]),
        # (35, 31, []),
        (2, 2, ["0 0 1 0", "1 2 2 2", "1 1 2 1"])
        ]
    for args in test_args:
        print avoid_roads(*args)
