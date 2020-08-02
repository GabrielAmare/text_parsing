from .abstracts import *


class Eq(Binary, com=True, sym='=='):
    pass


class Add(Binary, com=True, sym='+'):
    pass


class Mul(Binary, com=True, sym='*'):
    pass


class Sub(Binary, com=False, sym='-'):
    pass


class Truediv(Binary, com=False, sym='/'):
    pass


class Floordiv(Binary, com=False, sym='//'):
    pass


class Mod(Binary, com=False, sym='%'):
    pass


class Pow(Binary, com=False, sym='**'):
    pass


class Ne(Binary, com=False, sym='!='):
    pass


class Le(Binary, com=False, sym='<='):
    pass


class Lt(Binary, com=False, sym='<'):
    pass


class Ge(Binary, com=False, sym='>='):
    pass


class Gt(Binary, com=False, sym='>'):
    pass


class Is(Binary, com=True, sym='is'):
    pass


class IsNot(Binary, com=False, sym='is not'):
    pass


class In(Binary, com=False, sym='in'):
    pass


class NotIn(Binary, com=False, sym='not in'):
    pass


class Or(Binary, com=True, sym='or'):
    pass


class And(Binary, com=True, sym='and'):
    pass


class GetItem(Binary, com=False, sym='[...]'):
    pass


class GetAttr(Binary, com=False, sym='.'):
    pass


class SetId(Binary, com=False, sym='='):
    pass


class Call(Binary, com=False, sym='(...)'):
    def asNode(self, dot):
        name = str(hex(id(self)))
        dot.node(
            name=name,
            label="{ <_>__call__ | { <left> | ( | <right> | ) } }",
            shape='record',
            style='filled',
            fillcolor='#fad248'
        )
        left = self.left.asNode(dot)
        dot.edge(f"{name}:left", f"{left}:_")
        right = self.right.asNode(dot)
        dot.edge(f"{name}:right", f"{right}:_")
        return name


class Not(LUnary, sym='not'):
    pass


class Pos(LUnary, sym='+'):
    pass


class Neg(LUnary, sym='-'):
    pass


class Args(Enum, com=False, sym=','):
    pass


class Lines(Enum, com=False, sym='\n'):
    pass


class Par(Bloc, sym='(...)'):
    def asNode(self, dot):
        name = str(hex(id(self)))
        dot.node(
            name=name,
            label=" ( | <_> | ) ",
            shape='record',
            style='filled',
            fillcolor='#fad248'
        )
        inside = self.inside.asNode(dot)
        dot.edge(f"{name}:_", f"{inside}:_")
        return name


from .Economizer import Economizer


class SetAttr(Economizer):
    node_config = dict(shape='box', style='filled', fillcolor='#fad248')

    @classmethod
    def _key(cls, ctx, obj, key, val):
        return ctx, obj, key, val

    def _init(self, ctx, obj, key, val):
        self.ctx = ctx
        self.obj = obj
        self.key = key
        self.val = val

    def __repr__(self):
        return "__setattr__"

    def __iter__(self):
        yield self.obj
        yield self.key
        yield self.val

    def asNode(self, dot):
        name = str(hex(id(self)))
        dot.node(
            name=name,
            label="{ <_>__setattr__ | { <obj> | <key> | <val> } }",
            shape='record',
            style='filled',
            fillcolor='#fad248'
        )
        obj = self.obj.asNode(dot)
        dot.edge(f"{name}:obj", f"{obj}:_")
        key = self.key.asNode(dot)
        dot.edge(f"{name}:key", f"{key}:_")
        val = self.val.asNode(dot)
        dot.edge(f"{name}:val", f"{val}:_")
        return name


class Tern(Economizer):
    node_config = dict(shape='box', style='filled', fillcolor='#fad248')

    @classmethod
    def _key(cls, ctx, true, cond, false):
        return ctx, true, cond, false

    def _init(self, ctx, true, cond, false):
        self.ctx = ctx
        self.true = true
        self.cond = cond
        self.false = false

    def __repr__(self):
        return "__setattr__"

    def __iter__(self):
        yield self.true
        yield self.cond
        yield self.false

    def asNode(self, dot):
        name = str(hex(id(self)))
        dot.node(
            name=name,
            label="{ <_> \{\} if \{\} else \{\} | { <true> | <cond> | <false> } }",
            shape='record',
            style='filled',
            fillcolor='#fad248'
        )
        true = self.true.asNode(dot)
        dot.edge(f"{name}:true", f"{true}:_")
        cond = self.cond.asNode(dot)
        dot.edge(f"{name}:cond", f"{cond}:_")
        false = self.false.asNode(dot)
        dot.edge(f"{name}:false", f"{false}:_")
        return name


class For(Economizer):
    node_config = dict(shape='box', style='filled', fillcolor='#a448fa')

    @classmethod
    def _key(cls, ctx, condition, iterator):
        return ctx, condition, iterator

    def _init(self, ctx, condition, iterator):
        self.ctx = ctx
        self.condition = condition
        self.iterator = iterator

    def __repr__(self):
        return "for {} in {}:"

    def __iter__(self):
        yield self.condition
        yield self.iterator


class Conditionnal(Economizer):
    node_config = dict(shape='box', style='filled', fillcolor='#a448fa')

    @classmethod
    def _key(cls, ctx, condition):
        return ctx, condition

    def _init(self, ctx, condition):
        self.ctx = ctx
        self.condition = condition

    def __repr__(self):
        return "while {}:"

    def __iter__(self):
        yield self.condition


class While(Conditionnal):
    def __repr__(self):
        return "while {}:"


class If(Conditionnal):
    def __repr__(self):
        return "if {}:"


class Elif(Conditionnal):
    def __repr__(self):
        return "elif {}:"


class Else(Economizer):
    node_config = dict(shape='box', style='filled', fillcolor='#a448fa')

    @classmethod
    def _key(cls, ctx):
        return ctx

    def _init(self, ctx):
        self.ctx = ctx

    def __repr__(self):
        return "else:"

    def __iter__(self):
        return [].__iter__()
