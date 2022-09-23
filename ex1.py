class Garrafa:

    def __init__(self, capacidade, volume):
        if capacidade > 0 and capacidade > volume:
            self._capacidade = capacidade
            self._volume = volume
        else:
            raise TypeError("Capacidade não está dentro dos parâmetros")

    def __str__(self):
        return f'Capacidade em ml: {self._capacidade}, Volume: {self._volume}'

    @property
    def returncapacidade(self):
        return self._capacidade

    @property
    def returnvolume(self):
        return self._volume

    def despejar(self, quantidade):
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa. Verifique novamente")
        if (self._volume - quantidade) < 0:
            raise ValueError("Não se pode tirar mais que a quantidade atual do volume")
        elif (self._volume - quantidade) >= self._volume:
            self._volume - quantidade

    def encher(self, quantidade):
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa. Verifique novamente")
        if (self._volume + quantidade) <= self._capacidade:
            self._volume + quantidade
        elif (self._volume + quantidade) >= self._capacidade:
            raise ValueError("A garrafa irá transbordar, quantidade inserida maior que a suportada.")


def main():
    try:
        capacidadeGarrafa = float(input('Qual a capacidade da garrafa? '))
        volumeGarrafa = float(input('Qual o volume da garrafa? '))
        garrafaX = Garrafa(capacidadeGarrafa, volumeGarrafa)
        garrafaX.encher(200)
        garrafaX.despejar(100)
        garrafaX.encher(50)
        garrafaX.despejar(100)
        print(garrafaX)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
