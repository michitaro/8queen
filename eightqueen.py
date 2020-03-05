import argparse
from typing import List

State = List[int]

roots: List[State] = []


def main():
    global N, args
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', '-n', type=int, default=8)
    parser.add_argument('--print', '-p', action='store_true')
    args = parser.parse_args()
    N = args.n
    find_roots([])
    print(f'n={len(roots)}')


def print_state(s: State):
    for col_j in s:
        for i in range(N):
            print('Q' if col_j == i else '.', end='')
        print()
    print('-' * (2*N))


def find_roots(s: State):
    if len(s) == N:
        roots.append(s)
        if args.print:
            print_state(s)
        return
    for j in possible_j(s):
        find_roots(s + [j])


def possible_j(s: State):
    i0 = len(s)
    ps = set(range(N))
    for i, col_j in enumerate(s):
        d = i - i0
        ps.discard(col_j)
        ps.discard(col_j + d)
        ps.discard(col_j - d)
    return ps


main()
