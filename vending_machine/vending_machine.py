from . coins import Coin

class VendingMachine():
    def __init__(self) -> None:
        self._coins_inserted:list[Coin] = []
        self._display_format:str = "${:.2f}"

    def read_display(self) -> str:
        value = 0
        for n in self._coins_inserted:
            value += n.value()
        return self._display_format.format(value)
    
    def insert_coin(self, coin: Coin) -> None:
        self._coins_inserted.append(coin)