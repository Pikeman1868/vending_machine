from vending_machine.coins import Coin, Coins, PENNY, QUARTER, get_value_of_coin
from vending_machine.controller import Controller

class CoinPaymentService():
    def __init__(self) -> None:
        self.controller:Controller
        self._coin_return: Coins = Coins()

    def accept(self, coin:Coin) -> None:
        if not self._is_valid_coin(coin):
            self._coin_return.append(coin)
        else:
            self.controller.approve_amount(get_value_of_coin(coin))

    def _is_valid_coin(self, coin:Coin) -> bool:
        return coin != PENNY

    @property
    def coin_return(self) -> Coin:
        change = self._coin_return.copy()
        self._coin_return.clear()
        return change

    
        