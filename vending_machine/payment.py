from vending_machine.coins import Coin
from vending_machine.controller import Controller

class CoinPaymentService():
    def __init__(self, ctrl: Controller) -> None:
        self.controller:Controller = ctrl

    def accept(self, coin:Coin) -> None:
        self.controller.approve_amount(coin.value())
        