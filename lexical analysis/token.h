/*
	token 的编号原则为：
	单字符运算符的 token 编号就是其字符的数值；
	其他类型的 token 则从 256 开始编号。
*/ 
#include<stdio.h>
#include<string.h>

#ifndef TOKEN_H
#define TOKEN_H

typedef enum{
	T_NUL=1,T_IDENT,T_PLUS,T_MINUS,T_TIMES,T_SLASH,T_EQL,
	T_NEQ,T_LSS,T_LEQ,T_GTR,T_GEQ,T_BECOMES,

	T_CONSTSYM,T_VARSYM,T_PROCSYM,T_BEGINSYM,T_ENDSYM,
	T_ODDSYM,T_IFSYM,T_THENSYM,T_CALLSYM,T_WHILESYM,
	T_DOSYM,T_READSYM,T_WRITESYM,
	
	T_LPAREN,T_RPAREN,T_COMMA,T_SEMICOLON,T_PERIOD

}TokenType;

static void save_token_to_file(const char *filename,int token,char *yytext)
{
	static char *token_strs[]={
		
		"T_NUL","T_IDENT","T_PLUS","T_MINUS","T_TIMES","T_SLASH","T_EQL",
		"T_NEQ","T_LSS","T_LEQ","T_GTR","T_GEQ","T_BECOMES",

		"T_CONSTSYM","T_VARSYM","T_PROCSYM","T_BEGINSYM","T_ENDSYM",
		"T_ODDSYM","T_IFSYM","T_THENSYM","T_CALLSYM","T_WHILESYM",
		"T_DOSYM","T_READSYM","T_WRITE_SYM",
		
		"T_LPAREN","T_RPAREN","T_COMMA","T_SEMICOLON","T_PERIOD"
	};

	FILE *fp=fopen(filename,"a");
	fprintf(fp,"%s",token_strs[token-1]);
	fprintf(fp,"%c",',');
	fprintf(fp,"%s",yytext);
	fprintf(fp,"%c",'\n');
	fclose(fp);
	
}


static void print_token(int token)
{
	static char *token_strs[]={
		
		"T_NUL","T_IDENT","T_PLUS","T_MINUS","T_TIMES","T_SLASH","T_EQL",
		"T_NEQ","T_LSS","T_LEQ","T_GTR","T_GEQ","T_BECOMES",

		"T_CONSTSYM","T_VARSYM","T_PROCSYM","T_BEGINSYM","T_ENDSYM",
		"T_ODDSYM","T_IFSYM","T_THENSYM","T_CALLSYM","T_WHILESYM",
		"T_DOSYM","T_READSYM","T_WRITE_SYM",
		
		"T_LPAREN","T_RPAREN","T_COMMA","T_SEMICOLON","T_PERIOD"
	};
	 printf("%-20s", token_strs[token-1]);
}


#endif
