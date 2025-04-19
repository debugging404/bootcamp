my_height = 168
my_name = "Phu"

print(my_height)
print(my_name)

acceleration = 10
acceleration = 20
print(acceleration)


inplayer_health = 1000


# reduce by 100 here
player_health = inplayer_health - 100

print(player_health)

# summation = a + b  # Addition
# difference = a - b # Subtraction
# product = a * b    # Multiplication
# quotient = a / b   # Division

player_health = 1000
armor_multiplier = 2

# create armored_health here
armored_health = player_health * armor_multiplier
print(armored_health)

player_health = 100
poison_damage = -10

# don't touch below this line

player_poison_health = player_health + poison_damage

print(player_poison_health)


# Multi-Line Comments (Aka docstrings)
"""
    the code found below
    will print 'Hello, World!' to the console
"""
print("Hello, World!")


# the best_sword variable holds the value of the best sword in the game
best_sword = "scimitar"
print(best_sword)

player_health = 100

player_has_magic = True

# don't touch below this line
print("player_health is a/an ", type(player_health).__name__)
print("player_has_magic is a/an ", type(player_has_magic).__name__)


name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print(f"{name} is a {race} who is {age} years old.")


# create the empty "enemy" variable here
enemy = None

# don't touch below this line
print(enemy is None)

##

sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print(f"{sentence_start} {player1_health} {sentence_end}")
print(f"{sentence_start} {player2_health} {sentence_end}")


sword_name, sword_damage, sword_length = "Excalibur", 10, 200
# same as
sword_name = "Excalibur"
sword_damage = 10
sword_length = 200


quest_start = "You there! Adventurer!"
quest_middle = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
quest_objective = "Bring back 8 of their axes as proof of your hard work."
space = " "

# don't touch above this line
print(f"{quest_start}\n{quest_middle}\n{quest_end} {quest_objective}")


game_one_score = 97
game_two_score = 92
game_three_score = 106
game_four_score = 105

# Don't touch above this line

average_score = (game_one_score + game_two_score +
                 game_three_score + game_four_score) / 4

# Don't touch below this line

print(round(average_score))
