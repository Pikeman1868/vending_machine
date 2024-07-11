import pytest
from vending_machine.coins import * # NOSONAR Unit Under Test

class TestQuarter():
    def test_quarter_value_is_25_cents(self):
        assert pytest.approx(0.25) == QUARTER.value
    
    def test_quarter_name_is_quarter(self):
        assert QUARTER.name == "quarter"

    def test_quarter_diameter_is_0_955_in(self):
        assert QUARTER.diameter == pytest.approx(0.955)

    def test_quarter_weight_is_5_67_grams(self):
        assert QUARTER.weight == pytest.approx(5.67)
    
    def test_dime_is_not_equal_to_quarter(self):
        assert QUARTER != DIME

    def test_nickel_is_not_equal_to_quarter(self):
        assert QUARTER != NICKEL

    def test_penny_is_not_equal_to_quarter(self):
        assert QUARTER != PENNY

    def test_quarter_is_equal_to_quarter(self):
        assert QUARTER == Coin(0.25, "quarter", 0.955, 5.670)

class TestDime():

    def test_dime_value_is_10_cents(self):
        assert pytest.approx(0.10) == DIME.value

    def test_dime_name_is_dime(self):
        assert DIME.name == "dime"

    def test_dime_diameter_is_0705_in(self):
        assert DIME.diameter == pytest.approx(0.705)

    def test_dime_weight_is_2_268_grams(self):
        assert DIME.weight == pytest.approx(2.268)

    def test_dime_is_not_equal_to_quarter(self):
        assert DIME != QUARTER

    def test_dime_is_not_equal_to_nickel(self):
        assert DIME != NICKEL

    def test_dime_is_not_equal_to_penny(self):
        assert DIME != PENNY

    def test_dime_is_equal_to_dime(self):
        assert DIME == Coin(0.1, "dime", 0.705, 2.268)

class TestNickel():
    def test_nickel_value_is_5_cents(self):
        assert pytest.approx(0.05) == NICKEL.value

    def test_nickel_name_is_nickel(self):
        assert NICKEL.name == "nickel"

    def test_nickel_diameter_is_0_835_inches(self):
        assert NICKEL.diameter == pytest.approx(0.835)

    def test_nickel_weight_is_5_00_inches(self):
        assert NICKEL.weight == pytest.approx(5.00)

    def test_nickel_is_not_equal_to_quarter(self):
        assert NICKEL != QUARTER

    def test_nickel_is_equal_to_nickel(self):
        assert NICKEL == Coin(0.05, "nickel", 0.835, 5.00)

    def test_nickel_is_not_equal_to_penny(self):
        assert NICKEL != PENNY

    def test_nickel_is_not_equal_to_dime(self):
        assert NICKEL != DIME

class TestPenny():

    def test_penny_value_is_5_cents(self):
        assert pytest.approx(0.01) == PENNY.value

    def test_penny_name_is_penny(self):
        assert PENNY.name == "penny"

    def test_penny_diameter_is_0_750_inches(self):
        assert PENNY.diameter == pytest.approx(0.750)

    def test_penny_weight_is_2_50_grams(self):
        assert PENNY.weight == pytest.approx(2.50)

    def test_penny_is_not_equal_to_quarter(self):
        assert PENNY != QUARTER

    def test_penny_is_equal_to_penny(self):
        assert PENNY == Coin(0.01, "penny", 0.750, 2.50)

    def test_penny_is_not_equal_to_nickel(self):
        assert PENNY != NICKEL

    def test_penny_is_not_equal_to_dime(self):
        assert PENNY != DIME

class TestCoinValueMap():
    @pytest.mark.parametrize("input, expected", [(QUARTER, 0.25), (DIME, 0.1), (NICKEL, 0.05), (PENNY, 0.01)])
    def test_coin_has_correct_value(self, input:Coin, expected:float):
        assert get_value_of_coin(input) == pytest.approx(expected)

class TestCoins():
    @pytest.fixture
    def coins(self) -> Coins:
        return Coins()
    
    def test_can_add_coins_to_coins(self, coins:Coins):
        coins.append(QUARTER)
        assert len(coins) == 1
    
    def test_coins_raises_error_if_not_coin_appended(self, coins: Coins):
        with pytest.raises(ValueError):
            coins.append("coin")

    def test_empty_removes_all_coins(self, coins:Coins):
        coins.append(QUARTER)
        coins.append(DIME)
        coins.clear()
        assert len(coins) == 0

    def test_can_copy_coins(self, coins:Coins):
        coins.append(QUARTER)
        coins.append(DIME)
        actual = coins.copy()
        assert len(actual) == len(coins)
        
