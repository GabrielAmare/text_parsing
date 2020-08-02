from .Unit import Unit


class Astb:
    def __init__(self, model):
        self.model = model
        self.items = []

    def get_by_end(self, end):
        for item in self.items:
            if item.end == end:
                yield item

    def add(self, item):
        self.items.append(item)
        for rule in self.model.rules:
            for new in rule.build(self, item):
                self.add(new)

    def finalize(self):
        start = float('inf')
        end = 0
        for item in self.items:
            if isinstance(item, Unit):
                start = min(start, item.start)
                end = max(end, item.end)

        for item in self.items:
            if item.start == start and item.end == end:
                yield item
