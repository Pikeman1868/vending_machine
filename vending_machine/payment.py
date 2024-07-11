from vending_machine.coins import Coin, Coins, PENNY, QUARTER
from vending_machine.controller import Controller

class CoinPaymentService():
    def __init__(self) -> None:
        self.controller:Controller
        self._coin_return: Coins = Coins()

    def accept(self, coin:Coin) -> None:
        if(coin == PENNY):
            self._coin_return.append(coin)
        else:
            self.controller.approve_amount(coin.value)

    def is_quarter(self, coin:Coin) -> bool:
        qrt = QUARTER
        return (coin.diameter == qrt.diameter) or (coin.weight == qrt.weight)

    @property
    def coin_return(self) -> Coin:
        change = self._coin_return.copy()
        self._coin_return.clear()
        return change

    
        