class Lexer:
    def __init__(self, pattern_models):
        self.pattern_models = pattern_models

    def tokens(self, text):
        index = 0
        while text:
            for pattern_model in self.pattern_models:
                pattern = pattern_model.make(index, text)
                if pattern:
                    index += pattern.size
                    text = text[pattern.size:]
                    if not pattern.model.ignore:
                        yield pattern
                    break
            else:
                raise Exception(f"No pattern found !")
