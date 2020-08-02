from ..Economizer import Economizer


class Bloc(Economizer):
    sym = '<?>'
    node_config = dict(shape='box', style='filled', fillcolor='lightgray')
    syms = {}

    def __init_subclass__(cls, **kwargs):
        cls.sym = kwargs.get('sym', '?')
        assert cls.sym not in Bloc.syms
        Bloc.syms[cls.sym] = cls

    @classmethod
    def _key(cls, ctx, inside):
        return ctx, inside

    def _init(self, ctx, inside):
        self.ctx = ctx
        self.inside = inside

    def __repr__(self):
        return self.sym

    def __iter__(self):
        yield self.inside

    @classmethod
    def build(cls, ctx, item):
        return cls(
            ctx=ctx,
            inside=ctx.fabric(item.get('inside')),
        )

    def parts(self):
        yield 'inside', self.inside
