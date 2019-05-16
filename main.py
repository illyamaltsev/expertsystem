import sys

import config


def read_all(filename):
    f = open(filename, 'r')
    file_content = f.read()
    f.close()
    return file_content


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
            tokens.append(("true facts", ""))
        elif c is "?":
            tokens.append(("question facts", ""))
        elif c is "\n":
            tokens.append(("\n", ""))
        elif c is "#":
            index = content.find('\n', i, len(content) - 1)
            if index == -1:
                index = len(content)
            tokens.append(("comment", content[i:index]))
            i = index - 1
        elif c in config.facts:
            tokens.append(("fact", c))
        elif c in config.operations.keys():
            tokens.append(("operation", config.operations[c]))
        i = i + 1

    return tokens


def main(argc, argv):
    A = True
    B = False

    C = A and B







    filename = 'test.txt'
    f_content = read_all(filename)
    tokens = lex(f_content)
    for t in tokens:
        print(t)
    pass


main(len(sys.argv), sys.argv)