### 文件结构

token.h ==> TinyC中所有的token类型
scanner.l ==> 词法分析文件
lex.yy.c ==> flex根据.l文件自动生成
Makefile ==> 文件间的依赖
tinyC-sample.c ==> tinyC源程序示例
result.txt ==> 词法分析结果

# How to run
```
$ make
$ ./scanner < tinyC-sample.c > result.txt
```
