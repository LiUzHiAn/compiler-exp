CC = gcc
OUT = converter
OBJ = lex.yy.o y.tab.o
SCANNER = scanner.l
PARSER = parser.y

build: $(OUT)

clean:
	rm -f *.o lex.yy.c y.tab.c y.tab.h y.output $(OUT)

$(OUT): $(OBJ)
	$(CC) -o $(OUT) $(OBJ)  -lm

lex.yy.c: $(SCANNER) y.tab.c
	flex $<

y.tab.c: $(PARSER)
	bison -vdty $<