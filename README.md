# CS4450project
WELCOME TO OUR GIT REPO FOR THE CS4450 PARSER PROJECT!

Team members are: Jeffrey Morgan, Benjamin Williams, Jules Maslak-Hopper, Alex Osborne, Michael Hackmann

## How to use
1. Pull the repo and open a Python terminal at the location of the script
2. With all three files in the same directory run the following command to the Python terminal: 'java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -listener Python.g4' This creates the PythonLexer.py and PythonParser.py files necessary to run script.py. Note that you will need Java for this.
3. Then, update the file name on line 8 in the script.py to reflect which test case file you want to test.
4. Run script.py, parse tree for given file should be printed to terminal.
5. (Optional) If you want to create a .png, you will need to install GraphViz to your Python environment, and then use 'dot -Tpng parse_tree.dot -o parse_tree.png' in an ubuntu/wsl terminal (you may need to also install the ubuntu pkg for GraphViz as well, which can be found at https://www.graphviz.org/download/, you can also find other compatible versions as well)

DEMO VIDEO : https://www.youtube.com/watch?v=q20vMddxblM
