import pytest
from vending_machine.controller import CentralController

class TestVendingMachineController():
    def test_when_accept_payment_amount_added(self):
        controller = CentralController()
        assert pytest.approx(0.0) == controller.approved_amount
        controller.approve_amount(0.25)
        assert pytest.approx(0.25) == controller.approved_amount
    
    def test_when_cleared_the_amount_resets_to_0(self):
        controller = CentralController()
        controller.approve_amount(0.35)
        controller.clear()
        assert pytest.approx(0.0) == controller.approved_amount
