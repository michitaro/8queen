from typing import List

State = List[int]

roots: List[State] = []


def main():
    s = []
    find_roots(s)
    print(f'n={len(roots)}')


def print_state(s: State):
    assert len(s) == 8
    for col_j in s:
        for i in range(8):
            print('Q' if col_j == i else '.', end='')
        print()
    print('-' * 16)


def find_roots(s: State):
    if len(s) == 8:
        roots.append(s)
        print_state(s)
        return
    for j in possible_j(s):
        find_roots(s + [j])


def possible_j(s: State):
    i0 = len(s)
    ps = set(range(8))
    for i, col_j in enumerate(s):
        d = i - i0
        ps.discard(col_j)
        ps.discard(col_j + d)
        ps.discard(col_j - d)
    return ps


main()
