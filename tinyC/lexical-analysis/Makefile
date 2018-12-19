out:scanner

lex.yy.c:scanner.l
	flex scanner.l

scanner:lex.yy.c token.h
	gcc -o scanner lex.yy.c 


