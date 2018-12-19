# How to run

feel free to modify the code in `run.py`
```
$ python3 run.py 
```

# File structure
grammar.txt			给定算法优先文法的产生式


# Grammar example

```
S->#E#
E->E+T
E->T
T->T*F
T->F
F->P^F
F->P
P->(E)
P->i
```


