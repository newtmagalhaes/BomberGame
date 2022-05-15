from django.db import models

# Create your models here.
class Coordinates(models.Model):
    """Coordenadas do Campo
    =======================
    Coordenadas no campo minado 5x5.
    Posições válidas aprensentam índices (`x`, `y`) dentro do intervalo [1, 5].
    """
    # Constante
    POSICOES_VALIDAS = tuple(('{:02d}'.format(i), f'({i%5},{i//5})') for i in range(25))
    position = models.IntegerField(choices=POSICOES_VALIDAS)

    @property
    def x(self) -> int:
        return int(self.position.name) % 5


    @property
    def y(self) -> int:
        return int(self.position.name) // 5


    def __str__(self) -> str:
        return self.position.value


class Game(models.Model):
    """Bomber Game
    ==============
    Objeto contendo o setup das bombas no tabuleiro em sua data de criação.
    
    TODO
    ----
    - idealiza-se que exista apenas 1 objeto por dia no database;
        - bloquear outras tentativas de criação no mesmo dia;
        - criar uma caso não exista a do respectivo dia
    - Cada objeto deve conter:
        - data de criação;
        - posição das 3 bombas;
        - semente com número aleatório (baseado na data) para ser usada no
        sorteio das posições das bombas; (garantindo reprodutibilidade)
    """
    date = models.DateField()
    # bombs = models.CharField()

    def __str__(self) -> str:
        return f'Jogo do dia {self.date}'
