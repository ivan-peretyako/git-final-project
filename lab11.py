import random
from faker import Faker
fake = Faker("ru_RU")

def generate_name():
	return fake.first_name()

def roll_dice(sides):
	return random.randint(1, sides)

def assign_stats():
	stats = {
		"Strength": roll_dice(20),
		"Agility": roll_dice(20),
		"Intelligence": roll_dice(20),
		"Constitution": roll_dice(20)
	}
	return stats

def format_character_card(name, stats):
	card = f"Имя: {name}\nСила: {stats['Strength']}\nЛовкость: {stats['Agility']}\nИнтеллект: {stats['Intelligence']}\nТелосложение: {stats['Constitution']}"
	return card

def main():
	name = generate_name()
	stats = assign_stats()
	print(format_character_card(name, stats))

if __name__ == "__main__":
	main()