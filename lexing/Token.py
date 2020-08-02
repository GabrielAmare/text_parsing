class Token:
    def __init__(self, model, content, start, count=1):
        self.model = model
        self.content = content
        self.start = start
        self.size = len(self.content)
        self.end = self.start + self.size
        self.count = count

    def __repr__(self):
        return f"{self.model.name}[{self.count}][{self.start}:{self.end}][{repr(self.content)}]"
