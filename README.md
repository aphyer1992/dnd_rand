# D&D Character Generator

A Python-based Dungeons & Dragons character generator that uses a weighted choice system for random character creation.

## Features

- **WeightedChoice System**: Flexible random selection with customizable probabilities
- **Character Generation**: Random stats, classes, races, and special features
- **Interactive Character Building**: Swap stats and modify requirements
- **Extensive D&D Content**: Support for rare classes, races, and creature types
- **Bonus/Penalty System**: Random character quirks and abilities

## Files

- `chargen.py` - Main character generator with interactive interface
- `weighted_choice.py` - Core WeightedChoice class for probability-based selection
- `config_lists.py` - D&D data lists (classes, races, domains, etc.)

## Usage

Run the character generator:

```bash
python chargen.py
```

The generator will create random characters and allow you to:
- Swap ability scores
- Remove class requirements (with consequences)
- Generate random bonuses and penalties

## WeightedChoice System

The WeightedChoice class allows for sophisticated random selection:

```python
from weighted_choice import WeightedChoice

# Simple weighted selection
selector = WeightedChoice([
    "Common item",
    "Rare item", 
    "Legendary item"
], weights=[70, 25, 5])

# Nested selections with functions
complex_selector = WeightedChoice([
    "Basic option",
    lambda: some_complex_function(),
    other_weighted_choice_object
])

result = selector.choose()
```

## Requirements

- Python 3.6+
- No external dependencies

## License

This project is open source and available under the MIT License.
