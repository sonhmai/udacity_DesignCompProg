import logging
import sys
import pprint as pp

# -----------------
# User Instructions
#
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is
# '->' for here to there or '<-' for there to here. When only one
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.


def bsuccessors(state):
    """
    successor {state: action} {(here,there,t): (1,1,'->')}
    action (go_from_here, go_to_there, 'direction')

    :param state: tuple (here, there, t)
    :return:
    """
    here, there, t = state

    if 'light' in here:
        # list [(key,val),..]
        content = [(
            (here - frozenset([a, b, 'light']),
             there | frozenset([a, b, 'light']),
             t + max(a, b)
             ), (a, b, '->'))
            for a in here if a is not 'light'
            for b in here if b is not 'light']
        # pp.pprint(content)
        return dict(content)
    else:  # light in there side
        content = [(
            (here | frozenset([a, b, 'light']),
             there - frozenset([a, b, 'light']),
             t + max(a, b)
             ), (a, b, '<-'))
            for a in there if a is not 'light'
            for b in there if b is not 'light']
        return dict(content)


if __name__ == '__main__':
    # test from here to there
    here0 = frozenset([1, 2, 3, 4, 'light'])
    there0 = frozenset([])
    t0 = 0
    state = (here0, there0, t0)
    print("\nInitial state:", state)
    pp.pprint(bsuccessors(state))

    here0 = frozenset([1, 2, 4, 'light'])
    there0 = frozenset([3, 5])
    t0 = 0
    state = (here0, there0, t0)
    print("\nInitial state:", state)
    pp.pprint(bsuccessors(state))

    here0 = frozenset([1, 2])
    there0 = frozenset([3, 4, 'light'])
    t0 = 0
    state = (here0, there0, t0)
    print("\nInitial state:", state)
    pp.pprint(bsuccessors(state))

