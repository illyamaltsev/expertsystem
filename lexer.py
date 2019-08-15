import config


# lexer
def lex(content):

    # not secured start
    content = content.replace('*', '').replace('$', '')
    content = content.replace('<=>', '$')
    content = content.replace('=>', '*')
    # not secured end

    tokens = []
    i = 0
    while i < len(content):
        c = content[i]
        if c is "=":
            tokens.append(("true_facts", ""))
        elif c is "?":
            tokens.append(("question_facts", ""))
        elif c is "\n":
            tokens.append(("\n", ""))
        elif c is "#":
            index = content.find('\n', i, len(content) - 1)
            if index == -1:
                index = len(content)
            # tokens.append(("comment", content[i:index]))
            i = index - 1
        elif c in config.facts:
            tokens.append(("fact", c))
        elif c in config.operations.keys():
            tokens.append(("operation", config.operations[c]))
        i = i + 1

    return tokens