# http://tinyurl.com/j2scn4f

try:
	a = input("type a number:")
	b = input("type another:")
	a = int(a)
	b = int(b)
	print(a/b)
except (ZeroDivisionError, ValueError):
	print("Invalid input.")


