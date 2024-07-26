import ply.lex as lex
import ply.yacc as yacc

# Kotlin Lexer
tokens = (
    'ID',
    'INT',
    'FLOAT',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ASSIGN',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'IF',
    'ELSE',
    'WHILE',
    'FUN',
    'VAR',
    'LESSTHAN',  # Add LESSTHAN token for '<'
    'GREATERTHAN',  # Add GREATERTHAN token for '>'
    'EQUALS',  # Add EQUALS token for '=='
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_EQUALS = r'=='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove double quotes
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'fun': 'FUN',
    'var': 'VAR',
}

lexer = lex.lex()

# Kotlin Parser
def p_program(p):
    '''
    program : statement
           | program statement
    '''
    pass

def p_statement(p):
    '''
    statement : var_declaration
              | expression SEMICOLON
              | if_statement
              | while_loop
              | function_definition
    '''
    pass

def p_var_declaration(p):
    '''
    var_declaration : VAR ID ASSIGN expression
    '''
    pass

def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression LESSTHAN expression
               | expression GREATERTHAN expression
               | expression EQUALS expression
               | LPAREN expression RPAREN
               | INT
               | FLOAT
               | STRING
               | ID
    '''
    pass

def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression RPAREN LBRACE program RBRACE
                 | IF LPAREN expression RPAREN LBRACE program RBRACE ELSE LBRACE program RBRACE
    '''
    pass

def p_while_loop(p):
    '''
    while_loop : WHILE LPAREN expression RPAREN LBRACE program RBRACE
    '''
    pass

def p_function_definition(p):
    '''
    function_definition : FUN ID LPAREN RPAREN LBRACE program RBRACE
    '''
    pass

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

while True:
    try:
        s = input('Kotlin >>> ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)