from .Economizer import Economizer


class Cte(Economizer):
    node_config = dict(shape='box', style='filled', fillcolor='#4894fa')

    @classmethod
    def _key(cls, ctx, value):
        return ctx, value

    def _init(self, ctx, value):
        self.ctx = ctx
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __iter__(self):
        return [].__iter__()

    def parts(self):
        return []

    def asNode(self, dot):
        name = str(hex(id(self)))
        if isinstance(self.value, str):
            value = self.value.replace('\|', '\\\|').replace('|', '\|')
        else:
            value = self.value

        dot.node(
            name=name,
            label=f"<_>{value}",
            shape='record',
            style='filled',
            fillcolor='#4894fa'
        )
        return name