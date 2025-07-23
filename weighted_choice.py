import random

# WeightedChoice: Enhanced implementation for complex random selections
class WeightedChoice:
    def __init__(self, items, weights=None):
        """
        Create a weighted random selector.
        
        Args:
            items: list of values or callables
            weights: optional list of weights (defaults to equal weights)
        """
        if not items:
            raise ValueError("Items list cannot be empty")
        
        self.items = items
        self.weights = weights or [1] * len(items)
        
        if len(self.items) != len(self.weights):
            raise ValueError("Items and weights must have the same length")
        
        if any(w < 0 for w in self.weights):
            raise ValueError("Weights must be non-negative")
    
    def choose(self, params=None):
        """Select random item with weights, calling if it's a function."""
        result = random.choices(self.items, weights=self.weights, k=1)[0]
        return result(params) if callable(result) else result
    
    def add_item(self, item, weight=1):
        """Add a new item with optional weight."""
        self.items.append(item)
        self.weights.append(weight)
    
    def remove_item(self, item):
        """Remove an item and its corresponding weight."""
        try:
            index = self.items.index(item)
            self.items.pop(index)
            self.weights.pop(index)
        except ValueError:
            raise ValueError(f"Item {item} not found in selector")
    
    def set_weight(self, item, weight):
        """Change the weight of an existing item."""
        try:
            index = self.items.index(item)
            self.weights[index] = weight
        except ValueError:
            raise ValueError(f"Item {item} not found in selector")
    
    def get_probability(self, item):
        """Get the probability of selecting a specific item."""
        try:
            index = self.items.index(item)
            total_weight = sum(self.weights)
            return self.weights[index] / total_weight if total_weight > 0 else 0
        except ValueError:
            raise ValueError(f"Item {item} not found in selector")
    
    def __len__(self):
        """Return number of items."""
        return len(self.items)
    
    def __repr__(self):
        """String representation showing items and their weights."""
        return f"WeightedChoice({list(zip(self.items, self.weights))})"