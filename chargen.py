import random
from typing import Union, Callable, Any
from config_lists import *
from weighted_choice import WeightedChoice  

global_stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

bonus_selector = WeightedChoice([
    lambda _: "Domain Blessing: you gain the domain power of the " + random.choice(domains) + " domain and may cast its spells up to half your level once per day each.",
    lambda _: random.choice(energy_types) + " resistance: gain resistance 5, increasing by 5 each 5 levels.",
    lambda _: random.choice(creature_types) + " Hunter: you gain a +2 favored enemy bonus against that creature type, increasing by 1 each 5 levels.",
    'Great Fortitude: you gain a +2 bonus on Fortitude saves.',
    'Lightning Reflexes: you gain a +2 bonus on Reflex saves.',
    'Iron Will: you gain a +2 bonus on Will saves.',
    'Fury: gain 1/day Rage (as the barbarian ability).',
    lambda _: 'Skinchanger: 1/day Wild Shape (as the druid ability), only into a ' + random.choice(animal_companions) + '.',
    'Devourer: once per day per level, you may use Death Knell (as the cleric spell).',
    lambda _x: random.choice(['Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy']) + ' Immunity: you have automatic unbeatable SR against the listed school.  (This cannot be lowered voluntarily).',
])

penalty_selector = WeightedChoice([
    lambda _: random.choice(energy_types) + " vulnerability: take double damage from that energy type.",
    'Maimed: you have only one hand',
    'Lame: you have a permanent limp, reducing your speed by 10 feet',
    'Frail: you take a -3 penalty on Fortitude saves',
    'Stumble: you take a -3 penalty on Reflex saves',
    'Weak Willed: you take a -3 penalty on Will saves',
    lambda _: random.choice(creature_types) + ' Phobia: creatures of that type have Fearful Presence against you.',
    lambda _: random.choice(['Abjuration', 'Conjuration', 'Transmutation']) + ' Immunity: you have automatic unbeatable SR against the listed school.  (This cannot be lowered voluntarily).',
    lambda char: None if char['char_class'] != 'Wizard' else 'Extra Blocked School: ' + random.choice([c for c in magic_schools if c not in char['requirement']])
])

def roll_die(n):
    return random.randint(1, n)

def roll_stat():
    rolls = [roll_die(6) for _ in range(4)]
    return sum(rolls) - min(rolls)

def print_character(character):
    print(f"""{character['race']} {character['char_class']}\nStats (before racial bonuses):""")
    for stat in global_stats:
        print(f"{stat}: {character['stats'][stat]}")
    if len(character['requirement']):
        print(f"Class-specific requirement: {character['requirement']}")
    if 'bonus' in character:
        print(f"Bonus: {character['bonus']}")
    if 'penalty' in character:
        print(f"Penalty: {character['penalty']}")
    print()

def random_wizard_schools():
    focus = random.choice(magic_schools + ['Universalist'])
    if focus == 'Universalist':
        return('Generalist wizard with no school focus')
    else:
        prohibited = ' and '.join(random.sample([ s for s in magic_schools if s != focus], 2))
        return(f"Specialist wizard with focus on {focus} and prohibited schools {prohibited}")

def random_cleric_domains():
    my_domains = ' and '.join(random.sample(domains, 2))
    return f"{my_domains} domains"

def random_favored_enemy():
    return f"Favored enemy: {random.choice(creature_types)}"

def random_animal_companion():
    return(f"Animal companion: {random.choice(animal_companions)}")

def gen_character_requirement(character):
    if character['char_class'] == 'Wizard':
        return random_wizard_schools()
    elif character['char_class'] == 'Cleric':
        return random_cleric_domains()
    elif character['char_class'] == 'Ranger':
        return random_favored_enemy()
    elif character['char_class'] == 'Druid':
        return random_animal_companion()
    else:
        return ''

def gen_character():
    character = {
        'stats': {stat: roll_stat() for stat in global_stats},
        'char_class': class_selector.choose(),
        'race': race_selector.choose()
    }

    character['requirement'] = gen_character_requirement(character)
    done = False

    random_bonus = 2 if len(character['requirement']) else 1
    while not done:
        print_character(character)
        print("To swap two stats, type 'swap <stat1> <stat2>'.")
        print("To remove your class-specific requirement, type 'remove requirement'.")
        print("However, be aware that this will result in your character getting worse random items/bonuses/penalties during the next stage.")
        print("To finish, type 'done'.")
        user_input = input("Your choice: ").strip().upper()
        if user_input == "DONE":
            done = True
        elif user_input.startswith("SWAP "):
            _, stat1, stat2 = user_input.split()
            if stat1 in global_stats and stat2 in global_stats:
                character['stats'][stat1], character['stats'][stat2] = character['stats'][stat2], character['stats'][stat1]
                print(f"Swapped {stat1} and {stat2}.")
                random_bonus -= 1
            else:
                print(f"Invalid stats for swapping: you submitted {stat1} and {stat2}.")
                print("Options are: " + ", ".join(global_stats))
        elif user_input == "REMOVE REQUIREMENT":
            if character['requirement']:
                print(f"Removing requirement: {character['requirement']}")
                character['requirement'] = []
                random_bonus -= 1
            else:
                print("No requirement to remove.")
        else:
            print("Invalid command. Please try again.")
    
    if random.random() * 6 < (2 + random_bonus):
        character['bonus'] = bonus_selector.choose()
    
    if random.random() * 6 < (2 - random_bonus):
        character['penalty'] = penalty_selector.choose()

    print("\nFinal Character:")
    print_character(character)

random.seed('Sean_test_2')
for i in range(4):
    gen_character()
