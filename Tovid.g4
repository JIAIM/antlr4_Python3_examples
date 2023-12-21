    grammar Tovid;

    program: statement* EOF;

    statement: funcDeclaration
             | variableDeclaration
             | assignment
             | printStatement
             | ifStatement
             | forStatement
             | returnStatement
             | scanStatement;

    funcDeclaration: 'func' IDENT '(' parameters? ')' block;
    parameters: parameter (',' parameter)*;
    parameter: type IDENT;
    type: 'int' | 'float' | 'bool' | 'string';

    variableDeclaration: (('var' | 'const')? type? IDENT ((':=' expression) | ('=' expression))? ) | booleanExpression;
    assignment: IDENT (':=' expression)? ?;
    printStatement: 'print' '(' ((expression (',' expression)*) | STRING)? ')' ;
    scanStatement: 'scanf' '(' IDENT* ')' ;
    ifStatement: 'if' booleanExpression block ('else' block)?;
    forStatement: 'for' IDENT ':=' expression ';' booleanExpression ';' expression block;
    returnStatement: 'return' expression? ;

    block: '{'  statement* '}';
    expression: assignExpression;

    assignExpression: IDENT ':=' assignExpression
                   | arithmExpression;

    arithmExpression: term (addOp term)*;
    term: factor (('^' | multOp) factor)*;
    factor: unaryOp? (INT | FLOAT | IDENT | BOOLEAN | STRING | '(' assignExpression ')');

    booleanExpression: arithmExpression (compareOp arithmExpression | logicOp booleanExpression)?;

    addOp: '+' | '-';
    multOp: '*' | '/';
    powOp: '^';
    compareOp: '==' | '!=' | '<' | '<=' | '>' | '>=';
    logicOp: '&&' | '||';
    unaryOp: '-';

    INT: '-'? DIGIT+;
    FLOAT: '-'? DIGIT+ '.' DIGIT+;
    BOOLEAN: 'true' | 'false';
    STRING: '"' .*? '"' | '\''.*? '\'';
    IDENT: [a-zA-Z_] [a-zA-Z_0-9]*;
    DIGIT: [0-9];
    COMMENT: '//' ~[\r\n]* -> skip;
    WS: [ \t\r\n]+ -> skip;
