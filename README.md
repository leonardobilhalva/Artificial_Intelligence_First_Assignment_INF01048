# Artificial_Intelligence_First_Assignment_INF01048

Leonardo Barros Bilhalva - 315768
Gilmar Fêlix da Rosa - 00303051

Bibliotecas usadas:

1.bisect -> utilizamos para fazer a inserção ordenada em lista ordenada - ref: https://stackoverflow.com/questions/8024571/insert-an-item-into-sorted-list-in-python

Utilizamos também um algoritmo de busca binária comum para fazer as buscas.
A ideia da busca binaria e inserção por bisect foi que estavamos perdendo muito tempo nas procuras por elementos repetidos nas listas de explorados. Então, deixamos de fazer uma lista de nodos para fazer uma lista de estados(strings) e aplicamos a inseração e busca binária. Bingo!

------------

Para as funções de astar - modificamos a função de inserção binária do bisect para trabalhar a nossa lista de tuplas. A tupla que tratamos é composta por um nodo e uma heuristica. A função de inserção continua igual, mas a orientação do teste é feita sobre a heurística, ou seja, utilizamos esse número para decidir qual ficará mais a frente e inserimos a tupla com base nele.

Não sabiamos se poderiamos aumentar a classe nodo para ter a heuristica junto nela. Isso pouparia a criação de uma lista de tuplas para uma simples lista de nodos. Então, criamos a lista de tupla.
