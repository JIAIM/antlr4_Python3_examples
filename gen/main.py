from antlr4 import *
from TovidLexer import TovidLexer
from TovidParser import TovidParser


# from https://github.com/antlr/antlr4/blob/master/runtime/Python3/bin/pygrun
# this is a python version of TestRig
def format_tree(in_string):
    indent_size = 3
    add_indent = ' ' * indent_size
    out_string = in_string[0]  # no indent for 1st (
    indent = ''
    for i in range(1, len(in_string)):
        if in_string[i] == '(' and in_string[i + 1] != ' ':
            indent += add_indent
            out_string += "\n" + indent + '('
        elif in_string[i] == ')':
            out_string += ')'
            if len(indent) > 0:
                indent = indent.replace(add_indent, '', 1)
        else:
            out_string += in_string[i]
    return out_string


file_name = 'test.tovid'
input_stream = FileStream(file_name)
lexer = TovidLexer(input_stream)
print('input_stream:')
print(input_stream)
print()
token_stream = CommonTokenStream(lexer)
token_stream.fill()
print('tokens:')
for token in token_stream.tokens:
    print(token)
print()

parser = TovidParser(token_stream)
tree = parser.program()
print('tree:')
tree_str = tree.toStringTree(recog=parser)
print(format_tree(tree_str))
