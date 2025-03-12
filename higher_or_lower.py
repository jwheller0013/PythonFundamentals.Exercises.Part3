from random import randrange

def random_number():
	x= (randrange(10))
	return x

def number_input():
	number= input("Please guess a number between 0-10:")
	return number

def evaluate(a, b):
	if int(a) > int(b):
		print("Too high")
	if int(a) < int(b):
		print("Too low")
	if int(a) == int(b):
		print("Correct")

x= random_number()

number= number_input()

evaluate(x,number)

print("The random number was: " + str(x))
