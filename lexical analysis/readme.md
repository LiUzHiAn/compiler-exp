# File structure
scanner.l			flex的词法分析文件
token.h				简化fortran语言预定义token类型
fortran_sample.f  	符合词法的简化的FORTRAN源程序
wrong_sample.f  	不符合词法的简化的FORTRAN源程序	

# How to run

```
$ make
$ scanner < fortran_sample.f > result.txt
```
