import re

# regular expression for tokens
TOKENS = [
    (r'[ \n\t]+', None), # Whitespace
    (r'/\*.*?\*/', None), # Comment
    (r'[0-9]+\.[0-9]+' , 'FLOAT'), # Float constant
    (r'[0-9]+', 'INTEGER'), # Integer constant
    (r'"[^"]*"', 'STRING'), # String constant
    (r'[a-zA-Z][a-zA-Z0-9_]*', 'IDENTIFIER'), # Identifier
    (r'[+\-*/%]', 'OPERATOR'), # Arithmetic operator
    (r'[=<>!]=?', 'OPERATOR'), # Comparison operator
    (r'[(){}\[\],.;]', 'PUNCTUATION') # Punctuation
]

# tokenize the input
def tokenize(code):
    tokens = []
    while code:
        match = None
        for pattern, token_type in TOKENS:
            regex = re.compile('^' + pattern)
            match = regex.search(code)
            if match:
                if token_type:
                    tokens.append((match.group(0), token_type))
                break
        if not match:
            raise SyntaxError('Invalid syntax near %r' % code[0])
        code = code[match.end():]
    return tokens

filename ='./Simple.txt'
with open(filename, 'r') as file:
    code = file.read()
tokens = tokenize(code)
print(tokens)
