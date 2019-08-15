import sys
import json

from reader import read_all
from lexer import lex
from parser import parse


def main(argc, argv):
    filename = 'test.txt'
    f_content = read_all(filename)
    tokens = lex(f_content)
    tf, qf, rules = parse(tokens)

    print("tf", tf, "\n")
    print("qf", qf, "\n")
    for r in rules:
        print(json.dumps(r, indent=2))
    pass


main(len(sys.argv), sys.argv)
