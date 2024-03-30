import ply.lex as lex

reserved = {
    'sint' : 'type_int',
    'flot' : 'type_float',
    'doub' : 'type_double',
    'chain' : 'type_string',
    'car' : 'type_char',
    're' : 'type_struct_if',
    'redo' : 'type_else',
    'alor' : 'type_while',
    'len' : 'type_len',
    'and' : 'type_and',
    'or' : 'type_or',
    'not' : 'type_not',
    'right' : 'type_true',
    'lie' : 'type_false',
    'noBou' : 'type_void',
    'reto' : 'type_return',
    'prime' : 'type_print',
    'read'  : 'type_input',
    'pou' : 'type_for',
    'brok' : 'type_break',
    'Bou' : 'type_def',
    'clash' : 'type_class',
    'callin' : 'type_import',
    'frome' : 'type_from',
    'let' : 'type_do',
    'fool' : 'type_bool',
    'endBou' : 'type_finaldef',
    'end' : 'type_endvoid',
}

 # List of token names.   This is always required
tokens = [
    'num',
    'Sum',
    'Res',
    'Mul',
    'Div',
    'lparen',
    'rparen',
    'asignacion',
    'menor_que',
    'mayor_que',
    'igual_que',
    'diferente_que',
    'mayorIgual_que',
    'menorIgual_que',
    'lbracket',
    'rbracket',
    'lkey',
    'rkey',
    'dotncomma',
    'lincomment',
    'mulcomment',
    'doublequote',
    'simplequote',
    'ID',
    'mod',
    'decimal',
] + list(reserved.values())

 # Regular expression rules for simple tokens
t_Sum  = r'\+'
t_Res   = r'-'
t_Mul   = r'\*'
t_Div  = r'/'
t_lparen  = r'\('
t_rparen  = r'\)'
t_asignacion  = r'\='
t_menor_que  = r'\<'
t_mayor_que  = r'\>'
t_igual_que  = r'=='
t_diferente_que  = r'\!\='
t_mayorIgual_que  = r'\>\='
t_menorIgual_que  = r'\<\='
t_lbracket  = r'\{'
t_rbracket  = r'\}'
t_lkey  = r'\['
t_rkey  = r'\]'
t_dotncomma = r'\;'
t_lincomment = r'@.*'
t_mulcomment = r'@°°*(.|\n)*?°°@*'
t_doublequote = r'\".*\"'
t_simplequote = r'\'.*?\''
t_mod = r'\%'
#t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_decimal = r'[0-9]+\.[0-9]+'


def t_id(t):
  r'[a-zA-Z_]+([a-zA-Z0-9_]*)*'
  t.type = reserved.get(t.value, 'ID') 
  return t



#t_NUMBER  = r'\d+'
def t_num(t):
    r'\d+'
    t.value = int(t.value)  
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
# Build the lexer
lexer = lex.lex()


# Give the lexer some input
def tokenize_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        lexer.input(data)
        tokens_list = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens_list.append({'type': tok.type, 'lexeme': tok.value, 'line': tok.lineno, 'column': tok.lexpos})
    return tokens_list

# Test de la función
if __name__ == '__main__':
    file_path = 'Funciones.txt'
    tokens = tokenize_file(file_path)
    for token in tokens:
        print(token)
