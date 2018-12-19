# Description 
This repo includes an infix to postfix based on `SDT(Syntax-Directed Translation)`. The converter was implemeted with C,Flex and Bison. You should be familiar with their syntax first and you can find many Flex and Bison tutorials in Google.

You can use this converter either in terminal or from a file.By now, the basic operands '+','-','*','/','%','^','(',')' are supported. All the space between the expressions are ignored. The code is easy to understand, feel free to play with it and modify the code. :)

# How to Build

All you need to do is compiling the code by using `Makefile`
```
make
```

If you haven't install `make`,`bison`,`flex`,`gcc`. Please install them like the following command.
 ```
 sudo apt install XXX 
 ```

# How to Use
To input the expressions directly, you just run it like this:
```
./converter
1+2*3/5
```
To input many expressions via a file simultaneously and specify the output file, you can run it like this:
```
./converter < sample.txt > result.txt
```
