"""
turing.py: a class to simulate the turing machine

"""


import argparse


MAX_TRANSITION = 20


class Turing:

    def __init__(self, init_string, max_transitions):
        self.max_transitions = max_transitions
        self.str = self.create_machine(init_string)

    def parse(self, init_string):
        pass

    def run(self, str=None):
        if str is None:
            str = self.str

        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-mt", "--max_transitions",
                        help="define the max_transitions",
                        type=int)
    parser.add_argument("machine", help="define machine string")

    args = parser.parse_args()
    max_transitions = args.max_transitions if args.max_transitions else \
        MAX_TRANSITION
