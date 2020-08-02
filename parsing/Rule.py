from .NArg import NArg
from .NKwarg import NKwarg
from .Lemma import Lemma


class Rule:
    def __init__(self, names, *tests, g_test=None):
        self.names = names.split('|')
        self.tests = tuple(map(self.parse_test, tests))
        self.size = len(tests)
        self.g_test = g_test

    def parse_test(self, test):
        if isinstance(test, str):
            return self.parse_names(test)
            # return lambda item: any(name in test.split('|') for name in item.names)
        else:
            return test

    def get_test(self, index):
        return self.tests[-1 - index]

    def finalize(self, *items):
        if self.g_test is None or self.g_test(*items):
            args = []
            kwargs = {}

            for item, test in zip(items, self.tests):
                if isinstance(test, NArg):
                    test.build(item, args, kwargs)
            # print(args, kwargs, file=sys.stderr)
            return Lemma(self, *args, **kwargs)
        else:
            return None

    def parse_names(self, names):
        if ':' in names:
            return NKwarg(names)
        else:
            return NArg(names)

    def build(self, parser, item, *items):
        if self.get_test(len(items))(item):
            # if self.tests[-1 - len(items)](item):
            if 0 <= len(items) < self.size - 1:
                for prev in parser.get_by_end(item.start):
                    for res in self.build(parser, prev, item, *items):
                        yield res
            elif len(items) == self.size - 1:
                res = self.finalize(item, *items)
                if res:
                    yield res
                # if self.g_test is None or self.g_test(item, *items):
                #     yield Lemma(self, item, *items)
            else:
                raise Exception
