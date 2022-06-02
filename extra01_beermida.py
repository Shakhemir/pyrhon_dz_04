"""
Давайте представим, что ваша компания только что наняла вашего друга из колледжа и заплатила вам реферальный бонус.
Потрясающе! Чтобы отпраздновать, вы берете свою команду в очень странный бар по соседству и используете реферальный бонус,
чтобы купить и построить самую большую трехмерную пирамиду из пивных банок, которую вы можете.
Пирамида пивных банок будет квадратировать количество банок на каждом уровне - 1 банка на верхнем уровне,
4 на втором, 9 на следующем, 16, 25...
Определите функцию beeramid, чтобы вернуть количество полных уровней пирамиды пивных банок, которую вы можете сделать,
учитывая параметры: реферальный бонус и цена пивной банки.
Например:
beeramid(1500, 2)# 12
beeramid(5000, 3)# 16
"""

def beeramid(bonus, beer_price):
    level = 0
    while bonus > 0:
        level += 1
        bonus -= beer_price * level ** 2
    return level - 1

print(beeramid(1500, 2))
print(beeramid(5000, 3))