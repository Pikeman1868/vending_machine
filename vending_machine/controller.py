from abc import ABC, abstractmethod

class Controller(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def approve_amount(self, amount:float) -> None:
        ...

    @property
    @abstractmethod
    def amount(self) -> float:
        ...

    @property
    @abstractmethod
    def display(self) -> str:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...


class CentralController(Controller):
    INSERT_COIN_STRING:str = "Insert Coin"
    def __init__(self) -> None:
        super().__init__()
        self._display_format:str = "${:.2f}"
        self._amount: float = 0.0
        self._display: str = self.INSERT_COIN_STRING

    def approve_amount(self, amount:float) -> None:
        self._amount += amount
        self._display = self._display_format.format(self.amount)

    @property
    def amount(self) -> float:
        return self._amount
    
    @property
    def display(self) -> str:
        return self._display
    
    def clear(self) -> None:
        self._amount = 0.0
        self._display = self.INSERT_COIN_STRING