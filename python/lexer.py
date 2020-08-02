from ..lexing import Lexer, Pattern

lexer = Lexer([
    Pattern(name='KW_IS', mode='kw', expr='is'),
    Pattern(name='KW_IS_NOT', mode='kw', expr='is[ ]+not'),
    Pattern(name='KW_IN', mode='kw', expr="in"),
    Pattern(name='KW_NOT_IN', mode='kw', expr='not[ ]+in'),
    Pattern(name='KW_NOT', mode='kw', expr='not'),
    Pattern(name='KW_AND', mode='kw', expr='and'),
    Pattern(name='KW_OR', mode='kw', expr='or'),

    Pattern(name='KW_FOR', mode='kw', expr='for'),
    Pattern(name='KW_WHILE', mode='kw', expr='while'),
    Pattern(name='KW_IF', mode='kw', expr='if'),
    Pattern(name='KW_ELIF', mode='kw', expr='elif'),
    Pattern(name='KW_ELSE', mode='kw', expr='else'),

    Pattern(name='BOOL', mode='re', expr='True|False'),
    Pattern(name='VAR', mode='re', expr='[a-zA-Z_][a-zA-Z0-9_]*'),
    Pattern(name='DEC', mode='re', expr='[0-9]+\.[0-9]*|[0-9]*\.[0-9]+'),
    Pattern(name='INT', mode='re', expr='[0-9]+'),
    Pattern(name='STR', mode='re', expr='\".*?\"|\'.*?\''),

    Pattern(name='EQUAL_EQUAL', mode='str', expr='=='),
    Pattern(name='EXCMARK_EQUAL', mode='str', expr='!='),
    Pattern(name='LV_LV', mode='str', expr='<<'),
    Pattern(name='RV_RV', mode='str', expr='>>'),
    Pattern(name='LV_EQUAL', mode='str', expr='<='),
    Pattern(name='RV_EQUAL', mode='str', expr='>='),
    Pattern(name='STAR_STAR', mode='str', expr='**'),
    Pattern(name='SLASH_SLASH', mode='str', expr='//'),

    Pattern(name='DDOT', mode='str', expr=':'),
    Pattern(name='LP', mode='str', expr='('),
    Pattern(name='RP', mode='str', expr=')'),
    Pattern(name='LB', mode='str', expr='['),
    Pattern(name='RB', mode='str', expr=']'),
    Pattern(name='DOT', mode='str', expr='.'),
    Pattern(name='AMPERSAND', mode='str', expr='&'),
    Pattern(name='PIPE', mode='str', expr='|'),
    Pattern(name='LV', mode='str', expr='<'),
    Pattern(name='RV', mode='str', expr='>'),
    Pattern(name='EQUAL', mode='str', expr='='),
    Pattern(name='PLUS', mode='str', expr='+'),
    Pattern(name='MINUS', mode='str', expr='-'),
    Pattern(name='WAVE', mode='str', expr='~'),
    Pattern(name='STAR', mode='str', expr='*'),
    Pattern(name='PERCENT', mode='str', expr='%'),
    Pattern(name='SLASH', mode='str', expr='/'),
    Pattern(name='HAT', mode='str', expr='^'),
    Pattern(name='COMA', mode='str', expr=','),
    Pattern(name='NEWLINE', mode='re', expr='[\n]+', flag=16),

    Pattern(name='INDENT', mode='repeat', expr='\t'),

    Pattern(name='SPACE', mode='re', expr='[ \n\t]+', flag=16, ignore=True),
    Pattern(name='ERROR', mode='re', expr='.+'),
    Pattern(name='EOF', mode='re', expr='', ignore=True)
])
