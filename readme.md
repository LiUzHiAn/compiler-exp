# 说明
This repo includes all  the source code of experiment when attending compiler principles class. Feel free to modify the code and use it anywhere you want.

### 环境
- ubuntu 18.04
- python 3.6
- Gcc 7.3.0
- Flex 2.6.4
- Bison 3.0.4


### NOTICE
`源代码`:
`Author`: Liu Zhian
`Time`:2018/12/09


### 文件结构
- lexical analysis

简化的FORTRAN语言词法分析器（支持出错信息标识）
- nfa2dfa

将NFA确定化为DFA,NFA和DFA都是用json文件定义的
- operator_prec_grammar

算法优先文法求FIRSTVT()集合和LASTVT()集合
- infix-to-postfix-converter

将中缀表达式转换为后缀表达式
- tinyC

一个简单版C语言的编译器，我只实现了前端部分，生成Pcode代码。并参考[pandolia](http://pandolia.net/tinyc/index.html)写的Pcode虚拟机运行Pcode代码,在此特别提出鸣谢。

