from . coins import Coin, Coins, Penny

class VendingMachine():
    INSTER_COIN_STRING:str = "Insert Coin"
    def __init__(self) -> None:
        self._coins_inserted:list[Coin] = []
        self._display_format:str = "${:.2f}"
        self._display_string:str = self.INSTER_COIN_STRING
        self._coin_return: Coins = Coins()

    def read_display(self) -> str:
        return self._display_string
    
    def insert_coin(self, coin: Coin) -> None:
        if(isinstance(coin, Penny)):
            self._coin_return.append(coin)
        else:
            self._coins_inserted.append(coin)
            value = 0
            for n in self._coins_inserted:
                value += n.value()
            self._display_string = self._display_format.format(value)
        
    
    def check_coin_return(self) -> Coins:
        change = self._coin_return.copy()
        self._coin_return.clear()
        return change