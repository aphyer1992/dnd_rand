from weighted_choice import WeightedChoice

minor_magic_item_gen = WeightedChoice([
    minor_magic_weapon_gen,
    minor_magic_armor_gen,
    minor_magic_potion_gen,
    minor_magic_ring_gen,
    minor_magic_scroll_gen,
    minor_magic_wand_gen,
    minor_magic_wondrous_gen,
], [4, 5, 35, 2, 35, 10, 9]