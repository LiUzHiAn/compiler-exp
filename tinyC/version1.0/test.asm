FUNC @main:
	var i

	push 0
	pop i

_begWhile_1:
	push i
	push 10
	cmplt
	jz _endWhile_1
	push i
	push 1
	add
	pop i

_begIf_1:
	push i
	push 3
	cmpeq
	push i
	push 5
	cmpeq
	or
	jz _elIf_1
	jmp _begWhile_1
	jmp _endIf_1
_elIf_1:
_endIf_1:

_begIf_2:
	push i
	push 8
	cmpeq
	jz _elIf_2
	jmp _endWhile_1
	jmp _endIf_2
_elIf_2:
_endIf_2:

