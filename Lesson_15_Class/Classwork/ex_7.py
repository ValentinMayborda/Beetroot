class Coins:

    def __init__(self, total_sum: int):
        self._coins = (1, 2, 5, 10, 25, 50)  # приватний атрибут
        self.total_sum = total_sum

    def change(self) -> dict:
        result = {}
        remaining = self.total_sum
        for coin in sorted(self._coins, reverse=True):
            result[coin] = remaining // coin
            remaining %= coin
        return result

    def format_result(self) -> str:
        coins = self.change()
        lines = [f'Сума: {self.total_sum}']
        for coin, count in sorted(coins.items(), reverse=True):
            if count > 0:
                lines.append(f'  {coin:3} грн x {count}')
        return '\n'.join(lines)


c = Coins(185)
print(c.change())
# {50: 3, 25: 1, 10: 1, 5: 0, 2: 0, 1: 0}

print(c.format_result())
# Сума: 185
#  50 коп x 3
#  25 коп x 1
#  10 коп x 1

