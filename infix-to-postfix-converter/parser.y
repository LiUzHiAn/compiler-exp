%{
#include <stdio.h>
#include <math.h>
void yyerror(const char* msg);

int yylex();
%}

%token T_NUM

%left '+' '-'
%left '*' '/' '%'
%left '^'


%%

S   :   S E '\n'        { printf("\n");  printf("result = %d\n", $2);}
    |   /* empty */     { /* empty */ }
    ;

E   :   E '+' E         { $$ = $1 + $3; printf(" +");}
    |   E '-' E         { $$ = $1 - $3; printf(" -");}
    |   E '*' E         { $$ = $1 * $3; printf(" *");}
    |   E '/' E         { $$ = $1 / $3; printf(" /");}
    |   E '%' E         { $$ = $1 % $3; printf(" %%");}
    |   E '^' E         { $$ = (int)pow($1,$3); printf(" ^");}
    |   T_NUM           { $$ = $1;printf(" %d",$1); }
    |   '(' E ')'       { $$ = $2; }
    ;

%%

int main() {
    return yyparse();
}