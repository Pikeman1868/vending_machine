import pytest
from vending_machine import coins

class TestQuarter():
    @pytest.fixture()
    def quarter(self):
        return coins.Quarter()
    def test_quarter_value_is_25_cents(self, quarter: coins.Quarter):
        assert pytest.approx(0.25) == quarter.value()
    
    def test_quarter_name_is_quarter(self, quarter: coins.Quarter):
        assert quarter.name() == "quarter"

class TestDime():
    @pytest.fixture()
    def dime(self):
        return coins.Dime()
    def test_dime_vaule_is_10_cents(self, dime: coins.Dime):
        assert pytest.approx(0.10) == dime.value()

    def test_dime_name_is_dime(self, dime:coins.Coin):
        assert dime.name() == dime.name()
