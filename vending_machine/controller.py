from abc import ABC, abstractmethod

class Controller():
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def approve_amount(self, amount:float) -> None:
        ...

    @property
    @abstractmethod
    def approved_amount(self) -> float:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...


class CentralController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self._amount: float = 0.0

    def approve_amount(self, amount:float) -> None:
        self._amount += amount

    @property
    def approved_amount(self) -> float:
        return self._amount
    
    def clear(self) -> None:
        self._amount = 0.0