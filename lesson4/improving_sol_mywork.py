# -----------------
# User Instructions
#
# Modify the bridge_problem(here) function so that it
# tests for goal later: after pulling a state off the
# frontier, not when we are about to put it on the
# frontier.
import pprint as pp


def bsuccessors(state):
    """Return a dict of {state:action} pairs.  A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the light, and t is a number indicating the elapsed time."""
    here, there, t = state
    if 'light' in here:
        return dict(((here - frozenset([a, b, 'light']),
                      there | frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here | frozenset([a, b, 'light']),
                      there - frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light')


def elapsed_time(path):
    return path[-1][2]


def bridge_problem(here):
    """Modify this to test for goal later: after pulling a state off frontier,
    not when we are about to put it on the frontier."""
    ## modify code below
    here = frozenset(here) | frozenset(['light'])
    explored = set()  # set of states we have visited
    # State will be a (people-here, people-there, time-elapsed)
    frontier = [[(here, frozenset(), 0)]]  # ordered list of paths we have blazed
    if not here:
        return frontier[0]
    while frontier:
        path = frontier.pop(0)  # path [state, action, state]. state (here,there,t)
        state = path[-1]
        here = state[0]
        if not here:
            pp.pprint(path)
            return path
        # print("path:", path)
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                # print("state: {}, action: {}".format(state, action))
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                frontier.append(path2)
                frontier.sort(key=elapsed_time)
                # pp.pprint("frontier: {}".format(frontier))

    return []


def test():
    assert bridge_problem(frozenset((1, 2), ))[-1][-1] == 2  # the [-1][-1] grabs the total elapsed time
    assert bridge_problem(frozenset((1, 2, 5, 10), ))[-1][-1] == 17
    return 'tests pass'


# print(test())
# print(bridge_problem(frozenset((1, 2), ))[-1][-1])
print(elapsed_time(bridge_problem(frozenset((1, 2, 3, 4, 6, 7, 8, 10), ))))
print(bridge_problem(frozenset((1, 2, 3, 4, 6, 7, 8, 10), ))[0::2][2])
