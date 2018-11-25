"""
turing.py: a class to simulate the turing machine

"""


import argparse


MAX_TRANSITION = 20
START_STATE_NAME = 'q0'
ACCEPT_STATE_NAME = 'qa'
REJECT_STATE_NAME = 'qr'

EMPTY_CHR = '_'

START = 1
REJECT = 2
LOOP = 3
UNKNOWN = 5
ACCEPT = 10


class Transition:
    def __init__(self, state1, symbol1, state2, symbol2, move):
        self.symbol1 = symbol1
        self.symbol2 = symbol2
        self.state1 = state1
        self.state2 = state2
        self.move = move

    def show(self):
        print('\t', self.state1.name, ',', self.symbol1, '->',
              self.state2.name, ',', self.symbol2, ',', self.move)


class State:
    def __init__(self, name):
        self.name = name
        self.transitions = []

    def add_transition(self, symbol1, state2, symbol2, move):
        self.transitions.append(Transition(self, symbol1,
                                           state2, symbol2, move))

    def show(self):
        print('state name: ', self.name)
        for t in self.transitions:
            t.show()

    @property
    def st_type(self):
        if self.name == START_STATE_NAME:
            return START
        elif self.name == REJECT_STATE_NAME:
            return REJECT
        elif self.name == ACCEPT_STATE_NAME:
            return ACCEPT

        return UNKNOWN


class Turing:
    def __init__(self, init_string, max_transitions, verbose):
        self.max_transitions = max_transitions
        self.states = {}
        self.init_string = init_string
        self.verbose = verbose
        self.str = self.parse(init_string)

    def get_state(self, name):
        if name not in self.states:
            self.states[name] = State(name)
        return self.states[name]

    def parse(self, init_string):
        l = init_string.split('#')
        if len(l) <= 2:
            return None
        self.machine_str = '#'.join(l[:-2])
        for i in range(1, len(l)-3):
            str_list = l[i].split(',')
            st1 = self.get_state(str_list[0])

            str_list2 = str_list[1].split('-')
            sy1 = str_list2[0]
            st2 = self.get_state(str_list2[1][1:])
            st1.add_transition(sy1, st2, str_list[2], str_list[3])

        return l[-2]

    def show(self, str=None):
        print(self.machine_str)
        print(str if str is not None else self.str)
        print(sum([len(self.states[id].transitions) for id in self.states]))
        print(len(self.states))

        if self.verbose is True:
            print("State details:")
            for id in self.states:
                self.states[id].show()

    def show_iteration(self, it, st=None):
        print(st, it[0].name, it[1], it[2], it[3])

    def run(self, str=None):
        if str is None:
            str = self.str

        self.show(str)

        it = [self.states[START_STATE_NAME], str, 0, UNKNOWN]
        it_repo = [[it]]
        it_counter = 0
        it_status = UNKNOWN

        while (it_status is not ACCEPT) and it_counter <= self.max_transitions:
            if self.verbose is True:
                print('------------------------')
                print("it_counter:", it_counter)
            it_status = UNKNOWN
            it_repo.append([])
            for it in it_repo[it_counter]:
                if self.verbose is True:
                    print('------------------------')
                    self.show_iteration(it, 'Start State')

                if it[3] == UNKNOWN:
                    state = it[0]
                    s = it[1]
                    i = it[2]
                    if i >= len(s):
                        c = EMPTY_CHR
                    else:
                        c = s[i]

                    for tr in state.transitions:
                        if tr.symbol1 == '_' or tr.symbol1 == c:
                            # print('++++++++++++++++++')
                            # tr.show()
                            str_new = s
                            if tr.symbol2 != '_':
                                if i < 0:
                                    # recheck the case
                                    pass
                                elif i >= len(str_new):
                                    # print("i >= len(str_new)", i, len(str_new))
                                    str_new += '_' * (i-len(str_new)) \
                                        + tr.symbol2
                                else:
                                    # print("else", i, len(str_new))
                                    str_new = str_new[:i] + tr.symbol2 + \
                                        str_new[i+1:]

                            # print("str_new", str_new)

                            if tr.move == 'R':
                                i_new = i + 1
                            elif tr.move == 'L':
                                i_new = 1 - 1
                            # print(tr.move, i, i_new)

                            it_repo[it_counter+1].append([tr.state2, str_new,
                                                          i_new,
                                                          tr.state2.st_type])
                            if self.verbose is True:
                                self.show_iteration(it_repo[it_counter+1][-1],
                                                    '\t')

            it_counter += 1
            it_status = max([it[-1] for it in it_repo[it_counter]])

        if it_status == ACCEPT:
            print('M stops and accepts w')
        else:
            print('M stops and reject w')


# example
# init_string = #q0,a->qa,a,R#q0,a->q1,a,R#q0,b->q1,b,R#q0,_->q1,_,R#q1,b->q1,b,R#q1,_->q1,_,R#q1,a->qr,a,R#q1,b->qr,b,R##ab#


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-mt", "--max_transitions",
                        help="define the max_transitions",
                        type=int)
    parser.add_argument("-v", "--verbose", help="Show more details",
                        action='store_true')
    parser.add_argument("machine", help="define machine string")

    args = parser.parse_args()
    max_transitions = args.max_transitions if args.max_transitions else \
        MAX_TRANSITION

    t = Turing(args.machine, max_transitions, args.verbose)
    t.run()
