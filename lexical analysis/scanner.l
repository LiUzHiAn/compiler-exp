%{
#include "token.h"
int cur_line_num=1;
void init_scanner();
void lex_error(char *msg,int line);
%}

/*类型定义 */
UNSIGNER_INT		([0-9]+)
IDENGTIFIER		([_a-zA-Z][_a-zA-Z0-9]*)
SINGLE_COMMENT		("{"[^\n]*"}")
INVALID_IDENT		([0-9][_a-zA-Z0-9]*)


%%
[\n]			{cur_line_num++;}
[ \t\r\a]+		{/*忽略所有的空格*/}
{SINGLE_COMMENT}	{/*跳过单行注释*/}

"const"			{return T_CONSTSYM;}
"var"			{return T_VARSYM;}
"procedure"		{return T_PROCSYM;}
"begin"			{return T_BEGINSYM;}
"end"			{return T_ENDSYM;}
"odd"			{return T_ODDSYM;}
"if"			{return T_IFSYM;}
"then"			{return T_THENSYM;}
"call"			{return T_CALLSYM;}
"while"			{return T_WHILESYM;}
"do"			{return T_DOSYM;}
"read"			{return T_READSYM;}
"write"			{return T_WRITESYM;}
"+"			{return T_PLUS;}
"-"			{return T_MINUS;}
"*"			{return T_TIMES;}
"/"			{return T_SLASH;}
"="			{return T_EQL;}
"#"			{return T_NEQ;}
"<"			{return T_LSS;}
">"			{return T_GTR;}
":="			{return T_BECOMES;}
"<="			{return T_LEQ;}
">="			{return T_GEQ;}
"("			{return T_LPAREN;}
")"			{return T_RPAREN;}
","			{return T_COMMA;}	
";"			{return T_SEMICOLON;}
"."			{return T_PERIOD;}

{UNSIGNER_INT}		{return T_NUL;}
{IDENGTIFIER}		{return T_IDENT;}
{INVALID_IDENT}		{lex_error("invalid indentifier",cur_line_num);}

.			{lex_error("Unrecognized character",cur_line_num);}

%%


int main(int argc,char *agrv[])
{
	int token;
	init_scanner();
	const char *filename = "token.txt";
	while(token=yylex())
	{	
		// save_token_to_file(filename,token,yytext);
		print_token(token);
        puts(yytext);
	}
	return 0;
}

void init_scanner() {
    printf("%-20s%s\n", "TOKEN-TYPE", "TOKEN-VALUE");
    printf("-------------------------------------------------\n");
}

void lex_error(char* msg, int line) {
    printf("\nError at line %-3d: %s\n\n", line, msg);
}

int yywrap(void) {
    return 1;
}
