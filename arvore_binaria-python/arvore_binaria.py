#EQUIPE:
#  EDINAILTON KLÉBIO DA COSTA FERREIRA
#  FÁBIO VALERIO RIQUE ROCHA FILHO
#  GONÇALO GABRIEL DE HOLANDA SANTOS
#  JEIMISON GUIMARÃES DE ALBUQUERQUE
#  SÉRGIO FERNANDES DIAS DOS SANTOS FILHO

from no_arvore import TNode


class ArvoreBinaria:

    def __init__(self, dado=None):
                #caso ja tenha algum elemento em dado
                # ele será a raiz
        if dado:
                #criando primeiro nó, onde
                # será a raiz
            node = TNode(dado)
                #define que a raiz será o nó criado à cima
            self.root = node
        else:
            self.root = None

                #o percurso que será feito pelos nós de
                # modo simetrico
    def percurso_simetrico(self, node=None):
                #o nó sendo vazio entao o primeiro valor
                # será a raiz
        if node is None:
            node = self.root
                #será exibido primeiro o lado esquerdo
        if node.left:
            self.percurso_simetrico(node.left)
                #será exibido o nó e logo depois o do lado
                #direito
        print(node, end='')
                #após ser inserido o lado esquerdo,e nao tiver mais 
                # ramificaçoes será entao imprimido o nó e o lado direto.
                #seguindo o mesmo fluxo ate o fim da árvore.

        if node.right:
            self.percurso_simetrico(node.right)



if __name__ == "__main__":
        #os dados a ser inseridos a árvore
    tree = ArvoreBinaria()

    n1 = TNode("T")
    n2 = TNode("R")
    n3 = TNode("B")
    n4 = TNode("E")
    n5 = TNode("R")
    n6 = TNode("N")
    n7 = TNode("I")
    n8 = TNode("A")
    n9 = TNode("Y")
    n10 = TNode("E")
    n11 = TNode(" ")
        #colocando os dados na ordem específica
    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n4.left = n10
    n4.right = n11
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
        #construão da árvore
    tree.percurso_simetrico()


#CAMINHO PERCORRIDO PELA ÁRVORE
#           'R'
#          /   \
#        'T'   'B'
#             /   \
#            /     \
#          'E'     'R'
#         /  \     / \
#       'E' ('')  /   \
#                /     \
#               'N'    'Y'
#               / \
#              /   \
#            'I'   'A'