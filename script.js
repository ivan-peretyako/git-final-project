function getRandomElement(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

function generateName() {
    const names = [
        "Александр", "Дмитрий", "Максим", "Иван", "Артем",
        "Анна", "Мария", "Елена", "Дарья", "Алина"
    ];
    return getRandomElement(names);
}

function rollDice(sides) {
    return Math.floor(Math.random() * sides) + 1;
}

function assignStats() {
    return {
        Strength: rollDice(6) + 5,
        Agility: rollDice(6) + 5,
        Intelligence: rollDice(6) + 5,
        Constitution: rollDice(6) + 5
    };
}

function generateRace() {
    const races = ["Человек", "Эльф", "Гном"];
    return getRandomElement(races);
}

function generateClass() {
    const classes = ["Воин", "Маг", "Вор"];
    return getRandomElement(classes);
}

function generateBackstory() {
    const beginnings = [
        "Вы дитя великого героя",
        "Вы бродяга",
        "Вы знатная особа",
        "Вы артист цирка"
    ];
    const endings = [
        " и вас жестоко предали.",
        " и вы перешли дорогу не тому человеку.",
        " и вы ищите приключений.",
        " и вас вот-вот собираются казнить."
    ];
    return getRandomElement(beginnings) + getRandomElement(endings);
}

function formatCharacterCard(name, stats, race, charClass, backstory) {
    return `Имя: ${name}\n` +
           `Раса: ${race}\n` +
           `Класс: ${charClass}\n` +
           `Сила: ${stats.Strength}\n` +
           `Ловкость: ${stats.Agility}\n` +
           `Интеллект: ${stats.Intelligence}\n` +
           `Телосложение: ${stats.Constitution}\n\n` +
           `Предыстория:\n${backstory}`;
}

document.getElementById("generate-btn").addEventListener("click", () => {
    const name = generateName();
    const race = generateRace();
    const charClass = generateClass();
    const stats = assignStats();
    const backstory = generateBackstory();

    const cardText = formatCharacterCard(name, stats, race, charClass, backstory);
    
    const resultBox = document.getElementById("result-box");
    resultBox.textContent = cardText;
});
