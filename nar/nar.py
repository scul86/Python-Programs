def int_to_list (n):
	return map(int,str(n))

def is_narcissistic (n):
	d = int_to_list(n)
	e = 0
	for x in d:
		e = e + x ** len(d)
	return e == n
    
n = 1
while True:
	if is_narcissistic(n):
		print n
	n = n+1