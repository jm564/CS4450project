from antlr4 import *
from antlr4.tree.Trees import Trees
from PythonLexer import PythonLexer
from PythonParser import PythonParser

# To generate a .png of the parse tree, you will need to install GraphViz to your Python environment, and then use 'dot -Tpng parse_tree.dot -o parse_tree.png' in an ubuntu/wsl terminal (you may need to also install the ubuntu pkg for GraphViz as well)
# You can download GraphViz to your Python environment by using 'pip install graphviz' 
def to_dot(tree, rule_names):
    def escape(string):
        return string.replace('"', '\\"')

    def iterate_tree(t, buffer, parent_id=0):
        # Unique ID for each node
        node_id = id(t)

        # Get the name of the node
        node_name = Trees.getNodeText(t, rule_names)
        node_name = escape(node_name)

        # Add the node to the graph
        buffer.append(f'  {node_id} [label="{node_name}"];')

        # Connect to parent (if not the root)
        if parent_id:
            buffer.append(f'  {parent_id} -> {node_id};')

        # Visit children
        for child in Trees.getChildren(t):
            iterate_tree(child, buffer, parent_id=node_id)

    buffer = ['digraph G {']
    iterate_tree(tree, buffer)
    buffer.append('}')

    return '\n'.join(buffer)

def main():
    # Get user input or process a file, here we're reading from the command line
    with open("project_deliverable_1_testcase.py", "r") as file:
        file_content = file.read()

    input_stream = InputStream(file_content)
    lexer = PythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PythonParser(token_stream)

    try:
        tree = parser.file_input()
        print(f"Result: {tree.toStringTree(recog=parser)}")
        dot_format = to_dot(tree, parser.ruleNames)


        with open('parse_tree.dot', 'w') as dot_file:
            dot_file.write(dot_format)

        print("DOT file created. You can visualize it using Graphviz.")
    except RecognitionException as e:
        print("Error parsing.\n")

if __name__ == '__main__':
    main()
