class Unit:
    def __init__(self, start, token):
        self.start = start
        self.end = self.start + 1
        self.token = token

    @property
    def names(self):
        return self.token.model.name.split('|')

    @property
    def name(self):
        return self.names[0]

    def __repr__(self):
        return f"`{self.token.content}`"
