from antlr4 import *
from PythonLexer import PythonLexer
from PythonParser import PythonParser

def main():
    # Get user input or process a file, here we're reading from the command line
    input_stream = InputStream(input('Enter an expression: '))

    # Create a lexer from the input stream
    lexer = PythonLexer(input_stream)

    # Create a stream of tokens from the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser from the token stream
    parser = PythonParser(token_stream)

    # Attempt to parse the expression (assuming 'expression' is your entry point)
    try:
        tree = parser.expression()
        print(f"Resul: {tree.toStringTree(recog=parser)}")
    except RecognitionException as e:
        print(f"Something went wrong!")

if __name__ == '__main__':
    main()
