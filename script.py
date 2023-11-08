from antlr4 import *
from PythonLexer import PythonLexer
from PythonParser import PythonParser

def main():
    # Get user input or process a file, here we're reading from the command line
    file_inp = ""
    with open("project_deliverable_1_testcase.py", "r") as file:
        file_inp = file.readlines()

    for line in file_inp:
        input_stream = InputStream(line)

        lexer = PythonLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = PythonParser(token_stream)

        try:
            tree = parser.assignment_operators()
            print(f"Result: {tree.toStringTree(recog=parser)}")
        except RecognitionException as e:
            print("Error parsing.\n")

if __name__ == '__main__':
    main()
