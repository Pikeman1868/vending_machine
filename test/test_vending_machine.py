import pytest
from vending_machine import coins
from vending_machine.vending_machine import VendingMachine, VendingMachineBuilder


class TestVendingMachine():

    @pytest.fixture()
    def vm(self) -> VendingMachine:
        return VendingMachineBuilder().build()

    def test_when_awaiting_money_display_reads_insert_coin(self, vm:VendingMachine):
        assert vm.read_display() == "Insert Coin"

    def test_when_receives_money_display_reports_money(self, vm:VendingMachine):
        assert vm.read_display() == "Insert Coin"
        vm.insert_coin(coins.QUARTER)
        assert vm.read_display() == "$0.25"

    def test_when_penny_insert_place_in_coin_return(self, vm:VendingMachine):
        vm.insert_coin(coins.PENNY)
        assert len(vm.check_coin_return()) == 1

    def test_change_return_empty_when_valid_coin_is_inserted(self, vm: VendingMachine):
        vm.insert_coin(coins.QUARTER)
        assert len(vm.check_coin_return()) == 0