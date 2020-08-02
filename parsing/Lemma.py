from .Unit import Unit


class Lemma:
    def __init__(self, model, *items, **kwitems):
        assert all(isinstance(item, (Unit, Lemma)) for item in items)
        assert all(isinstance(item, (Unit, Lemma)) for item in kwitems.values())
        # assert all(items[i].end == items[i + 1].start for i in range(len(items) - 1))
        self.model = model
        self.items = items
        self.kwitems = kwitems

        self.end = max(item.end for item in (*self.items, *self.kwitems.values()))
        self.start = min(item.start for item in (*self.items, *self.kwitems.values()))

    @property
    def names(self):
        return self.model.names

    @property
    def name(self):
        return self.names[0]

    def get(self, key):
        if isinstance(key, int):
            return self.items[key]
        elif isinstance(key, str):
            return self.kwitems[key]
        else:
            raise Exception

    def get_content(self, key):
        return self.get(key).token.content

    def __repr__(self):
        args = [f"{item}" for item in self.items]
        kwargs = [f"{key}={val}" for key, val in self.kwitems.items()]
        return f"{self.name}[{', '.join(args + kwargs)}]"
