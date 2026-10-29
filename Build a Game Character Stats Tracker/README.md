# Game Character Stats Manager

## Description
A Python program that simulates a game character's basic statistics, including health, mana, and level. It uses object-oriented programming to manage character attributes, control valid stat ranges, and restore health and mana when the character levels up.

## Features
- **Character Creation:** Initialize a character with a name, 100 health points, 50 mana points, and level 1.
- **Health Management:** Update health while keeping its value between 0 and 100.
- **Mana Management:** Update mana while keeping its value between 0 and 50.
- **Attribute Access:** Use properties to access and manage character attributes.
- **Level Progression:** Increase the character's level and restore health and mana to their maximum values.
- **Character Status Display:** Print the character's name, level, health, and mana in a readable format.

## Concepts Used
- Python Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Encapsulation
- Properties and Setters
- Conditional Statements
- Instance Methods
- String Formatting
- Special Methods (`__str__`)

## How It Works
1. A character is created with default health, mana, and level values.
2. Health and mana can be updated within their allowed ranges.
3. The `level_up()` method increases the character's level and restores health and mana.
4. The `__str__()` method provides a formatted summary of the character's current statistics.

## Example

```python
hero = GameCharacter("Kratos")

hero.health -= 30
hero.mana -= 10

print(hero)

hero.level_up()
print(hero)
```

## Sample Output

```text
Name: Kratos
Level: 1
Health: 70
Mana: 40

Kratos leveled up to 2!
Name: Kratos
Level: 2
Health: 100
Mana: 50
```

## How to Run
1. Make sure Python 3 is installed.
2. Save the program in a `.py` file.
3. Run it using the terminal:

   ```bash
   python game_character.py
   ```

## Purpose
This project demonstrates how object-oriented programming can model game characters, manage attributes safely, and implement basic character progression mechanics.

**Language:** Python 3
