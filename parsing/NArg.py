from .Lemma import Lemma
from .Unit import Unit


class NArg:
    def __init__(self, content):
        items = content.split('|')
        assert not any('|' in item for item in items)
        self.items = items

    def __iter__(self):
        return self.items.__iter__()

    def __contains__(self, names):
        if isinstance(names, list):
            return any(name in self.items for name in names)
        elif isinstance(names, str):
            return any(name in self.items for name in names.split('|'))
        else:
            raise Exception(f"{names.__class__.__name__} should be list|str")

    def __call__(self, item):
        assert isinstance(item, (Lemma, Unit))
        return item.names in self

    def build(self, item, args, kwargs):
        args.append(item)
