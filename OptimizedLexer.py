class Lexer:
    """
        This class provides an optimized way to tokenize a text with a given set of rules.

        -> the format of the patterns is very simple but efficient
        -> be careful, the tokens can overlap each others

        format of a pattern is as following :

        the Lexer is defined by a dict map of pattern names to their definition

        > pattern : is a list of sections

        > section : is a tuple of 2 items : cardinality & charset

        > cardinality : allows only 4 variants :
            '!' means 1 char of the charset need to be matched
            '?' means the same thing but is optional
            '+' means 1 char or more
            '*' means 0 char or more

        > charset : is a string containing all the characters that the section can accept

        use case :
        >>> lexer = Lexer(
        >>>     word=[('+', Lexer.letters), ('?', "'")], # equivalent to the regex "[a-zA-ZéàèâêûîôäëïüöÿçùÄËÜÏÖÂÊÛÎÔ]+[']?"
        >>>     number=[('+', Lexer.digits)],
        >>>     space=[('+', ' ')],
        >>>     newline=[('!', '\\n')],
        >>>     ponct=[('+', '.!?')]
        >>> )
        >>> for token_type, token_content, start_index in lexer.tokenize("hi I'm a sentence !"):
        >>>     print(token_type, token_content, start_index)
    """
    alp = 'abcdefghijklmnopqrstuvwxyz'
    ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    oth = 'éàèâêûîôäëïüöÿçù'
    OTH = 'ÄËÜÏÖÂÊÛÎÔ'
    letters = alp + ALP + oth + OTH
    digits = '0123456789'

    @staticmethod
    def step(item):
        card, chars = item
        assert card in ('!', '?', '+', '*')
        assert isinstance(chars, str)
        return card in ('*', '?'), card in ('!', '?'), chars

    def __init__(self, **patterns):
        sizes = dict((key, len(steps)) for key, steps in patterns.items())
        self.base = tuple((k, tuple(map(Lexer.step, patterns[k])), sizes[k], 0, False, '') for k in patterns)

    def tokenize(self, chars):
        instance = self.Instance(self.base)
        for char in chars:
            for token in instance.feed(char):
                yield token
        for token in instance.end():
            yield token

    class Instance:
        def __init__(self, b):
            self.c = 0
            self.n = ()
            self.b = b

        def feed(self, c):
            t = []
            a = False
            for k, p, s, i, l, r in self.n + self.b:
                if l and p[i][1]:
                    l, i = False, i + 1
                while i < s:
                    if c in p[i][2]:
                        t.append((k, p, s, i, True, r + c))
                    elif l or p[i][0]:
                        l, i = False, i + 1
                        continue
                    break
                if i == s and not a:
                    yield k, r, self.c - len(r)
                    a = True
            self.n = tuple(t)
            self.c += 1

        def end(self):
            for k, p, s, i, l, r in self.n:
                while i < s:
                    if l or p[i][0]:
                        l, i = False, i + 1
                        continue
                    break
                if i == s:
                    yield k, r, self.c - len(r)
                    break


if __name__ == '__main__':

    lexer = Lexer(
        word=[('+', Lexer.letters), ('?', "'")],  # equivalent to the regex "[a-zA-ZéàèâêûîôäëïüöÿçùÄËÜÏÖÂÊÛÎÔ]+[']?"
        number=[('+', Lexer.digits)],
        space=[('+', ' ')],
        newline=[('!', '\n')],
        ponct=[('+', '.!?')]
    )
    
    text = "hi I'm a sentence !\nFollowed by another on another line..."

    for token_type, token_content, start_index in lexer.tokenize(text):
        print(f"[{start_index}]{token_type.upper()} `{repr(token_content)[1:-1]}`")
