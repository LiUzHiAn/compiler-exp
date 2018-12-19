# How to run 

## 一键式命令

test.c 是tinyC源程序，`$ make test`后将生成test.asm的Pcode代码，再`$ make simulate`即可运行Pcode代码
```
$ make
$ make test
$ make simulate
```


## 运行你自己的源文件
```
$ make
$ tcc < yourfile.c > yourfile.asm
直接运行得出结果
$ python3 pysim_for_python3.py yourfile.asm -a
或者单步执行
$ python3 pysim_for_python3.py yourfile.asm -da

```
