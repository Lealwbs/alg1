##### **DFS e BFS:**

**Busca em Profundidade (Depth First Search) e Busca em largura (Breadth First Search)**

DFS usa PILHA (STACK -> DFSTACK)

BFS usa FILA (QUEUE -> BARBEQUEUE)

VETOR \[MARCADOS]

VETOR \[ANTECESSORES]



MatrixAdj = V \* V = O(V²) 

ListaAdj = V + d(v) = O(V + E) 



* **DFS: Retornar um Caminho QUALQUER (se houver) entre 2 vertices**
* **BFS: Retorna o Caminho MAIS CURTO (se houver) entre 2 vertices**
* **Ordem de execução de tarefas com interdependência**
* **Se Há ciclos no gráfico**

Aresta de Árvore: V.marcado -> V.não\_marcado

Aresta de Retorno (Indica Ciclos): V.marcado -> V.marcado

(Um grafo direcionado é acíclico se, e somente se, a DFS não encontra nenhuma aresta de retorno)

* **Identificar componentes conexos**

\[ID\_COMPONENTES]

COMPONENTES\_COUNT++ para cada loopada de vertice



##### **GRAFO BIPARTIDO**

* Se, e somente se, não contém um ciclo de tamanho ímpar
* BFS O(V+E) colorindo cada nivel (raiz: verm, n1: azul, n2: verm...), depois verificar se uma aresta possui os terminais da mesma cor O(E).
* Custo: O(V+E) + O(E) = O(V+E)





##### **USOS DAS BUSCAS**

* Achar vértices que alcançam V: Rodar busca no grafo reverso



**Aresta de árvore:** V.em\_exploracao -> V.nao\_explorado

**Aresta de retorno:** V.em\_exploracao -> V.antecessor

**Arestas de avanço:** V.em\_exploracao -> finalizado (descendente)

**Arestas de cruzamento:** V.em\_exploracao -> finalizado (n descendente)



**DAGs =** Grafos direcionados sem ciclos (Quase árvores)



###### **Ordenação Topológica**

Ordenação horizontal (u -> v) dos vértices tal que, para toda aresta (u,v), u < v.

Um grafo direcionado com ciclo não pode ser ordenado topologicamente (pq ia ter u <- v)



**Como gerar:** Vertices terminais ficam por último na ordenação, DFS no grafo, ao terminar de explorar um vertice (vertice terminal), inserir no inicio de uma lista encadeada), terminando a busca, retorna a lista com os vértices em ordem.



**Custo:** Mesmo da DFS + Inserção no inicio da lista encadead = O(V + E) + O(1) = O(V + E)

\*Se é um DAG, então o algoritimo encontra uma ordenação topológica



###### **Componentes Fortemente Conexos**

**(Partição do conjunto de vértices) Subconjunto maximal de vértices tal que há:**

Relfexividade: Todo vértice alcança a si mesmo

Transitividade: Se u->v, e v->z, então u->z

Simetria: Tal que todo u e v são mutualmente alcançáveis



##### **Algoritmo de Kosaraju-Sharir**

**Serve para descobir os componentes conexos de um grafo. O grafo de componentes é um DAG.**

1. Rode a DFS a partir de um vértice arbitrário e compute os tempo de finalização dos vértices de G
2. Obtenha GR (grafo reverso)
3. Rode a DFS em GR escolhendo vértices em ordem decrescente do tempo de finalização obtido em 1
4. Retorne as árvores obtidas em 3 como CFCs separados

O algoritmo explora os componentes na ordem topológica do grafo de componentes



**Custo: 2 DFS O(V + E) + Calcular Grafo Reverso O(V + E) = O(V + E)**





###### **Arvore Geradora**

**É Subgrafo de um grafo com todos seus vértices e um subconjunto máximo de arestas que não formam ciclos.**

Uma árvore é geradora mínima (ou tem custo mínimo) se incluir somente as arestas de menor peso possível que ligam todos os vértices.



**Algoritmos gulosos:** Buscam uma solução ótima global a partir de soluções ótimas locais.



###### **Algoritmo Genérico para MST**

Começa com um vértice, e o conjunto de arestas S = {}, seleciona uma aresta, e se ela for segura adiciona à S



###### **Corte e Cutset**

Corte (cut) é uma partição do conjunto de vértices de G.

Cutset é um conjunto de arestas cuja remoção desconecta o corte do grafo.

A menor aresta (Aresta segura) desse cutset pertence a uma árvore geradora mínima.





##### **Algoritmo de Prim**

**Modificação do algoritmo genérico que a todo instante escolhe a aresta de menor peso do cut-set entre os vertices atualmente da árvore e os demais.**

Encontra uma árvore geradora mínima (MST) em um  grafo ponderado conexo e não direcionado.



VETOR \[ANTECESSORES] -> \[todos] = -1

VETOR \[VISITADOS] -> \[todos] = False

VETOR \[ROTULOS] -> \[raiz] = 0 e \[todos] = ∞

HEAP \[Usando os valores dos rótulos como chave]



Inicia duma origem, e enquanto o heap não tiver vazio, remove o menor elemento e marca ele.

Pra cada vértice V adjacente ao atual U, se não tiver marcado e se o peso de UV for menor que o rótulo em V:

Ele atualiza o antecessor, atualiza o rótulo, e atualiza a chave no heap.

\[ANTECESORES] Descreve a MST



Construção do Heap: O(V)

Laço principal O(V) e Cada loop remove o menor elemento do heap O(log(V))

Ao todo, todas as arestas são avaliadas para atualizar o custo mínimo O(E) e cada atualização é O(log(V))

**Custo:** O(V) \* O(log(V)) + O(E) \* O(log(V)) = O(V + E) \* O(log(V)). Como E é muito maior que V, então = O(E \* log(V))





##### **Algoritmo de Kruskal**

**Parecido com Prim, porém ele usa DSU (Estrutura para conjuntos disjuntos (união-busca)**

Todas os vertices viram arvores individuais, e enquanto tiver mais que uma árvore, ele escolhe a aresta de menor custo do grafo e uni as 2 arvores que a aresta encosta.



* **Quick-Find**

Armazena-se os conjuntos em uma lista encadeada, no inicio cada elemento é associado numa lista que tem só ele

Make-set O(n), (cada uma das n listas requer O(1) para ser criada).

Fund-set O(1), retorna o primeiro elemento da lista (representante),

Union O(n²), em geral (n elementos, realizando até n-1 operações)

pode ser reduzido para O(m + nlog(n)) m = operações, n = elementos



* **Quick-Union**

Arvore em que cada nó de um elemento aponta para seu pai na árvore, a raiz aponta pra si mesmo. O find-set segue os nós da árvore até encontrar a raiz (representante).

Make-set O(n), (cria uma arvore por elemento = O(1) \* V com a raiz apontando para si mesma)

Find-set O(n), já que a árvore pode degenerar para uma lista encadeada

Union O(1), a união faz com que a raiz de uma árvore aponte para a raiz da outra, 

Para o find, pode-se aplicar união pela altura, para manter a árvore melhor balanceada e compressão de caminhos para evitar o pior caso do find-set, tornando ele O(m \* k), com m = operações, e n = elementosm, k = f(n) com um crescimento bem lento.



Ordenar as arestas O(E \* log(E)), E < V², como log(E) = O(log(V)), logo fica O(E \* log(V))

V operações de make-set = O(V) \* 1 = O(V)

E operações de find-set e union para cada aresta = E \* (find-set + union)

com Union-Find com as 2 otimizações, temos que find-set + union = k(V) + O(1) = k(V), onde o crescimento é quase constante, assim fica: O(E) \* O(k(V))

Como E < V², O (log(E) = O(log(V)), então:

**Custo:** O(E log(V)) + O(V) + O(E \* k(V)) = O(E \* log(V)), igual a prim





###### Todos subcaminho de um caminho mais curto é um caminho mais curto



##### **Algoritmo de Dijkstra**

**Não admite arestas negativas**

* Caminhos mais curtos a partir de uma única origem
* Encontrar o caminho mais curto para um único destino
* Encontrar o menor caminho entre um par de vértices
* Encontrar o menor caminho entre todos os pares de vértices



É parecido com Prim, usa estratégia gulosa, e encontra a solução ótima



VETOR \[PESOS\_ESTIMADOS]: todos = infinito, exceto \[0] = 0 - Estimativa (limite superior) de menor caminho entre S e os demais

Caso exista um caminho mais curto p/ V que a estimativa atual, o antecessor e a estimativa de V são atualizados. (Relaxados)

VETOR \[ANTECESSORES]: todos = -1

MINHEAP com os PESOS\_ESTIMADOS como chave



Enquanto o heap não tiver vazio, pega o menor (inicialmente o 0:start), e pra cada vértice adjacente, relaxa o vértice,

ou seja, se o caminho atual de start->vertice\_v for menor que algum outro caminho guardado anteriormente, troca e muda o pai.



Vetor de antecessores: O(V)

Laço, todos os vértices: O(V), cada chamada remove o menor elemento do heap O(log(V)) = O(V\*log(V)

Todas as arestas são avaliadas, ou seja, são feitos no pior caso O(E) relaxamentos, incorrendo O(log(V)) cada um = O(E\*log(V))

**Custo:** O(V\*log(V) + E\*log(V)) = O((V+E) \* log(V)) = O(E \* log(V))





##### **Algoritmo de Bellman-Ford**

**Admite arestas negativas**

* Computa o caminho mais curto
* Detecta ciclos negativos (retorna falso caso exista ciclo negativo)



Relaxa as arestas do grafo V-1 vezes, se depois de todas as iterações, existirem vértices relaxaveis, então existe ciclo negativo no grafo.



VETOR \[PESOS\_ESTIMADOS]: todos = infinito, exceto \[0] = 0 

VETOR \[ANTECESSORES]: todos = -1



Loopa V-1 vezes: Para cada aresta do grafo, relaxa ela

Depois, para cada a aresta, se for possível relaxar mais uma vez, tem ciclo negativo e retorna falso. Se não houver ciclos, retorna verdadeiro



Custo: O(V \* E), pois executa O(V) relaxações em todas as arestas

É mais caro que Dijkstra, mas não assume que os pesos são positivos.





##### **Algoritmo de Ford-Fulkerson**

**Fluxo máximo em: Origem S -> Intermediários -> Destino T**

**Os pessos associados à arestas são chamados de capacidade.**



Objetivo: Determinar um fluxo máximo entre a origem e destino, os vértices intermediários não retém fluxo.

**Conservação de fluxo:** Fluxo de entrada = Fluxo de Saída. Fluxo transmitido por uma rede = Fluxo que sai por S

**Restrição de capacidade:** O fluxo de uma aresta não pode ultrapassar a capacidade máxima.



Inicializamos todos os fluxos com zero, em seguida buscamos um caminho entre s e t sem saturar capacidade das arestas

Aresta pra frente (Forward Edges): Aumentar o fluxo na direção da aresta (u,v)

Aresta pra trás (Backward Edges): "Devolver" o fluxo na aresta (u,v)

P = Caminho aumentante: caminho simples entre S e T no grafo residual Gf

R = Gargalo de P: Menor capacidade das arestas



Aumentar Fluxo: Se (u,v) é uma aresta para frente, o fluxo += R, se (u, v) é pra trás, fluxo (v, u) -= r



Alogrítmo: Para todo vértice do grafo, fluxo = 0. Enquanto existir caminho aumentante, (ou seja, no grafo residual, enquanto tiver como S chegar a T), aumenta o fluxo das arestas do caminho aumentante, e faz isso até não existir mais caminho aumentante (de S até T)



Se as capacidades forem irracionais, o algorítmo pode não chegar num resultado, mas se forem inteiras, ele converge



Inicializar todos fluxos com zero = O(E)

Fluxo máximo = F, o incremento é pelo menos >= 1, logo, o ciclo principal é executado no máximo F vezes

Computar um caminho com DFS ou BFS: em Gf tem custo O(E)

Aumentar fluxo avalia todas as arestas do caminho simples O(V)

A construção do gráfico residual é O(E)

**Custo:** O(F \* E), pois V <= E



##### **Teorema Max-Flow Min-Cut**

**Em todo fluxo em redes, o valor do fluxo máximo é igual ao valor da menor capacidade de um corte s-t**



##### **Algoritmo Capacity-Scaling**

**Eleger o caminho aumentante com o maior gargalo, buscando eles com gargalos, no mínimo, iguais a um parâmetro Δ**

Para isso, busca um caminho aumentante num subconjunto do grafo residual com somente as arestas com capacidade >= Δ



O algoritmo inicia com Δ **= 2^lg(maior\_capacidade\_de\_saida\_de\_S)**

Depois reduz pela metade, o ciclo repete enquanto Δ >= 1



Assim, pra cada aresta, ele seta o fluxo = 0, faz o grafo residual, e enquanto Δ >= 1,

enquanto existir caminho aumentando no Gf(Δ) (grafo residual que contém só as arestas dentro do parâmetro.

Ele acha o caminho (de s à t) nessas arestas, aumenta o fluxo, faz o grafo residual novamente, e divide o parametro Δ por 2

Na última iteração com Δ=1, o algoritmo é idêntico a Ford-Fulkerson



O laço externo controlandO o parâmetro é executado no máximo O(lg(C))

Custo: O(E² \* lg(C))





##### **Algoritmo de Edmonds-Karp**

**Modificação do algoritmo de Ford-Fulkerson**



O caminho é recuperado através de uma modificação da busca em largura, ou seja, ele é o menor caminho aumentante (em número de arestas), O(E)

Os caminhos podem ter tamanho de 1 a V, CADA ARESTA PODE PARTICIPAR DE UM CAMINHO DE TAMANHO k, logho existem no máximo O(VE) caminhos aumentantes

essa modificação faz com que o custo seja O(E²\* V)



Resumo:



| Algoritmo                          | Objetivo principal                                                             | Complexidade                            | Observação / Lógica principal                                                                |

| ---------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------- | -------------------------------------------------------------------------------------------- |

| \*\*DFS (Depth-First Search)\*\*       | Explorar todos os vértices/arestas, verificar conectividade, detectar ciclos   | O(V + E)                                | Vai “profundamente” até não poder mais; útil para componentes conexos, topological sort etc. |

| \*\*BFS (Breadth-First Search)\*\*     | Explorar vértices por camadas, achar caminho mais curto em grafo não ponderado | O(V + E)                                | Visita primeiro os vértices mais próximos; gera árvore de camadas.                           |

| \*\*Karzanov–Sharir (fluxo máximo)\*\* | Algoritmo polinomial para fluxo máximo (similar ao Dinic, mas menos eficiente) | O(V²E)                                  | Usa caminhos aumentantes em camadas; precursor do Dinic.                                     |

| \*\*Prim\*\*                           | Encontrar Árvore Geradora Mínima (MST)                                         | O(E log V) (com heap)                   | Expande a MST a partir de um vértice, sempre pegando a aresta mais barata que conecta.       |

| \*\*Kruskal\*\*                        | Encontrar Árvore Geradora Mínima (MST)                                         | O(E log V)                              | Ordena arestas e une componentes com Union-Find; cresce pela menor aresta global.            |

| \*\*Dijkstra\*\*                       | Caminho mínimo a partir de uma origem (sem pesos negativos)                    | O((V + E) log V) (com heap)             | Relaxa arestas, escolhendo sempre o vértice de menor distância ainda não processado.         |

| \*\*Bellman-Ford\*\*                   | Caminho mínimo com pesos negativos (sem ciclos negativos)                      | O(VE)                                   | Relaxa todas as arestas V-1 vezes; detecta ciclos negativos.                                 |

| \*\*Ford-Fulkerson\*\*                 | Fluxo máximo em grafos com capacidades                                         | O(EF), onde F = fluxo máximo            | Aumenta fluxo via caminhos aumentantes; complexidade depende do valor de F.                  |

| \*\*Capacity Scaling\*\*               | Fluxo máximo otimizado com escalonamento de capacidade                         | O(E² log U), onde U = capacidade máxima | Busca caminhos aumentantes só com arestas de capacidade ≥ Δ; Δ diminui exponencialmente.     |

| \*\*Edmonds-Karp\*\*                   | Fluxo máximo com escolha do menor caminho aumentante (BFS)                     | O(VE²)                                  | Garante polinomial; cada aresta pode saturar/dessaturar O(V) vezes.                          |





