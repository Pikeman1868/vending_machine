from vending_machine.coins import Quarter, Penny
from vending_machine.payment import CoinPaymentService
from vending_machine.controller import CentralController
import pytest


class TestCoinPaymentServie():
    
    @pytest.fixture
    def service(self) -> CoinPaymentService:
        service = CoinPaymentService()
        service.controller = CentralController()
        return  service

    def test_accept_coin(self, service: CoinPaymentService):
        service.accept(Quarter())
        assert pytest.approx(0.25) == service.controller.amount

    def test_penny_does_not_update_amount(self, service: CoinPaymentService):
        service.accept(Penny())
        assert pytest.approx(0.0) == service.controller.amount

    def test_penny_is_placed_in_coin_return(self, service: CoinPaymentService):
        service.accept(Penny())
        assert len(service.coin_return) == 1
