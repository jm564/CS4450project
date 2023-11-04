grammar Python;

// entry point is currently expression

/*
inputs i've tested that you can try on your own machine to replicate my results;

SHOULD WORK;
3 + 4
5 * 6
10 / 2
7 - 1
8 % 3
(3 + 4) * 2
3 * (4 + 5)
(6 + (2 - 3)) * 4
((3)) + 2
1 + 2 * 3
4 * 2 + 6
(7 + 8) / (3 - 2)
(2 + 3 * 4) - 5 / 6 % 7

SHOULDN'T WORK;
+ 3 4
3 +
* 5 6
10 / * 2
(3 + 4
3 * 4)) <-- please at least test this one on your machine, for some reason it passes on mine but i don't see a reason why it should! i think its just an issue with my venv and how i set it up
((6 + 2) - 3 * 4
3 % + 4
5 %
% 3 2
3 + (4 - 5 *
(2 2) + 3
3 & 4
3 ++ 4
5 -- 6
 */

// define rules for python expressions
expression
    : expression ('*' | '/' | '+' | '-' | '%') expression         
    | INT                                  
    | '(' expression ')'                   
    ;

// lexer rules
INT :   [0-9]+ ;                           // for integers
MUL :   '*' ;                              // multiplication
DIV :   '/' ;                              // division
ADD :   '+' ;                              // addition
SUB :   '-' ;                              // subtraction
MOD :   '%' ;                              // modulo
LPAREN: '(' ;                              // left parenthesis
RPAREN: ')' ;                              // right parenthesis

// define a rule for whitespace to ignore it
WS  :   [ \t\r\n]+ -> skip ;              