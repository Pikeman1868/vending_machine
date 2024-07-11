from dataclasses import dataclass
from collections import UserList
from typing import List

@dataclass(frozen=True)
class Coin():
    value:float
    name: str
    diameter:float
    weight:float

    # def __eq__(self, value: object) -> bool:
    #     return (value.diameter == self.diameter) and (value.weight == self.weight)

QUARTER = Coin(0.25, "quarter", 0.955, 5.670)
DIME = Coin(0.1, "dime", 0.705, 2.268)
NICKEL = Coin(0.05, "nickel", 0.835, 5.00)
PENNY = Coin(0.01, "penny", 0.750, 2.50)

COIN_VALUE_MAP = {QUARTER: 0.25,
                  DIME: 0.10,
                  NICKEL: 0.05,
                  PENNY: 0.01}

class Coins(UserList):

    def append(self, coin:Coin) -> None:
        if( not isinstance(coin, Coin)):
            raise ValueError("coin is not of type Coin")
        self.data.append(coin)

    def clear(self) -> None:
        self.data.clear()
    
    def __len__(self) -> int:
        return len(self.data)