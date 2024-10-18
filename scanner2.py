class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value
    
    def __repr__(self):
        return f"<{self.token_type}, {self.value}>"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0  
        self.tokens = []  
        self.current_char = self.source_code[self.position] if self.source_code else None


    def advance(self):
        self.position += 1
        if self.position < len(self.source_code):
            self.current_char = self.source_code[self.position]
        else:
            self.current_char = None

    #State Transitions 
    def scan(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            # identifiers (A-Z)
            elif self.current_char.isalpha() and self.current_char.isupper():
                self.tokens.append(self.state_identifier())
            # assignment operator '='
            elif self.current_char == '=':
                self.tokens.append(Token("ASSIGN", "="))
                self.advance()
            # matrix elements '(n,m)'
            elif self.current_char == '(':
                self.tokens.append(self.state_matrix())
            # operators 'x' and '+'
            elif self.current_char == 'x':
                self.tokens.append(Token("OP_MUL", "x"))
                self.advance()
            elif self.current_char == '+':
                self.tokens.append(Token("OP_ADD", "+"))
                self.advance()
            # state for keyword 'display'
            elif self.current_char == 'd':
                self.tokens.append(self.state_display())
            # for errors 
            else:
                self.tokens.append(Token("ERROR", self.current_char))
                self.advance()

        return self.tokens

    # state for parsing identifiers (single capital letters A-Z)
    def state_identifier(self):
        identifier = self.current_char
        self.advance()  
        return Token("ID", identifier)

    # state for parsing matrix elements 
    def state_matrix(self):
        matrix_value = self.current_char  # MUST start with '(' 
        self.advance()

        while self.current_char is not None and (self.current_char.isdigit() or self.current_char in ',)'):
            matrix_value += self.current_char
            self.advance()

        return Token("MATRIX", matrix_value)

    # state 'display' parsing 
    def state_display(self):
        display_keyword = ""
        for expected_char in "display":
            if self.current_char == expected_char:
                display_keyword += self.current_char
                self.advance()
            else:
                return Token("ERROR", display_keyword + self.current_char)

        return Token("DISPLAY", "display")


# example input 
source_code = """
 = (1,2)
    (3,4)
 = (5,6)
    (7,8)
C = A x B
display C
"""


lexer = Lexer(source_code)
tokens = lexer.scan()

for token in tokens:
    print(token)
