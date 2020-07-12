class SimpleLexer:
    """
        This object take ``text`` and transform it in a list of tokens on the form (content, type)
        When calling $.tokens, it yields a sequence of (str | int) elements (respectively words & numbers) and ignore the spaces
        -> three token types are defined here : 'word', 'number', 'space'
            -> 'word' matches any letter sequence
            -> 'number' matches any integer
            -> 'space' matches any other character

        NB : This lexer have been optimized to read text character by character and do as less operations as possible.
             Doing so, it can tokenize fastly very long texts.
    """

    @staticmethod
    def isLetter(n):
        """Return True if n (which is ord(char) is a letter)"""
        return 65 <= n <= 90 or \
               97 <= n <= 122 or \
               192 <= n <= 207 or \
               209 <= n <= 214 or \
               217 <= n <= 221 or \
               224 <= n <= 228 or \
               230 <= n <= 239 or \
               241 <= n <= 246 or \
               249 <= n <= 253 or \
               n == 255

    @staticmethod
    def isDigit(n):
        """Return True if n (which is ord(char) is a digit)"""
        return 48 <= n <= 57

    def __init__(self, text):
        self.text = text

    @property
    def tokens(self):
        """
            Yield all the tokens extracted from the text
            -> if a word is matched return a str
            -> if a number is matched return an int
            -> else ignore the content..
        """
        LETTER, DIGIT, UNKNOWN = 0, 1, 2
        NO, WORD, NUMBER, SPACE = 0, 1, 2, 3
        type_ = NO
        content = ''

        for index, char in enumerate(self.text):
            n = ord(char)
            chartype = LETTER if self.isLetter(n) else DIGIT if self.isDigit(n) else UNKNOWN

            if type_ == WORD and chartype != LETTER:
                yield content
                content = ''
            elif type_ == NUMBER and chartype != DIGIT:
                yield int(content)
                content = ''
            elif type_ == SPACE and chartype != UNKNOWN:
                content = ''
            if chartype == LETTER and type_ != WORD:
                type_ = WORD
            elif chartype == DIGIT and type_ != NUMBER:
                type_ = NUMBER
            elif chartype == UNKNOWN and type_ != SPACE:
                type_ = SPACE

            content += char

        if content:
            if type_ == WORD:
                yield content
            elif type_ == NUMBER:
                yield int(content)
