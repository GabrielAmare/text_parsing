from ..Economizer import Economizer


class Enum(Economizer):
    com = False
    sym = '<?>'
    node_config = dict(shape='box', style='filled', fillcolor='#fad248')
    syms = {}

    def __init_subclass__(cls, **kwargs):
        cls.com = kwargs.get('com', False)
        cls.sym = kwargs.get('sym', '?')
        assert cls.sym not in Enum.syms
        Enum.syms[cls.sym] = cls

    @classmethod
    def _key(cls, ctx, items):
        if cls.com:
            return ctx, items
        else:
            return ctx, tuple(sorted(map(id, items)))

    def _init(self, ctx, items):
        self.ctx = ctx
        self.items = items

    def __repr__(self):
        return self.sym.replace('\n', '\\\\n')

    def __iter__(self):
        for item in self.items:
            yield item

    @classmethod
    def build(cls, ctx, item):
        return cls(
            ctx=ctx,
            items=tuple(map(ctx.fabric, (e for i, e in enumerate(item.items) if not i % 2)))
        )

    def parts(self):
        for index, item in enumerate(self):
            yield index, item

    def asNode(self, dot):
        name = str(hex(id(self)))
        dot.node(
            name=name,
            label="{ " + f"<_>{self.sym}" + " | " + "{ " + " | ".join(
                f"<{index}>" for index in range(len(self.items))) + " }" + " }",
            shape='record',
            style='filled',
            fillcolor='#fad248'
        )
        for index, item in enumerate(self.items):
            sub = item.asNode(dot)
            dot.edge(f"{name}:{index}", f"{sub}:_")
        return name
