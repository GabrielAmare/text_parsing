from .NArg import NArg


class NKwarg(NArg):
    def __init__(self, content):
        uid, names = content.split(':', 1)
        assert ':' not in uid and '|' not in uid
        assert not any(':' in name for name in names)
        self.uid = uid
        super().__init__(names)

    def build(self, item, args, kwargs):
        kwargs[self.uid] = item
