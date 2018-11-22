"""
turing.py: a class to simulate the turing machine

"""


import argparse


MAX_TRANSITION = 20
START_STATE_NAME='q0'
END_STATE_NAME='qr'


class State:
    def __init__(self, name):
        self.name = name
        self.transitions = []

    def add_transition(self, symbol1, state2, symbol2, move):
        self.transitions.append([symbol1, state2, symbol2, move])

    def show(self):
        print('state name: ', self.name)
        for t in self.transitions:
            print('\t', t[0], '->', t[1].name, ',', t[2], ',', t[3])


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

        for i in range(1, len(l)-3):
            str_list = l[i].split(',')
            st1 = self.get_state(str_list[0])

            str_list2 = str_list[1].split('-')
            sy1 = str_list2[0]
            st2 = self.get_state(str_list2[1][1:])
            st1.add_transition(sy1, st2, str_list[2], str_list[3])

        return l[-2]

    def show(self):
        print(self.init_string)
        print(self.str)
        if self.verbose is True:
            print("State details:")
            for id in self.states:
                self.states[id].show()

    def run(self, str=None):
        if str is None:
            str = self.str

        pass

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
    t.show()
    t.run()
