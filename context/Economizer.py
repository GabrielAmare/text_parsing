class Economizer:
    instances = {}

    def __init_subclass__(cls, **kwargs):
        cls.instances = {}

    def __new__(cls, *args, **kwargs):
        key = cls._key(*args, **kwargs)
        if key in cls.instances:
            return cls.instances[key]
        else:
            self = super().__new__(cls)
            return self

    @classmethod
    def _key(cls, *args, **kwargs):
        raise NotImplementedError

    def _init(self, *args, **kwargs):
        raise NotImplementedError

    def __init__(self, *args, **kwargs):
        if not hasattr(self, '_lock'):
            self._init(*args, **kwargs)
            self.instances[self._key(*args, **kwargs)] = self
            self._lock = True
