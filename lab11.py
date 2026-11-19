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

def generate_race():
	races = [
		"Человек",
		"Эльф",
		"Гном",
		"Дворф",
		"Орк",
		"Троль",
		"Тифлинг"
	]
	return random.choice(races)

def generate_class():
	classes = [
		"Воин",
		"Паладин",
		"Маг",
		"Чародей",
		"Бард",
		"Жрец",
		"Друид"
	]
	return random.choice(classes)

def format_character_card(name, stats, race, char_class):
	card = (f"Имя: {name}\n"
			f"Раса: {race}\n"
			f"Класс: {char_class}\n"
			f"Сила: {stats['Strength']}\n"
			f"Ловкость: {stats['Agility']}\n"
			f"Интеллект: {stats['Intelligence']}\n"
			f"Телосложение: {stats['Constitution']}"
	)
	return card

def main():
	name = generate_name()
	stats = assign_stats()
	race = generate_race()
	char_class = generate_class()
	print(format_character_card(name, stats, race, char_class))

if __name__ == "__main__":
	main()