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
    #lambda race: get_preferred_class(race), once I have those implemented
    lambda _: random.choice(rare_class_list)
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
    lambda _: rare_race_selector.choose()
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

weapons_raw = [
    ['Dagger', 'Light', 'Simple', 'PS', 1],
    ['Light Mace', 'Light', 'Simple', 'B', 1],
    ['Sickle', 'Light', 'Simple', 'S', 0.2],
    ['Club', 'One-Handed', 'Simple', 'B', 0.2],
    ['Heavy Mace', 'One-Handed', 'Simple', 'B', 1],
    ['Morningstar', 'One-Handed', 'Simple', 'BP', 1],
    ['Shortspear', 'One-Handed', 'Simple', 'P', 1],
    ['Spear', 'Two-Handed', 'Simple', 'P', 1],
    ['Longspear', 'Two-Handed', 'Simple', 'P', 1],
    ['Quarterstaff', 'Two-Handed', 'Simple', 'B', 1],
    ['Heavy Crossbow', 'Ranged', 'Simple', 'P', 1],
    ['Light Crossbow', 'Ranged', 'Simple', 'P', 1],
    ['Darts', 'Thrown', 'Simple', 'P', 0.2],
    ['Javelins', 'Thrown', 'Simple', 'P', 1],
    ['Sling', 'Ranged', 'Simple', 'B', 0.5],
    ['Throwing Axes', 'Thrown', 'Martial', 'S', 0.5],
    ['Handaxe', 'Light', 'Martial', 'S', 1],
    ['Kukri', 'Light', 'Martial', 'P', 0.5],
    ['Shortsword', 'Light', 'Martial', 'P', 1],
    ['Battleaxe', 'One-Handed', 'Martial', 'S', 1],
    ['Flail', 'One-Handed', 'Martial', 'B', 1],
    ['Longsword', 'One-Handed', 'Martial', 'S', 1],
    ['Rapier', 'One-Handed', 'Martial', 'P', 1],
    ['Scimitar', 'One-Handed', 'Martial', 'S', 1],
    ['Trident', 'One-Handed', 'Martial', 'P', 1],
    ['Warhammer', 'One-Handed', 'Martial', 'B', 1],
    ['Falchion', 'Two-Handed', 'Martial', 'S', 1],
    ['Glaive', 'Two-Handed', 'Martial', 'S', 1],
    ['Greataxe', 'Two-Handed', 'Martial', 'S', 1],
    ['Greatsword', 'Two-Handed', 'Martial', 'S', 1],
    ['Greatclub', 'Two-Handed', 'Martial', 'B', 1],
    ['Heavy Flail', 'Two-Handed', 'Martial', 'B', 1],
    ['Halberd', 'Two-Handed', 'Martial', 'S', 1],
    ['Scythe', 'Two-Handed', 'Martial', 'S', 0.5],
    ['Longbow', 'Ranged', 'Martial', 'P', 1],
    ['Shortbow', 'Ranged', 'Martial', 'P', 1],
    ['Sai', 'Light', 'Exotic', 'P', 0.5],
    ['Bastard Sword', 'One-Handed', 'Exotic', 'S', 1],
    ['Dwarven Waraxe', 'One-Handed', 'Exotic', 'S', 1],
    ['Kama', 'Light', 'Exotic', 'S', 0.5],
    ['Nunchaku', 'Light', 'Exotic', 'B', 0.5],
    ['Siangham', 'Light', 'Exotic', 'P', 0.5],
    ['Spiked Chain', 'Two-Handed', 'Exotic', 'P', 0.5],
    ['Whip', 'Two-Handed', 'Exotic', 'S', 0.2],
    ['Orc Double Axe', 'Two-Handed', 'Exotic', 'S', 0.5],
    ['Gnome Hooked Hammer', 'One-Handed', 'Exotic', 'BP', 0.2],
    ['Dire Flail', 'Two-Handed', 'Exotic', 'B', 0.5],
    ['Bolas', 'Thrown', 'Exotic', 'B', 0.2],
    ['Hand Crossbow', 'Ranged', 'Exotic', 'P', 0.5],
    ['Repeating Heavy Crossbow', 'Ranged', 'Exotic', 'P', 0.2],
    ['Repeating Light Crossbow', 'Ranged', 'Exotic', 'P', 0.2],
    ['Net', 'Thrown', 'Exotic', 'B', 0.2],
    ['Shuriken', 'Thrown', 'Exotic', 'P', 0.2],
]

weapon_details = {}
for w in weapons_raw:
    weapon_details[w[0]] = {
        'name': w[0],
        'category' : w[1],
        'proficiency': w[2],
        'damage_type': w[3],
        'frequency': w[4],
        'metal' : False if w[0] in ('Quarterstaff', 'Club', 'Greatclub', 'Net', 'Bolas') or w[1] == 'Ranged' else True,
    }

random_weapon_selector = WeightedChoice(
    [w[0] for w in weapons_raw],
    [w[4] for w in weapons_raw]
)

special_weapon_materials = [
    'Adamantine',
    'Cold Iron',
    'Silver',
]