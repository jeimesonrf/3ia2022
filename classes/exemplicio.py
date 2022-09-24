class ContaDeLuz():

    data_leitura = ''
    numero_leitura = 0
    leitura_atual = 0
    leitura_anterior = 0
    consumo_mensal = 0
    valor = 0.0
    data_pgto = ''
    media_diaria = 0.0

    def __init__(self,data, numero, anterior, atual):
        self.data_leitura = data
        self.numero_leitura = numero
        self.leitura_anterior = anterior
        self.leitura_atual = atual
        self.calcular_consumo()
        self.calcular_media()
        self.calcular_valor()
    
    def calcular_consumo(self):
        self.consumo_mensal = self.leitura_atual - self.leitura_anterior

    def calcular_valor(self):
        self.valor = self.consumo_mensal * 0.78797

    def calcular_media(self):
        self.media_diaria = self.consumo_mensal / 30
    
    def verificar_debito(self):
        if (self.data_pgto == '') or (self.data_pgto == None):
            return True
        else:
            return False
    
    def __str__(self) -> str:
        return f'Data da leitura:    {self.data_leitura}\nNúmero da leitura:  {self.numero_leitura}\nLeitura anterior:   {self.leitura_anterior}\nLeitura atual:      {self.leitura_atual}\nConsumo (KWh):      {self.consumo_mensal}\nMédia diária(KWh):  {self.media_diaria:.2f}\nValor (em reais):   {self.valor:.2f}'

    def exibirConta(self):
        print(self)


if __name__ == '__main__':
    conta = ContaDeLuz('12/08/22','00001',10,102)
    print(conta.valor)
    print(conta)