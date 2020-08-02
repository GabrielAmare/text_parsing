from ..Economizer import Economizer


class LUnary(Economizer):
    sym = '<?>'
    node_config = dict(shape='box', style='filled', fillcolor='#fad248')
    syms = {}

    def __init_subclass__(cls, **kwargs):
        cls.sym = kwargs.get('sym', '?')
        assert cls.sym not in LUnary.syms
        LUnary.syms[cls.sym] = cls

    @classmethod
    def _key(cls, ctx, right):
        return ctx, right

    def _init(self, ctx, right):
        self.ctx = ctx
        self.right = right

    def __repr__(self):
        return self.sym

    def __iter__(self):
        yield self.right

    @classmethod
    def build(cls, ctx, item):
        return cls(
            ctx=ctx,
            right=ctx.fabric(item.get('right'))
        )

    def parts(self):
        yield 'right', self.right

    def asNode(self, dot):
        name = str(hex(id(self)))
        dot.node(
            name=name,
            label=f" <_>{self.sym} | <right> ",
            shape='record',
            style='filled',
            fillcolor='#fad248'
        )
        right = self.right.asNode(dot)
        dot.edge(f"{name}:right", f"{right}:_")
        return name
