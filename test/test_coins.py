import pytest
from vending_machine.coins import *

class TestQuarter():
    @pytest.fixture()
    def quarter(self):
        return Quarter()
    def test_quarter_value_is_25_cents(self, quarter: Quarter):
        assert pytest.approx(0.25) == quarter.value()
    
    def test_quarter_name_is_quarter(self, quarter: Quarter):
        assert quarter.name() == "quarter"

class TestDime():
    @pytest.fixture()
    def dime(self):
        return Dime()
    def test_dime_value_is_10_cents(self, dime: Dime):
        assert pytest.approx(0.10) == dime.value()

    def test_dime_name_is_dime(self, dime:Coin):
        assert dime.name() == "dime"

class TestNickel():
    @pytest.fixture()
    def nickel(self) -> Nickel:
        return Nickel()
    def test_nickel_value_is_5_cents(self, nickel:Nickel):
        assert pytest.approx(0.05) == nickel.value()

    def test_nickel_name_is_nickel(self, nickel:Nickel):
        assert nickel.name() == "nickel"

class TestPenny():
    @pytest.fixture()
    def penny(self) -> Penny:
        return Penny()
    def test_penny_value_is_5_cents(self, penny:Penny):
        assert pytest.approx(0.01) == penny.value()

    def test_penny_name_is_penny(self, penny:Penny):
        assert penny.name() == "penny"

class TestCoins():
    @pytest.fixture
    def coins(self) -> Coins:
        return Coins()
    
    def test_can_add_coins_to_coins(self, coins:Coins):
        coins.append(Quarter())
        assert len(coins) == 1
    
    def test_coins_raises_error_if_not_coin_appended(self, coins: Coins):
        with pytest.raises(ValueError):
            coins.append("coin")

    def test_empty_removes_all_coins(self, coins:Coins):
        coins.append(Quarter())
        coins.append(Dime())
        coins.clear()
        assert len(coins) == 0

    def test_can_copy_coins(self, coins:Coins):
        coins.append(Quarter())
        coins.append(Dime())
        actual = coins.copy()
        assert len(actual) == len(coins)
        
