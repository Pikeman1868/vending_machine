from vending_machine import vending_machine, coins

def test_accept_coins():
    vm = vending_machine.VendingMachineBuilder().build()
    assert vm.read_display() == "Insert Coin"
    quarter = coins.Quarter()
    vm.insert_coin(quarter)
    assert vm.read_display() == "$0.25"
    dime = coins.Dime()
    vm.insert_coin(dime)
    assert vm.read_display() == "$0.35"
    nickel = coins.Nickel()
    vm.insert_coin(nickel)
    assert vm.read_display() == "$0.40"
    penny = coins.Penny()
    vm.insert_coin(penny)
    assert vm.read_display() == "$0.40"
    assert len(vm.check_coin_return()) == 1

