from .Economizer import Economizer


class Var(Economizer):
    node_config = dict(shape='box', style='filled', fillcolor='#60fa48')

    @classmethod
    def _key(cls, ctx, name):
        return ctx, name

    def _init(self, ctx, name):
        self.ctx = ctx
        self.name = name

    def __repr__(self):
        return self.name

    def __iter__(self):
        return [].__iter__()

    def parts(self):
        return []

    def asNode(self, dot):
        name = str(hex(id(self)))
        dot.node(
            name=name,
            label=f"<_>{self.name}",
            shape='record',
            style='filled',
            fillcolor='#60fa48'
        )
        return name
