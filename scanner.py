import re

# Token definitions
TOKENS = [
    ("ID", r'[A-Z]'),  
    ("ASSIGN", r'='),  # assignment operator
    ("MATRIX", r'\(\d+,\d+\)'),  # matrix elements like (1,2)
    ("OP_MUL", r'x'),  # multiplication operator
    ("OP_ADD", r'\+'),  # addition operator
    ("DISPLAY", r'display'),  # display keyword
    ("WHITESPACE", r'\s+'),  # whitespace ?? if needed (should be skipping whitespace here)
]

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value
    
    def __repr__(self):
        return f"<{self.token_type}, {self.value}>"

#scanner function 
def scan(source_code):
    tokens = []
    position = 0
    last_token_type = None  
    while position < len(source_code):
        match = None
        for token_type, token_regex in TOKENS:
            regex = re.compile(token_regex)
            match = regex.match(source_code, position)
            if match:
                text = match.group(0)
                if token_type != "WHITESPACE":  
                    # check for missing identifier before '='
                    if token_type == "ASSIGN" and last_token_type != "ID":
                        tokens.append(Token("ERROR", "Missing identifier before '='"))
                    tokens.append(Token(token_type, text))
                    last_token_type = token_type  # updates the prior token type
                position = match.end(0)
                break
        if not match:
            # treats any unknown characters (not represented by our regex's) as an error 
            unknown_char = source_code[position]
            tokens.append(Token("ERROR", unknown_char))
            position += 1
    return tokens

# example input program 
input_program = """
A = (1,2)
    (3,4)
= (5,6)%_
    (7,8)
C = A x B
dissplay C*
"""

tokens = scan(input_program)

for token in tokens:
    print(token)
