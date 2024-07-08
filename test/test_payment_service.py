from vending_machine.coins import Quarter
from vending_machine.payment import CoinPaymentService
from vending_machine.controller import CentralController
import pytest


class TestCoinPaymentServie():
    def test_accept_coin(self):
        controller = CentralController()
        service = CoinPaymentService(controller)
        service.accept(Quarter())
        assert pytest.approx(0.25) == controller.approved_amount