# CS4450project
WELCOME TO OUR GIT REPO FOR THE CS4450 PARSER PROJECT!

Team members are: Jeffrey Morgan, Benjamin Williams, Jules Maslak-Hopper, Alex Osborne, Michael Hackmann

To use: download the script.py, the Python.g4, the relevant testcase.py, and for same dependency sake the antlr.jar.
1) With all three files in the same directory run the following command:
2) java -jar antlr-4.13.1-complete.jar  -Dlanguage=Python3 -visitor -listener Python.g4
This creates the PythonLexer.py and PythonParser.py files necessary to run script.py
3) Then update the file name on line 8 in the script.py to reflect which test case file you want to test.
4) Run script.py, parse tree for each line of file should be printed to terminal.



