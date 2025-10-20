class Item:
    def __init__(self):
        self.weigth
        self.value
        self.quantity

    def get_density(self):
        return self.value / self.weigth


class Backpack:
    def __init__(self):
        self.items: dict[int:Item] = dict()
        self.max_id: int = 0
        pass

    def __str__(self) -> str:
        result: str = f"# ITEMS IN BACKPACK #"
        for id in self.items:
            item = self.items[id]
            result += str(f"\Item {id:>03} | Mass: {item.mass} | Value: {item.value} | Density: {item.get_density()}")
        return result
    
    def size(self) -> int:
        return len(self.dict)

    def is_empty(self) -> bool:
        return self.size() == 0

    def add_item(self, mass: int, value: int, id: int = -1) -> int:
        if value < 0 or mass < 0:
            raise Exception(f"The value and the mass cannot be negative")
    
        if id == -1 or id in self.items: 
            self.max_id += 1
            id = self.max_id

        self.items[id] = Item(mass=mass, value=value)
        return id
    
    def pop_item(self, id) -> tuple[int, int]:
        item: Item = self.items.pop(id)
        return (item.mass, item.value)
    

    def fractionate_backpack(self, max_weight: int):
        for item_id in self.items:
            item: Item = self.items[item_id]
            x1 = 0
            density = item.get_density()
            total_weigth = 0

            while total_weigth < max_weight:
                a = min(w1, max_weight - total_weigth)
                x1 = a
                w += a

        
        return 0

# Algorithm FractionalKnapsack(S, W):
# Input: Set S of items, such that each item i ∈ S has a positive benefit bi and a
# positive weight wi; positive maximum total weight W
# Output: Amount xi of each item i ∈ S that maximizes the total benefit while
# not exceeding the maximum total weight W
# for each item i ∈ S do
# xi ← 0
# vi ← bi/wi // value index of item i
# w ← 0 // total weight
# while w<W and S 	= ∅ do
# remove from S an item i with highest value index // greedy choice
# a ← min{wi, W − w} // more than W − w causes a weight overflow
# xi ← a
# w ← w + a







