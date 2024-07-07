from abc import ABC, abstractmethod
from collections import UserList
from typing import List

class Coin(ABC):
    @abstractmethod
    def value(self) -> float:
        ...
    @abstractmethod
    def name(self) -> str:
        ...

class Quarter(Coin):
    def value(self) -> float:
        return 0.25
    
    def name(self) -> str:
        return "quarter"
    
class Dime(Coin):
    def value(self) -> float:
        return 0.10
    def name(self) -> str:
        return "dime"
    
class Nickel(Coin):
    def value(self) -> float:
        return 0.05
    def name(self) -> str:
        return "nickel"

class Penny(Coin):
    def value(self) -> float:
        return 0.01
    def name(self) -> str:
        return "penny"

class Coins(UserList):

    def append(self, coin:Coin) -> None:
        if( not isinstance(coin, Coin)):
            raise ValueError("coin is not of type Coin")
        self.data.append(coin)

    def clear(self) -> None:
        self.data.clear()
    
    def __len__(self) -> int:
        return len(self.data)