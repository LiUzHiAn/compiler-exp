%{
#include "y.tab.h"
void yyerror(const char *msg);
void unrecognized_char(char c);
%}

OPERATOR        [-+*/%()\^\n]
NUM             [1-9][0-9]*|[0]

%%
{NUM}           { yylval = atoi(yytext); return T_NUM; }
{OPERATOR}      { return yytext[0]; }
.               { unrecognized_char(yytext[0]);}
%%

int yywrap(void) { 
    return 1;
}


void unrecognized_char(char c) {
    char buf[32] = "Unrecognized character: ?";
    buf[24] = c;
    yyerror(buf);
}

void yyerror(const char *msg) {
    printf("Error:\n%s\n", msg);
    exit(1);
}