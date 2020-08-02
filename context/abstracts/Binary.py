from ..Economizer import Economizer


class Binary(Economizer):
    com = False
    sym = '<?>'
    node_config = dict(shape='record', style='filled', fillcolor='#fad248')
    syms = {}

    def __init_subclass__(cls, **kwargs):
        cls.com = kwargs.get('com', False)
        cls.sym = kwargs.get('sym', '?')
        assert cls.sym not in Binary.syms
        Binary.syms[cls.sym] = cls

    @classmethod
    def _key(cls, ctx, left, right):
        if cls.com:
            return ctx, (left, right)
        else:
            return ctx, tuple(sorted(map(id, (left, right))))

    def _init(self, ctx, left, right):
        self.ctx = ctx
        self.left = left
        self.right = right

    def __repr__(self):
        return f" <left> | {self.sym} | <right> "

    def __iter__(self):
        yield self.left
        yield self.right

    def parts(self):
        yield 'left', self.left
        yield 'right', self.right

    @classmethod
    def build(cls, ctx, item):
        return cls(
            ctx=ctx,
            left=ctx.fabric(item.get('left')),
            right=ctx.fabric(item.get('right'))
        )

    def asNode(self, dot):
        name = str(hex(id(self)))
        dot.node(
            name=name,
            label=f" <left> | <_>{self.sym} | <right> ",
            shape='record',
            style='filled',
            fillcolor='#fad248'
        )
        left = self.left.asNode(dot)
        right = self.right.asNode(dot)
        dot.edge(f"{name}:left", f"{left}:_")
        dot.edge(f"{name}:right", f"{right}:_")
        return name
