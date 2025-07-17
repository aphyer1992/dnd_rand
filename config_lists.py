from weighted_choice import WeightedChoice
import random
rare_class_list = [
    "Psion", "Psychic Warrior", "Soulknife", "Wilder",
    "Ninja", "Scout", "Spellthief",
    "Warlock", "Wu jen",
    "Shugenja", "Spirit Shaman",
    "Ardent", "Divine Mind", "Erudite", "Lurk",
    "Hexblade", "Samurai", "Swashbuckler",
    "Favored Soul", "Healer", "Marshal", "Warmage",
    "Beguiler", "Dragon Shaman", "Duskblade", "Knight",
    "Binder", "Shadowcaster"
]

class_selector = WeightedChoice([
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Wizard",
    lambda: random.choice(rare_class_list)
])


rare_race_selector = WeightedChoice([
    "Aasimar",
    "Tiefling",
    lambda: random.choice(['Air', 'Earth', 'Fire', 'Water']) + " Genasi",
    "Dromite",
    "Goliath",
    "Elan",
    "Half-Giant",
    "Maenad",
    "Wood Elf",
    "Gray Elf",
    "Duergar",
    "Goblin",
    "Hobgoblin",
    "Kobold",
    "Gnoll",
    "Lizardfolk",
    "Orc",
])

race_selector = WeightedChoice([
    "Human",
    "Dwarf",
    "Elf",
    "Gnome",
    "Halfling",
    "Half-Elf",
    "Half-Orc",
    lambda: rare_race_selector.choose()
])

race_selector.set_weight("Human", 4)
race_selector.set_weight("Dwarf", 2)
race_selector.set_weight("Elf", 2)

magic_schools = [
    "Abjuration",
    "Conjuration",
    "Divination",
    "Enchantment",
    "Evocation",
    "Illusion",
    "Necromancy",
    "Transmutation",
]

domains = [
    "Air",
    "Animal",
    "Chaos",
    "Death",
    "Destruction",
    "Earth",
    "Evil",
    "Fire",
    "Good",
    "Healing",
    "Knowledge",
    "Law",
    "Luck",
    "Magic",
    "Plant",
    "Protection",
    "Strength",
    "Sun",
    "Travel",
    "Trickery",
    "War",
    "Water"
]

creature_types = [
    "Aberration",
    "Animal", 
    "Construct",
    "Dragon",
    "Elemental",
    "Fey",
    "Giant",
    "Humanoid (aquatic)",
    "Humanoid (dwarf)",
    "Humanoid (elf)",
    "Humanoid (goblinoid)",
    "Humanoid (gnoll)",
    "Humanoid (gnome)",
    "Humanoid (halfling)",
    "Humanoid (human)",
    "Humanoid (orc)",
    "Humanoid (reptilian)",
    "Magical beast",
    "Monstrous Humanoid",
    "Ooze",
    "Outsider (evil)",
    "Plant",
    "Undead",
    "Vermin"
]

animal_companions = [ 
    "badger", "camel", "dire rat", "dog", "riding dog", "eagle", "hawk", 
    "light horse", "heavy horse", "owl", "pony", "Small viper", "Medium viper", "wolf"
]

energy_types = ['Acid', 'Cold', 'Electricity', 'Fire']
