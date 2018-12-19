OUT= tcc
TEST_FILE=test.c
SCANNER= scanner.l
PARSER=parser.y

CC=gcc
OBJ=lex.yy.o y.tab.o
TEST_OUT=$(basename $(TEST_FILE)).asm
OUT_FILES=lex.yy.c y.tab.c y.tab.h y.output $(OUT)

.PHONY: build test simulate clean

build: $(OUT)

test: $(TEST_OUT)

simulate: $(TEST_OUT) 
	python3 pysim_for_python3.py $< -da

clean:
	rm -f *.o $(OUT_FILES)

$(TEST_OUT): $(TEST_FILE) $(OUT)
	./$(OUT) < $< > $@

$(OUT): $(OBJ)
	$(CC) -o $(OUT) $(OBJ)

lex.yy.c: $(SCANNER) y.tab.c
	flex $<

y.tab.c: $(PARSER) 
	bison -vdty $<
