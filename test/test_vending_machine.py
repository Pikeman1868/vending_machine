from vending_machine import coins
from vending_machine.vending_machine import VendingMachine


def test_when_receives_money_display_reports_money():
    vm = VendingMachine()
    assert vm.read_display() == "$0.00"
    vm.insert_coin(coins.Quarter())
    assert vm.read_display() == "$0.25"