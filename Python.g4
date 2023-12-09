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

SPECIAL_CHARS: '.';
CAP: [A-Z];
LOW: [a-z];
UND: '_';
INT: [0-9]+ ('.' [0-9]+)?;
TRE: 'True';
FLE: 'False';
NEWLINE: '\n';
CARRIAGE_RETURN: '\r';
POUND: '#';
TRIPLE_QUOTE: '"""';
TRIPLE_BACK_SLASH: '\'\'\'';

file_input: (assignment_operators | if)* EOF;

assignment_operators: equal | assignment_arithmetic;

assignment_arithmetic: variable ('+=' | '-=' | '*=' | '/=') (variable | expression);

// expression: expression ('*' | '/' | '+' | '-' | '%') expression | variable | '(' expression ')';
expression: expression ('*' | '/' | '+' | '-' | '%') expression | variable | '(' expression ')';

equal: variable '=' equal_operand;

equal_operand: expression | TRE | FLE | string | charquotes | listing | variable;

variable: (CAP | LOW | UND | INT | '-'INT | SPECIAL_CHARS)+;

string: '"' variable '"';

charquotes: '\'' variable '\'';

comp_value: string | charquotes | variable;

listing: '[' ']' | '[' comp_value (',' comp_value)* ']';

WS  :   [ \t\r\n]+ -> skip ;

SINGLE_LINE_COMMENTS : POUND .*? CARRIAGE_RETURN? NEWLINE -> skip ;
MULTI_LINE_COMMENTS : (TRIPLE_QUOTE .*? TRIPLE_QUOTE | TRIPLE_BACK_SLASH .*? TRIPLE_BACK_SLASH) -> skip;


// deliverable 2 - Conditional statements (<, <=, >, >=, ==, !=,and, or, not)

conditional_statements: expression | '(not' expression ')' | conditional_statements ( '<' | '<=' | '>' | '>=' | '==' | '!=' | 'and' | 'or' | 'not') conditional_statements;

// the commented out sections contain the '\t' in the parser, which is for the tab. It's mandatory in Python for if statements
// so I put it in the parser but because the system we're using removes all whitespace when you try compiling it with the test
// case it won't recognize it because the test case is tabless. It's confusing, but the uncommented sections work with the
// test cases.

//if: 'if' conditional_statements ':' ('\t' (assignment_operators | if))* elif;
if: 'if' conditional_statements ':' (assignment_operators | if)* elif;


//elif: else | 'elif' conditional_statements ':' ('\t' (assignment_operators | if))* elif*;
elif: else | 'elif' conditional_statements ':' (assignment_operators | if)* elif*;

//else: 'else:' ('\t' (assignment_operators | if))*;
else: 'else:' (assignment_operators | if)*;


// deliverable 3
// While loop
while_loop: 'while' conditional_statements ':' loop_body;

// For loop
for_loop: 'for' variable 'in' iterable ':' loop_body;

// Iterables for for-loop
iterable: variable | listing;

// Loop body
loop_body: (assignment_operators | if | while_loop | for_loop | comment)*;

// Comments
comment: SINGLE_LINE_COMMENTS
        | MULTI_LINE_COMMENTS;
