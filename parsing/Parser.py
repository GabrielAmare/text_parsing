from .Astb import Astb
from .Unit import Unit


class Parser:
    def __init__(self, rules):
        self.rules = rules

    def build(self, tokens, debug=False):
        astb = Astb(self)
        for index, token in enumerate(tokens):
            if debug:
                if index:
                    print(' -> ', end='')
                print(token, end='')
            astb.add(Unit(index, token))
        if debug:
            print()
        return astb
