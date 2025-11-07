class Cashier:
    def __init__(self, coins: list[int] | dict[int:int] ) -> None:
        if type(coins) == list:
            self.avaliable_coins: dict[int:int] = dict.fromkeys(sorted(coins, reverse = True), float('inf'))
            return
        self.avaliable_coins: dict[int:int] = dict(sorted(coins.items(), reverse = True))

    def __str__(self) -> str:
        return f"Cashier({self.avaliable_coins})"
    
    def add_coin(self, coin: int) -> None:
        if coin in self.avaliable_coins:
            self.avaliable_coins[coin] += 1

    def remove_coin(self, coin: int) -> int:
        quantity: int = 0
        if coin in self.avaliable_coins and self.avaliable_coins[coin]:
            quantity = self.avaliable_coins[coin]
            self.avaliable_coins[coin] -= 1
        return quantity
    
    def get_quantity(self, coin: int) -> int:
        quantity: int = 0
        if coin in self.avaliable_coins and self.avaliable_coins[coin]:
            quantity = self.avaliable_coins[coin]
        return quantity
    
    def get_change_greedy(self, value: int, max_coins: int = float('inf')) -> dict[int:int]:
        result: dict[int:int] = self._get_zero_coins()
        avaliable_coins: dict[int:int] = self.avaliable_coins.copy()
        for coin in avaliable_coins:
            while value - coin >= 0 and avaliable_coins[coin] and max_coins >= 0:
                value -= coin
                result[coin] += 1
                avaliable_coins[coin] -= 1
                max_coins -= 1
        return result
    
    def get_change_bruteforce():
        pass

    def get_change_dinamic():
        pass
    
    def get_change_value_possible(self, value: int, max_coins: int = float('inf')) -> int:
        change: dict[int:int] = self.get_change_greedy(value, max_coins)
        result: int = 0
        for coin in change:
            result += change[coin] * coin
        return result

    def get_change_quantity_coins(self, value: int, max_coins: int = float('inf')) -> int:
        change: dict[int:int] = self.get_change_greedy(value, max_coins)
        result: int = 0
        for coin in change:
            result += change[coin] 
        return result

    def _get_zero_coins(self) -> dict[int:int]:
        result: dict[int:int] = {}
        for coin in self.avaliable_coins:
            result[coin] = 0
        return result


if __name__ == "__main__":
    my_coins: dict[int:int] = {
        100: 1,
        50: 2,
        20: 3,
        10: 4,
        5: 5,
        2: 6,
        1: 7 }
    
    my_coins2: list[int] = [80, 70, 50]
    
    C: Cashier = Cashier(my_coins2)
    # print(C)
    # print(C._get_zero_coins())
    # print(C.change_quantity_coins(200))
    print(C.get_change_greedy(200))
    print(C.get_change_value_possible(200), "/", 200)
    print(C.get_change_quantity_coins(200))
