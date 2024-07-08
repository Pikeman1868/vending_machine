import pytest
from vending_machine.controller import CentralController

class TestCentalController():
    @pytest.fixture
    def controller(self) -> CentralController:
        return CentralController()

    def test_when_accept_payment_amount_added(self, controller: CentralController):
        assert pytest.approx(0.0) == controller.amount
        controller.approve_amount(0.25)
        assert pytest.approx(0.25) == controller.amount
    
    def test_when_cleared_the_amount_resets_to_0(self,  controller: CentralController):
        controller.approve_amount(0.35)
        controller.clear()
        assert pytest.approx(0.0) == controller.amount
    
    def test_when_amount_is_0_display_reads_insert_coin(self,  controller: CentralController):
        assert "Insert Coin" == controller.display

    def test_when_amount_is_greater_than_0_display_reads_amount(self, controller: CentralController):
        controller.approve_amount(0.25)
        assert "$0.25" == controller.display

