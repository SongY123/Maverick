grammar Maverick;

chunk
    : block EOF
    ;

block
    : stat* laststat?
    ;

stat
    : ';'
    | varinit
    | varassign
    | functioncall
    | label
    | break
    | whileblock
    | repeatblock
    | ifblock
    | forequalblock
    | forinblock
    | funcdef
    ;

varinit
    : type varlist '=' explist
    ;

varassign
    : var '=' exp
    ;

whileblock
    : 'while' condition 'do' block 'end'
    ;

repeatblock
    : 'repeat' block 'until' condition
    ;

ifblock
    : ifconditionblock (elseifconditionblock)* (elseconditionblock)? 'end'
    ;

ifconditionblock
    : 'if' condition 'then' block
    ;

elseifconditionblock
    : 'elseif' condition 'then' block
    ;

elseconditionblock
    : 'else' block
    ;

forequalblock
    : 'for' (type)? NAME '=' exp ',' exp (',' exp)? 'do' block 'end'
    ;

forinblock
    : 'for' namelist 'in' explist 'do' block 'end'
    ;

funcdef
    : 'function' type funcname '(' parlist? ')' funcbody
    ;

laststat
    : 'return' exp? | break | continue ';'?
    ;

label
    : '::' NAME '::'
    ;

funcname
    : NAME ('.' NAME)* (':' NAME)?
    ;

varlist
    : var (',' var)*
    ;

namelist
    : type NAME (',' type NAME)*
    ;

explist
    : (exp ',')* exp
    ;

condition
    : exp
    ;

exp
    : 'nil'                                 # nil_expr
    | ('false' | 'true')                    # truefalse_expr
    | number                                # number_expr
    | string                                # string_expr
    | '...'                                 # more_expr
    | functioncall                          # functioncall_expr
    | varOrExp                              # varorexp_expr
    | tableconstructor                      # tableconstructor_expr
    | <assoc=right> exp operatorPower exp   # power_expr
    | operatorUnary exp                     # unary_expr
    | exp operatorMulDivMod exp             # muldivmod_expr
    | exp operatorAddSub exp                # addsub_expr
    | <assoc=right> exp operatorStrcat exp  # strcat_expr
    | exp operatorComparison exp            # comp_expr
    | exp operatorAnd exp                   # and_expr
    | exp operatorOr exp                    # or_expr
    | exp operatorBitwise exp               # bitwise_expr
    ;

functioncall
    : printfFunction
    | scanfFunction
    | selffunctioncall
    ;

varOrExp
    : var | '(' exp ')'
    ;

var
    : (NAME | '(' exp ')' varSuffix) varSuffix*
    ;

varSuffix
    : nameAndArgs* ('[' exp ']' | '.' NAME)
    ;

nameAndArgs
    : (':' NAME)? args
    ;

args
    : '(' explist? ')' | tableconstructor | string
    ;

funcbody
    : block 'end'
    ;

// TODO 可变参数
parlist
    : namelist (',' '...')? | '...'
    ;

tableconstructor
    : '{' fieldlist? '}'
    ;

fieldlist
    : field (fieldsep field)* fieldsep?
    ;

field
    : '[' exp ']' '=' exp | NAME '=' exp | exp
    ;

fieldsep
    : ',' | ';'
    ;

operatorOr
	: 'or';

operatorAnd
	: 'and';

operatorComparison
	: '<' | '>' | '<=' | '>=' | '!=' | '==';

operatorStrcat
	: '..';

operatorAddSub
	: '+' | '-';

operatorMulDivMod
	: '*' | '/' | '%';

operatorBitwise
	: '&' | '|' | '~' | '<<' | '>>';

operatorUnary
    : 'not' | '#' | '-' | '~';

operatorPower
    : '^';

number
    : myINT | myHEX | myFLOAT
    ;

string
    : NORMALSTRING | CHARSTRING | LONGSTRING
    ;

type
    : 'void'
    | 'byte'
    | 'boolean'
    | 'int'
    | 'float'
    ;
myINT : INT;
myHEX : HEX;
myFLOAT : FLOAT;
break : 'break';
continue : 'continue';

// LEXER

NAME
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

NORMALSTRING
    : '"' ( EscapeSequence | ~('\\'|'"') )* '"'
    ;

CHARSTRING
    : '\'' ( EscapeSequence | ~('\''|'\\') )* '\''
    ;

LONGSTRING
    : '[' NESTED_STR ']'
    ;

fragment
NESTED_STR
    : '=' NESTED_STR '='
    | '[' .*? ']'
    ;

INT
    : Digit+
    ;

HEX
    : '0' [xX] HexDigit+
    ;

FLOAT
    : Digit+ '.' Digit* ExponentPart?
    | '.' Digit+ ExponentPart?
    | Digit+ ExponentPart
    ;

fragment
ExponentPart
    : [eE] [+-]? Digit+
    ;

fragment
HexExponentPart
    : [pP] [+-]? Digit+
    ;

fragment
EscapeSequence
    : '\\' [abfnrtvz"'|$#\\]   // World of Warcraft Lua additionally escapes |$#
    | '\\' '\r'? '\n'
    | DecimalEscape
    | HexEscape
    | UtfEscape
    ;

fragment
DecimalEscape
    : '\\' Digit
    | '\\' Digit Digit
    | '\\' [0-2] Digit Digit
    ;

fragment
HexEscape
    : '\\' 'x' HexDigit HexDigit
    ;

fragment
UtfEscape
    : '\\' 'u{' HexDigit+ '}'
    ;

fragment
Digit
    : [0-9]
    ;

fragment
HexDigit
    : [0-9a-fA-F]
    ;

fragment
SingleLineInputCharacter
    : ~[\r\n\u0085\u2028\u2029]
    ;

COMMENT
    : '--[' NESTED_STR ']' -> channel(HIDDEN)
    ;

LINE_COMMENT
    : '--' SingleLineInputCharacter* -> channel(HIDDEN)
    ;

WS
    : [ \t\u000C\r\n]+ -> skip
    ;

SHEBANG
    : '#' '!' SingleLineInputCharacter* -> channel(HIDDEN)
    ;

/*
Inner Function
*/
printfFunction
    : 'printf' '(' string (',' (var | exp))* ')'
    ;

scanfFunction
	  : 'scanf' '(' string (',' (var | exp))* ')'
	  ;

selffunctioncall
    : varOrExp nameAndArgs+
    ;