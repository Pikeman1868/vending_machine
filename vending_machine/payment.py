from vending_machine.coins import Coin, Coins, Penny
from vending_machine.controller import Controller

class CoinPaymentService():
    def __init__(self) -> None:
        self.controller:Controller
        self._coin_return: Coins = Coins()

    def accept(self, coin:Coin) -> None:
        if(isinstance(coin, Penny)):
            self._coin_return.append(coin)
        else:
            self.controller.approve_amount(coin.value())

    @property
    def coin_return(self) -> Coin:
        change = self._coin_return.copy()
        self._coin_return.clear()
        return change

    
        