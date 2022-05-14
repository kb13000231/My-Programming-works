def is_valid_state(state, n):
    # check if it is a valid solution
    return len(state) == n


def get_candidates(state, n):
    if not state:
        return range(n)

    # find the next position in the state to populate
    position = len(state)
    candidates = set(range(n))
    # prune the candidates that place the queens into attacks
    for row, col in enumerate(state):
        # discardthe col index if it's occcupied
        candidates.discard(col)
        dist = position - row

        # discard diagonals
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates


def search(state, solutions, n):
    if is_valid_state(state, n):
        state_str = state_to_string(state, n)
        solutions.append(state_str)
        return

    for candidate in get_candidates(state, n):
        # recurse
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


def state_to_string(state, n):
    ret = []
    for i in state:
        addstring = '.'*i + 'Q' + '.'*(n - i - 1)
        ret.append(addstring)
    return ret


def solve():
    n = int(input('Enter the no of queens: '))
    solutions = []
    state = []
    search(state, solutions, n)
    return solutions


print(solve())
