from random import randint
from itertools import cycle


class HumanPlayer:
    name = 'Gracz'
    def makemove(self, remaining):
        while True:
            value = input('Podaj liczbe 1-5: ')
            try:
                step = int(value)
            except ValueError:
                print('Podana wartość nie jest liczbą')
                continue
            if step>0 and step <=5:
                return step
            else:
                print('Podano nieprawidłową liczbę ')

class CommPlayer:
    name = 'VEGA'
    def makemove(self, remaining):
        value=randint(1,5)
        return value

class PlayGame:
    def __init__(self,p1,p2):
        self.gracze =(p1, p2)
        self.point = 36

    def doit(self):
        for player in cycle(self.gracze):

            wynik=player.makemove(self.point)
            print('Rusza {}, krok = {}'.format(player.name, wynik))
            self.point= self.point - wynik
            print('Do konca zostalo punktow ' + str(self.point))
            if self.point <= 0:
                print('Wygrał '+player.name)
                break


p1=HumanPlayer()
p2=CommPlayer()
g=PlayGame(p1,p2)
g.doit()
