class livro:
    def__init__(self, codigo:int, titulo : str ,  preco: flot, tipo : int, desconto_percentual: flot= 0):
        if preco < 0:
            raiser ValueError(" O preço não pode ser  negativo.")
        if desconto_percentual < 0 or desconto_percentual > 100:
            raiser ValueError ("O desconto deve ser entr 0 e 100.")
        if tipo not in [1,2]:
            raiser ValueError ("tipo inválido. Use 1 para gratuito e 2 para pago ")
        
        self.codigo = codigo
        self.titulo
        self.preco
        self.tipo
        self.desconto_percentual

    def preco_final(self) -> flot:
        if self.tipo == 1:
            return 0.0
        desconto= self.preco * (self.desconto_percentual/100)
        return round(self.preco -  desconto, 2)