from __future__ import annotations
from . coins import Coin, Coins, Penny
from . controller import Controller, CentralController 
from . payment import CoinPaymentService


class VendingMachineBuilder():
    def __init__(self) -> None:
        self.controller = CentralController()
        self.payment_service = CoinPaymentService()
    
    def build(self) -> VendingMachine:
        return VendingMachine(self)


class VendingMachine():
    def __init__(self, builder: VendingMachineBuilder) -> None:
        self._controller: Controller = builder.controller
        self._payment = builder.payment_service
        self._payment.controller = builder.controller
    
    def read_display(self) -> str:
        return self._controller.display
    
    def insert_coin(self, coin: Coin) -> None:
        self._payment.accept(coin)
        
    def check_coin_return(self) -> Coins:
        return self._payment.coin_return