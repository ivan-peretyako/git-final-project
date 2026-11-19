import random
from faker import Faker
fake = Faker("ru_RU")

def generate_name():
	return fake.first_name()

def format_character_card(name):
	return f"Имя: {name}"	

def main():
	name = generate_name()
	print(format_character_card(name))

if __name__ == "__main__":
	main()