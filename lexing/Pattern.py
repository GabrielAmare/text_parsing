import re
from .Token import Token


class Pattern:
    def __init__(self, name, mode, expr, flag=0, ignore=False):
        self.name = name
        self.mode = mode
        self.expr = expr
        self.size = len(self.expr)
        self.flag = flag
        self.ignore = ignore

        if self.mode == 'kw':
            self.mode = 're'
            self.expr = f"(?<![\w\d]){self.expr}(?![\w\d])"

    def make(self, index, text):
        if self.mode == 'str':
            if text.startswith(self.expr):
                return Token(model=self, content=self.expr, start=index)
        elif self.mode == 're':
            match = re.match(f"^{self.expr}", text, flags=self.flag)
            if match:
                return Token(model=self, content=match.group(), start=index)
        elif self.mode == 'repeat':
            count = 0
            while text[count * self.size:].startswith(self.expr):
                count += 1
            if count:
                return Token(model=self, content=count * self.expr, start=index, count=count)
