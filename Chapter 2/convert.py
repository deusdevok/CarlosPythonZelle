# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
	print("This program converts a temperature value from Celsius to Fahrenheit.")

	print("Celsius Fahrenheit")
	print("------------------")
	for c in [0,10,20,30,40,50,60,70,80,90,100]: # Temperatures in Celsius
		#celsius = eval(input("What is the Celsius temperature? "))
		#fahrenheit = 9/5 * celsius + 32
		f = 9/5 * c + 32
		#print("The temperature is", fahrenheit, "degrees Fahrenheit.")
		print(c,"    ", f)


	input("Press the <Enter> key to quit.")

main()