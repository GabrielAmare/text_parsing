from graphviz import Digraph

from text_parsing.parsing import Lemma
from text_parsing.context import Context
from text_parsing.python.lexer import lexer
from text_parsing.python.parser import parser

import os

os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz-2.38\\bin'

if __name__ == '__main__':
    ctx = Context()

    text = ""
    atext = True
    while atext:
        atext = input(">>> ")
        text += ('\n' if text and atext else '') + atext

    tokens = lexer.tokens(text)
    astb = parser.build(tokens, debug=True)

    cn = 0
    for final in astb.finalize():
        if isinstance(final, Lemma):
            obj = ctx.fabric(final)
            cn += 1

            dot = Digraph(engine='dot')
            obj.asNode(dot)
            dot.render(f'graphs\\tmp_{cn}', view=True)
