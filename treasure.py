import random
from weighted_choice import WeightedChoice
from config_lists import random_weapon_selector, magic_schools, domains, energy_types, creature_types, animal_companions, weapon_details, special_weapon_materials

minor_specific_weapon_gen = WeightedChoice([
    'Sleep Arrow',
    'Screaming Bolt',
    'Javelin of Lightning',
    'Slaying Arrow',
    lambda weapon: None if weapon_details[weapon]['metal'] == False else 'Masterwork ' + random.choice(special_weapon_materials) + ' ' + weapon,
], [1, 1, 1, 1, 10])

minor_magic_weapon_enchantment_gen = WeightedChoice([
    lambda weapon: random.choice(creature_types) + ' Bane',
    'Defending', 'Flaming', 'Frost', 'Shock', 'Ghost Touch',
    lambda weapon: None if weapon_details[weapon]['damage_type'] == 'B' else 'Keen',
    'Ki Focus', 'Merciful', 'Mighty Cleaving', 'Spell Storing', 'Throwing', 'Thundering', 'Vicious',
    lambda weapon: minor_magic_weapon_enchantment_gen.choose(weapon) + ', ' + minor_magic_weapon_enchantment_gen.choose(weapon),
], [10, 7, 10, 10, 10, 9, 11, 4, 4, 7, 5, 4, 4, 4, 1])

minor_magic_weapon_gen = WeightedChoice([
    lambda weapon: "+1 " + weapon,
    lambda weapon: "+2 " + weapon,
    lambda weapon: minor_specific_weapon_gen.choose(weapon),
    lambda weapon: minor_magic_weapon_gen.choose(weapon) + ", " + minor_magic_weapon_enchantment_gen.choose(weapon),
], [70, 15, 5, 10])

minor_magic_armor_gen=None
minor_magic_ring_gen=None
minor_magic_scroll_gen=None
minor_magic_wand_gen=None
minor_magic_potion_gen=None
minor_magic_wondrous_gen=None
minor_magic_item_gen = WeightedChoice([
    lambda weapon: minor_magic_weapon_gen(random_weapon_selector.choose()).choose(),
    minor_magic_armor_gen,
    minor_magic_potion_gen,
    minor_magic_ring_gen,
    minor_magic_scroll_gen,
    minor_magic_wand_gen,
    minor_magic_wondrous_gen,
], [4, 5, 35, 2, 35, 10, 9])

for i in range(10):
    print(minor_magic_weapon_gen.choose(random_weapon_selector.choose()))