from vending_machine.coins import QUARTER, PENNY
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
        service.accept(QUARTER)
        assert pytest.approx(0.25) == service.controller.amount

    def test_penny_does_not_update_amount(self, service: CoinPaymentService):
        service.accept(PENNY)
        assert pytest.approx(0.0) == service.controller.amount

    def test_penny_is_placed_in_coin_return(self, service: CoinPaymentService):
        service.accept(PENNY)
        assert len(service.coin_return) == 1
    
    def test_when_given_quarter_return_true(self, service: CoinPaymentService):
        assert service.is_quarter(QUARTER)

    
