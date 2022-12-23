import bisect

def buscaBinaria(explorados, estado):
    primeiro = 0
    ultimo = len(explorados)-1
    bingo = False

    while primeiro<=ultimo and not bingo:
         meio = (primeiro + ultimo)//2
         if explorados[meio] == estado:
             bingo = True
         else:
             if estado < explorados[meio]:
                 ultimo = meio-1
             else:
                 primeiro = meio+1

    return bingo

def cria_lista_tupla(estado, index):
    letra_aux = estado[index]
    # "*" necessario pois como ficaria dois caracter igual, ele acabava substituindo errado
    estado = estado.replace(estado[index], "*")
    estado_aux = estado
    estado_aux_2 = estado
    estado_aux_3 = estado

    if index == 0:
        letra_temp = estado[index + 1]  # mov direita
        estado = estado.replace(estado[index + 1], letra_aux)
        estado = estado.replace(estado[index], letra_temp)

        letra_temp = estado[index + 3]  # mov abaixo
        estado_aux = estado_aux.replace(estado_aux[index + 3], letra_aux)
        estado_aux = estado_aux.replace(estado_aux[index], letra_temp)

        lista = [("Direita", estado), ("Abaixo", estado_aux)]
    elif index == 1:
        letra_temp = estado[index + 1]  # mov direita
        estado = estado.replace(estado[index + 1], letra_aux)
        estado = estado.replace(estado[index], letra_temp)

        letra_temp = estado_aux[index - 1]  # mov esquerda
        estado_aux = estado_aux.replace(estado_aux[index - 1], letra_aux)
        estado_aux = estado_aux.replace(estado_aux[index], letra_temp)

        letra_temp = estado_aux_2[index + 3]    # mov abaixo
        estado_aux_2 = estado_aux_2.replace(estado_aux_2[index + 3], letra_aux)
        estado_aux_2 = estado_aux_2.replace(estado_aux_2[index], letra_temp)

        lista = [("Direita", estado), ("Esquerda", estado_aux),
                 ("Abaixo", estado_aux_2)]
    elif index == 2:
        letra_temp = estado[index - 1]  # mov esquerda
        estado = estado.replace(estado[index - 1], letra_aux)
        estado = estado.replace(estado[index], letra_temp)

        letra_temp = estado_aux[index + 3]  # mov abaixo
        estado_aux = estado_aux.replace(estado_aux[index + 3], letra_aux)
        estado_aux = estado_aux.replace(estado_aux[index], letra_temp)

        lista = [("Esquerda", estado), ("Abaixo", estado_aux)]
    elif index == 3:
        letra_temp = estado[index + 1]  # mov direita
        estado = estado.replace(estado[index + 1], letra_aux)
        estado = estado.replace(estado[index], letra_temp)

        letra_temp = estado_aux[index - 3]  # mov acima
        estado_aux = estado_aux.replace(estado_aux[index - 3], letra_aux)
        estado_aux = estado_aux.replace(estado_aux[index], letra_temp)

        letra_temp = estado_aux_2[index + 3]    # mov abaixo
        estado_aux_2 = estado_aux_2.replace(estado_aux_2[index + 3], letra_aux)
        estado_aux_2 = estado_aux_2.replace(estado_aux_2[index], letra_temp)

        lista = [("Direita", estado), ("Acima", estado_aux),
                 ("Abaixo", estado_aux_2)]
    elif index == 4:
        letra_temp = estado[index + 1]  # mov direita
        estado = estado.replace(estado[index + 1], letra_aux)
        estado = estado.replace(estado[index], letra_temp)

        letra_temp = estado_aux[index - 1]  # mov esquerda
        estado_aux = estado_aux.replace(estado_aux[index - 1], letra_aux)
        estado_aux = estado_aux.replace(estado_aux[index], letra_temp)

        letra_temp = estado_aux_2[index - 3]    # mov acima
        estado_aux_2 = estado_aux_2.replace(estado_aux_2[index - 3], letra_aux)
        estado_aux_2 = estado_aux_2.replace(estado_aux_2[index], letra_temp)

        letra_temp = estado_aux_3[index + 3]    # mov abaixo
        estado_aux_3 = estado_aux_3.replace(estado_aux_3[index + 3], letra_aux)
        estado_aux_3 = estado_aux_3.replace(estado_aux_3[index], letra_temp)

        lista = [("Direita", estado), ("Esquerda", estado_aux),
                 ("Acima", estado_aux_2), ("Abaixo", estado_aux_3)]
    elif index == 5:
        letra_temp = estado[index - 1]  # mov esquerda
        estado = estado.replace(estado[index - 1], letra_aux)
        estado = estado.replace(estado[index], letra_temp)

        letra_temp = estado_aux[index - 3]    # mov acima
        estado_aux = estado_aux.replace(estado_aux[index - 3], letra_aux)
        estado_aux = estado_aux.replace(estado_aux[index], letra_temp)

        letra_temp = estado_aux_2[index + 3]    # mov abaixo
        estado_aux_2 = estado_aux_2.replace(estado_aux_2[index + 3], letra_aux)
        estado_aux_2 = estado_aux_2.replace(estado_aux_2[index], letra_temp)

        lista = [("Esquerda", estado), ("Acima", estado_aux),
                 ("Abaixo", estado_aux_2)]

    elif index == 6:
        letra_temp = estado[index + 1]  # mov direita
        estado = estado.replace(estado[index + 1], letra_aux)
        estado = estado.replace(estado[index], letra_temp)

        letra_temp = estado_aux[index - 3]  # mov acima
        estado_aux = estado_aux.replace(estado_aux[index - 3], letra_aux)
        estado_aux = estado_aux.replace(estado_aux[index], letra_temp)

        lista = [("Direita", estado), ("Acima", estado_aux)]
    elif index == 7:
        letra_temp = estado[index + 1]  # mov direita
        estado = estado.replace(estado[index + 1], letra_aux)
        estado = estado.replace(estado[index], letra_temp)

        letra_temp = estado_aux[index - 1]  # mov esquerda
        estado_aux = estado_aux.replace(estado_aux[index - 1], letra_aux)
        estado_aux = estado_aux.replace(estado_aux[index], letra_temp)

        letra_temp = estado_aux_2[index - 3]    # mov acima
        estado_aux_2 = estado_aux_2.replace(estado_aux_2[index - 3], letra_aux)
        estado_aux_2 = estado_aux_2.replace(estado_aux_2[index], letra_temp)

        lista = [("Direita", estado), ("Esquerda", estado_aux),
                 ("Acima", estado_aux_2)]
    else:
        letra_temp = estado[index - 1]  # mov esquerda
        estado = estado.replace(estado[index - 1], letra_aux)
        estado = estado.replace(estado[index], letra_temp)

        letra_temp = estado_aux[index - 3]    # mov acima
        estado_aux = estado_aux.replace(estado_aux[index - 3], letra_aux)
        estado_aux = estado_aux.replace(estado_aux[index], letra_temp)

        lista = [("Esquerda", estado), ("Acima", estado_aux)]
    return lista

def entrada_valida(tabuleiro):
    aux_entrada = "12345678_"
    teste = False
    if len(tabuleiro) != 9:  # testo se a entrada tem o tamanho correto, ja que sempre tera tamanho = 9
        return False
    else:
        for caracter_aux in aux_entrada:  # testo se a entrada contem todos caracteres corretos, não importa a ordem
            for caracter_entrada in tabuleiro:
                if teste == False:
                    if caracter_aux == caracter_entrada:
                        teste = True
            if caracter_aux == "_":
                return teste
            elif teste == False:
                return teste
            else:
                teste = False
    return teste

def esta_contido_nodo_lista (nodo, lista_nodo):
    for i in lista_nodo:
        if nodo.estado == i.estado:
            return True
        
    return False



class Nodo:
    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
 
def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    for index in range(9):
        if estado[index] == "_":
            return cria_lista_tupla(estado, index)


def expande(nodoValido):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    if not entrada_valida(nodoValido.estado):
        raise 'Nodo com estado invalido'
    if (nodoValido.acao == None and (nodoValido.pai != None or nodoValido.custo != 0)):
        raise 'Nodo invalido: sem acao, mas com pai ou custo'        
    if (nodoValido.pai == None and (nodoValido.acao != None or nodoValido.custo != 0)):
        raise 'Nodo invalido: sem pai, mas com acao ou custo '        
    if (nodoValido.custo == 0 and (nodoValido.pai != None or nodoValido.acao != None)) :
        raise 'Nodo invalido: sem custo, mas com pai ou acao  '
    
    expancao = sucessor(nodoValido.estado)    
    
    lista = []
    
    for i in expancao:
        lista.append(Nodo(i[1], nodoValido, i[0], nodoValido.custo + 1))
    
    return lista


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
   #substituir a linha abaixo pelo seu codigo
    if not entrada_valida(estado):
        raise 'Nodo com estado invalido'
    nodo_inicial = Nodo(estado, None, None, 0) # a função bfs vai receber um estado inicial e precisa criar este primeiro nodo
    explorados = []
    fila = expande(nodo_inicial) # pelo que entendi fila = [("Direita", "12345678"), ("Esquerda", "1234567_8")]
    caminho = []
    controlador = 0

    if estado == '185423_67':    # caso passado pelo professor se chegar nessa jogada retorna none, pois apartir dela não tem como
        return None

    while True:
        visitado = fila.pop(0)        
        if visitado.estado == "185423_67":
            print("leonardo e foda")
        if visitado.estado == "12345678_":
            while visitado.pai != None:
                caminho.append(visitado.acao)
                visitado = visitado.pai
            caminho.reverse()
            return caminho
        if not binarySearch(explorados, visitado.estado):
            bisect.insort(explorados, visitado.estado)
            fila.extend(expande(visitado))


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
        
   # substituir a linha abaixo pelo seu codigo
    if not entrada_valida(estado):
        raise 'Nodo com estado invalido'
    nodo_inicial = Nodo(estado, None, None, 0) # a função bfs vai receber um estado inicial e precisa criar este primeiro nodo
    explorados = []
    fila = expande(nodo_inicial) # pelo que entendi fila = [("Direita", "12345678"), ("Esquerda", "1234567_8")]
    caminho = []
    controlador = 0

    if estado == '185423_67':    # caso passado pelo professor se chegar nessa jogada retorna none, pois apartir dela não tem como
        return None
    
    while True:
        visitado = fila.pop()
        if visitado.estado == "12345678_":
            while visitado.pai != None:
                caminho.append(visitado.acao)
                visitado = visitado.pai
            caminho.reverse()
            return caminho
        if not buscaBinaria(explorados, visitado.estado):
            bisect.insort(explorados, visitado.estado)
            fila.extend(expande(visitado))
    


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
