import logging
import sys
import pprint as pp


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.handlers.clear()  # clear the default handler to avoid duplicate logs
logger.addHandler(handler)


def bsuccessors(state):
    """
    successor {state: action} {(here,there,t): (1,1,'->')}
    action (go_from_here, go_to_there, 'direction')

    :param state: tuple (here, there, t)
    :return:
    """
    here, there, t = state
    logger.debug("here: {}".format(here))
    logger.debug("there: {}".format(there))

    successors = {}
    if 'light' in here:
        here = [x for x in here if x is not 'light']
        direction = '->'
        for person in here:
            # implement single person crossing first
            action = (person, person, direction)
            logging.debug('person {0}, action {1}'.format(person, action))
            # new state
            t_new = t + person
            here_new = frozenset([p for p in here if p is not person])
            there_new = there.union(['light', person])
            logging.debug('t_new {}, here_new {}, there_new {}'.format(t_new, here_new, there_new))
            state_new = (here_new, there_new, t_new)
            logging.debug('state_new={}'.format(state_new))
            successors[state_new] = action
    else:  # light in there side
        there = [x for x in there if x is not 'light']
        direction = '<-'
        for person in there:
            # implement single person crossing first
            action = (person, person, direction)
            logging.debug('person {0}, action {1}'.format(person, action))
        pass
    return successors


if __name__ == '__main__':
    # test from here to there
    here0 = frozenset([1, 2, 3, 4, 'light'])
    there0 = frozenset([])
    t0 = 3
    state = (here0, there0, t0)
    pp.pprint(bsuccessors(state))

    # test from there to here
    there0 = frozenset([1, 2, 'light'])
    here0 = frozenset([])
    t0 = 3
    state = (here0, there0, t0)
    print(bsuccessors(state))
