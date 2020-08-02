from ..parsing import Parser, Rule, EnumRule


def cls(n):
    assert isinstance(n, int)
    assert n >= 0
    base = '0|C|GI|GS|GA'
    for k in range(1, n + 1):
        base += f'|{k}'
    return base


# def get_indent(lineOrscope):
#     assert isinstance(lineOrscope, Lemma)
#     if 'line' in lineOrscope.names:
#         pass
#     elif ''
#
#
# def build_scope(head, *body):
#     pass


def OpeRule(name, symbol, order, right=None):
    names = f"{name}|{order}|val|ope"
    left = f"left:{cls(order)}"
    if right is None:
        right = f"right:{cls(order - 1)}"
    else:
        right = f"right:{right}"
    return Rule(names, left, symbol, right)


def OpeBlocRule(name, left_symbol, right_symbol, order, right=None):
    names = f"{name}|{order}|val|ope"
    left = f"left:{cls(order)}"
    if right is None:
        right = f"right:{cls(order - 1)}"
    else:
        right = f"right:{right}"
    return Rule(names, left, left_symbol, right, right_symbol)


def LOpeRule(name, symbol, order):
    names = f"{name}|{order}|val|l_ope"
    right = f"right:{cls(order)}"
    return Rule(names, symbol, right)


parser = Parser([
    Rule("int|0|val", "value:INT"),
    Rule("float|0|val", "value:DEC"),
    Rule("str|0|val", "value:STR"),
    Rule("bool|0|val", "value:BOOL"),
    Rule("var|0|val|<args>|<vars>", "name:VAR"),

    Rule("par|0|bloc", "LP", f"inside:{cls(13)}|<args>", "RP"),

    EnumRule("<args>|enum", f"{cls(12)}", "COMA"),

    EnumRule("<vars>|enum", "var", "COMA"),

    EnumRule("<lines>|enum", "<stmt>", "NEWLINE"),

    Rule(f";for|<stmt>|<head>", "KW_FOR", "<vars>", "KW_IN", f"{cls(12)}", "DDOT"),
    Rule(f";while|<stmt>|<head>", "KW_WHILE", f"{cls(12)}", "DDOT"),
    Rule(f";if|<stmt>|<head>", "KW_IF", f"{cls(12)}", "DDOT"),
    Rule(f";elif|<stmt>|<head>", "KW_ELIF", f"{cls(12)}", "DDOT"),
    Rule(f";else|<stmt>|<head>", "KW_ELSE", "DDOT"),

    Rule("__setid__|ope|<stmt>", "left:var", "EQUAL", "right:val"),
    Rule("__setattr__|<stmt>", "obj:val", "DOT", "key:var", "EQUAL", "val:val"),

    OpeBlocRule("__call__|C|<stmt>", "LP", "RP", 0, f"{cls(12)}|<args>"),
    OpeBlocRule("__getitem__|GI", "LB", "RB", 0, "<slice>"),
    OpeBlocRule("__getitem__|GS", "LB", "RB", 0, "val"),
    OpeRule("__getattr__|GA", "DOT", 0, "var"),

    OpeRule("__pow__", "STAR_STAR", 1),

    LOpeRule("__neg__", "MINUS", 2),
    LOpeRule("__pos__", "PLUS", 2),
    LOpeRule("bw_not", "WAVE", 2),

    OpeRule("__mul__", "STAR", 3),
    OpeRule("__truediv__", "SLASH", 3),
    OpeRule("__floordiv__", "SLASH_SLASH", 3),
    OpeRule("__mod__", "PERCENT", 3),

    OpeRule("__add__", "PLUS", 4),
    OpeRule("__sub__", "MINUS", 4),

    OpeRule("bw_l_shift", "LV_LV", 5),
    OpeRule("bw_r_shift", "RV_RV", 5),

    OpeRule("bw_and", "AMPERSAND", 6),

    OpeRule("bw_xor", "HAT", 7),

    OpeRule("bw_or", "PIPE", 8),

    OpeRule("__eq__", "EQUAL_EQUAL", 9),
    OpeRule("__ne__", "EXCMARK_EQUAL", 9),
    OpeRule("__le__", "LV_EQUAL", 9),
    OpeRule("__lt__", "LV", 9),
    OpeRule("__ge__", "RV_EQUAL", 9),
    OpeRule("__gt__", "RV", 9),
    OpeRule("__is__", "KW_IS", 9),
    OpeRule("__is_not__", "KW_IS_NOT", 9),
    OpeRule("__in__", "KW_IN", 9),
    OpeRule("__not_in__", "KW_NOT_IN", 9),

    LOpeRule("__not__", "KW_NOT", 10),

    OpeRule("__and__|", "KW_AND", 11),

    OpeRule("__or__|", "KW_OR", 12),

    Rule(f"tern|13|val", f"true:{cls(12)}", "KW_IF", f"cond:{cls(12)}", "KW_ELSE", f"false:{cls(13)}"),

])
