from .Rule import Rule
from .Lemma import Lemma


class EnumRule(Rule):
    def __init__(self, names, element, separator, can_end_with_sep=False):
        super().__init__(names, element, separator)
        self.can_end_with_sep = can_end_with_sep

    def test(self, index, item, parity):
        mode = abs(index % 2 - parity)
        if index == 0 and self.can_end_with_sep:
            if self.tests[0](item):
                return True, 0
            elif self.tests[1](item):
                return True, 1
            else:
                return False, 0
        else:
            return self.tests[mode](item), parity

    def build(self, parser, item, *items, parity=0):
        r, parity = self.test(len(items), item, parity)
        if r:
            c = 0
            for prev in parser.get_by_end(item.start):
                c += 1
                for result in self.build(parser, prev, item, *items, parity=parity):
                    yield result
            if c == 0 and len(items) >= [2, 1][self.can_end_with_sep]:
                if len(items) % 2:
                    yield Lemma(self, *items)
                else:
                    yield Lemma(self, item, *items)
        elif len(items) >= 2:
            if len(items) % 2:
                yield Lemma(self, *items)
            # else:
            #     yield Lemma(self, item, *items)
