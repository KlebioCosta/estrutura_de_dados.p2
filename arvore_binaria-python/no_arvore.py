    #classe que receberá os nós da árvore
class TNode:
    #metodo de inicialização para receber os dados
    #'left' e 'right' direciona o lado certo a ser
    # inserido o valor.
    #
    def __init__(self, dado):
        self.dado = dado
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.dado)