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

CAP: [A-Z];
LOW: [a-z];
UND: '_';
INT: [0-9]+ ('.' [0-9]+)?;
TRE: 'True';
FLE: 'False';

file_input: (assignment_operators)* EOF;

assignment_operators: equal | assignment_arithmetic;

assignment_arithmetic: variable ('+=' | '-=' | '*=' | '/=') (variable | expression);

expression: expression ('*' | '/' | '+' | '-' | '%') expression | variable | '(' expression ')';

equal: variable '=' equal_operand;

equal_operand: expression | TRE | FLE | string | charquotes | listing | variable;

variable: (CAP | LOW | UND | INT)+;

string: '"' variable '"';

charquotes: '\'' variable '\'';

comp_value: string | charquotes | variable;

listing: '[' ']' | '[' comp_value (',' comp_value)* ']';

WS  :   [ \t\r\n]+ -> skip ;  
