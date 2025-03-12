def greet(a, b):
	if int(b) == 3:
		print("Welcome to my code "+str(a))

	if int(b) == 2:
		print("Willkommen bei meinem code "+str(a))

	if int(b) == 1:
		print("Huānyíng shǐ yòngwǒ de dàimǎ " +str(a))

def name_input(statement):

	if statement == 1:
		name= input("Qǐng shūrù nínde xìngmíng:\n")
		return name

	if statement == 2:
		name= input("Bitte geben Sie Ihren Namen ein:\n")
		return name

	if statement == 3:
		name= input("Please enter your name:\n")
		return name

def language_input ():
	language= input("Please select a language: 1. Mandarin 2. German 3. English:\n")
	return language

language=int(language_input())

name=name_input(language)

greet(name,language)
