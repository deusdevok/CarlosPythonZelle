def main():
	print("Welcome to some calculator")
	for _ in range(100):
		print("Enter your expression below...")
		res = eval(input("> "))
		print("The answer is", res)

main()