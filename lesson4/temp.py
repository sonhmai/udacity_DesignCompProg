import itertools


def get_travel_set(f):
    """

    :param f:
    :return:
    """
    print([{a, b} for a in f for b in f])
    print([(a, b) for a in f for b in f])
    print(dict((a, b) for a in f for b in f))
    print()

f = frozenset([1, 3, 4])
get_travel_set(f)