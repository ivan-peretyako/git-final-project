import random
from faker import Faker
fake = Faker("ru_RU")

def generate_name():
	return fake.first_name()

def roll_dice(sides):
	return random.randint(1, sides)

def assign_stats():
	stats = {
		"Strength": roll_dice(6)+5,
		"Agility": roll_dice(6)+5,
		"Intelligence": roll_dice(6)+5,
		"Constitution": roll_dice(6)+5
	}
	return stats

def generate_race():
	races = [
		"Человек",
		"Эльф",
		"Гном"
	]
	return random.choice(races)

def generate_class():
	classes = [
		"Воин",
		"Маг",
		"Вор",
	]
	return random.choice(classes)	

def generate_backstory():
	beginings = [
		"Вы дитя великого героя",
		"Вы бродяга",
		"Вы знатная особа",
		"Вы артист цирка"
	]
	endings = [
		" и вас жестоко предали.",
		" и вы перешели дорогу не тому человеку.",
		" и вы ищите приключений.",
		" и вас вот-вот собираются казнить."
	]
	return random.choice(beginings)+random.choice(endings)

def format_character_card(name, stats, race, char_class, backstory):
	card = (f"Имя: {name}\n"
			f"Раса: {race}\n"
			f"Класс: {char_class}\n"
			f"Сила: {stats['Strength']}\n"
			f"Ловкость: {stats['Agility']}\n"
			f"Интеллект: {stats['Intelligence']}\n"
			f"Телосложение: {stats['Constitution']}\n\n"
			f"Предыстория:\n{backstory}"
	)
	return card

def main():
	name = generate_name()
	race = generate_race()
	char_class = generate_class()
	stats = assign_stats()
	backstory = generate_backstory()
	print(format_character_card(name, stats, race, char_class, backstory))

if __name__ == "__main__":
	main()