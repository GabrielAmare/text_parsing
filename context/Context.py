from ..parsing import Lemma
from .Var import Var
from .Cte import Cte
from .Objects import *


class Context:
    def __init__(self):
        self.items = set()

    def build(self, lemma_cls, item, *keys):
        args = []
        kwargs = {}
        for key in keys:
            obj = self.fabric(item.get(key))
            if isinstance(key, int):
                args.append(obj)
            elif isinstance(key, str):
                kwargs[key] = obj
        return lemma_cls(self, *args, **kwargs)

    def fabric(self, item: Lemma):
        if item.name == 'var':
            built = Var(ctx=self, name=item.get_content('name'))
        elif item.name == 'int':
            built = Cte(ctx=self, value=int(item.get_content('value')))
        elif item.name == 'float':
            built = Cte(ctx=self, value=float(item.get_content('value')))
        elif item.name == 'str':
            built = Cte(ctx=self, value=item.get_content('value'))
        elif item.name == 'bool':
            built = Cte(ctx=self, value=eval(item.get_content('value')))
        elif item.name == ';for':
            assert len(item.items) == 5
            built = For(
                ctx=self,
                condition=self.fabric(item.items[1]),
                iterator=self.fabric(item.items[3]),
            )
        elif item.name == ';while':
            assert len(item.items) == 3
            built = While(
                ctx=self,
                condition=self.fabric(item.items[1])
            )
        elif item.name == ';if':
            assert len(item.items) == 3
            built = If(
                ctx=self,
                condition=self.fabric(item.items[1])
            )
        elif item.name == ';elif':
            assert len(item.items) == 3
            built = Elif(
                ctx=self,
                condition=self.fabric(item.items[1])
            )
        elif item.name == ';else':
            assert len(item.items) == 2
            built = Else(
                ctx=self
            )
        elif item.name == '__setattr__':
            built = self.build(SetAttr, item, 'obj', 'key', 'val')
        elif item.name == 'tern':
            built = self.build(Tern, item, 'true', 'cond', 'false')
        elif 'bloc' in item.names:
            sym = f"{item.get_content(0)}...{item.get_content(1)}"
            # built = self.build(Bloc.syms[sym], item, 'inside')
            built = Bloc.syms[sym].build(self, item)
        elif 'ope' in item.names:
            if len(item.items) == 2:
                sym = f"{item.get_content(0)}...{item.get_content(1)}"
            elif len(item.items) == 1:
                sym = item.get_content(0)
            else:
                raise Exception
            built = Binary.syms[sym].build(self, item)
            # built = self.build(Binary.syms[sym], item, 'left', 'right')
        elif 'l_ope' in item.names:
            sym = item.get_content(0)
            built = self.build(LUnary.syms[sym], item, 'right')
        elif 'enum' in item.names:
            sym = item.get_content(1)
            built = Enum.syms[sym].build(self, item)
            # built = Enum.syms[sym](
            #     ctx=self,
            #     items=tuple(map(self.fabric, (e for i, e in enumerate(item.items) if not i % 2)))
            # )
        else:
            raise Exception(item.name)
        self.items.add(built)
        return built
