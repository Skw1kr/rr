import random
from random import randint

colors = ["Черный", "Красный", "Зеленый"]
types = [1, 2]
balance = 500.234

#тут в тупую прошу и сразу принимаю эти данные в класс
class Player:
    def place_bet(self):
        self.name = str(input("Введи имя:    "))
        self.color = str(input("Введи цвет:   "))
        self.amount = int(input("Введи число от 0 до 36:    "))
        self.bet_type = int(input("Введите четность(1) или нечетность(2):   "))

#в спине рандомно подбираю выпавшее число цвет и не/четность
class Roulette:
    def spin(self):
        self.amount1 = randint(0, 36)
        self.color1 = random.choice(colors)
        self.bet_type1 = random.choice(types)
#тут проверяю что ввел чел и что выпало и в зависимости от этого вывожу
    def resolve_bet(self, player, balance):
        print("На рулетке:  ", self.color1, "   ", self.amount1, "   ", self.bet_type1)
        if player.color == self.color1 and player.amount == self.amount1 and player.bet_type == self.bet_type1:
            balance *=2;
            print("Ты победил, твой баланс :  ",  balance)
        else:
            balance*=0;
            print("гг, баланс :  ", balance)

        return balance

#методы прогоняю
player = Player()
player.place_bet()

roulette = Roulette()
roulette.spin()

#обновил баланс
balance = roulette.resolve_bet(player, balance)

#общий коммент
#я просто с наследованиями и т.д работал в плюсах(С++), тут примерно по той же схеме действовал. тут как такового наследования нет, но сама структура этих классов и т.д. поэтому по памяти из лаб в унике все воссоздавал.