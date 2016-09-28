# https://community.topcoder.com/stat?c=problem_statement&pm=3509&rd=6528&rm=&cr=7452866
#
# Consider an empty chess board (8x8 squares), with a
# chess knight placed on one of the squares.
#
# If the knight moves n times, each time picking one of
# the eight directions uniformly at random (possibly a direction which 
# makes the knight leave the chess board), determine the probability that
# it's still on the board after n jumps. Once the knight leaves the board,
#  it can't enter it again.
#
# Create a class ChessKnight containing the method probability which takes an
# int x, an int y (the start square of the chess knight, where 1,1 is one of
# the corners) and an int n, the number of jumps the knight will make. The method
# should return a double, the probability that the knight is still on the chess
# board after making n random jumps.


from itertools import permutations, product

def isin_board(coords):
    x, y = coords
    return (x > 0 and x <= 8) \
            and (y > 0 and y <= 8)

def get_prob(x_0, y_0, n):
    memo = []
    cell_neighbors = {}

    directions = [(c, d) for a, b in product([1, -1], [2, -2])
                    for c, d in permutations([a, b])
                ]

    for k in range(n):
        memo_probs = [[0 for _ in xrange(8)] for _ in xrange(8)]
        if k > 0:
            prev_probs = memo[-1]
        for x in range(1,9):
            for y in range(1,9):
                if k == 0:
                    nbrs = filter(isin_board,
                                [(x + c, y + d) for c, d in directions])
                    cell_neighbors[(x,y)] = nbrs
                    memo_probs[x-1][y-1] = len(nbrs) / 8.
                else:
                    memo_probs[x-1][y-1] = (1/8.)*sum(prev_probs[c-1][d-1]
                                                for c, d in cell_neighbors[(x, y)])
        memo.append(memo_probs)
    return memo[-1][x_0-1][y_0-1]



if __name__ == '__main__':
    print get_prob(1, 1, 2) # .1875
    print get_prob(4, 4, 1) # 1.0
    print get_prob(2, 3, 10) # 0.0522148497402668
    print get_prob(4, 3, 50) # 8.356427906809618E-7
