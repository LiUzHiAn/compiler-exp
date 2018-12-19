FUNC @main:
	var i, j, result

	push 1
	pop i

	push 2
	pop j

	push i
	push j
	$my_sum
	pop result

	push result
	print "result is %d\n"

	push 0
	ret ~

ENDFUNC

FUNC @my_sum:
	arg a, b

	push a
	push b
	add
	ret ~

ENDFUNC

