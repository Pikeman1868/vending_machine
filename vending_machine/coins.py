from abc import ABC, abstractmethod

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
        return ""